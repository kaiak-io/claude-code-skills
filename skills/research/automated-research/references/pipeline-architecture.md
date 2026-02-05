# Pipeline Architecture

Detailed implementation reference for the two-script research automation pipeline.

## Script 1: search.py

### Flow

1. Load `config.yaml`
2. For each topic, check if the topic is due based on its `frequency` and `last_run` timestamp
3. For due topics, query each configured source with the topic's keywords
4. Deduplicate results against `candidates.md` (match by URL)
5. Auto-download all freely accessible content to `topics/{topic}/sources/{YYYY-MM-DD}/`
6. Append new candidates to `topics/{topic}/candidates.md` with download status
7. Generate digest in `digests/{topic-name}/`
8. Update `last_run` timestamp for the topic
9. Log run results

### Frequency Logic

The script runs daily but only processes topics that are due:

```python
frequency_days = {
    "daily": 1,
    "every_2_days": 2,
    "every_3_days": 3,
    "weekly": 7,
    "biweekly": 14
}

def is_topic_due(topic_config, last_run_date):
    interval = frequency_days[topic_config["frequency"]]
    return (today - last_run_date).days >= interval
```

Last run timestamps stored in `logs/last_run_{topic}.txt`.

### Source Query Logic

Each source returns a list of candidates with: title, authors, abstract/snippet, URL, date published.

- **arXiv**: Query API endpoint, filter by `submittedDate` (last 24h for daily, last 7d for weekly)
- **Google Scholar**: Query via configured method, filter recent publications
- **Web search**: Search API for recent articles matching keywords
- **RSS**: Parse configured feeds, check publication dates against last run

### Deduplication

Track seen URLs in a `.seen_urls` file per topic. Before appending a candidate, check if its URL (normalized — strip trailing slashes, query params) already exists. Skip duplicates silently.

### Candidate Output Format

Append to `topics/{topic}/candidates.md`:

```markdown
---
### {Title}
**Authors:** {Author list}
**Published:** {Date}
**Source:** {arxiv|scholar|web|rss}
**URL:** {URL}

{Abstract or first 2-3 sentences}

**Status:** [ ] To review
---
```

### Error Handling

- If a source API fails, log the error and continue with remaining sources
- If rate-limited, log and skip that source for this run
- Never let one source failure stop the entire search
- Log all errors with timestamp to `logs/search.log`

## Script 2: summarize.py

### Flow

1. Load `config.yaml`
2. For each topic, scan all date subdirectories in `sources/` for files
3. Compare against existing summaries in `notes/` (match by filename)
4. For each new file, invoke Claude to generate a summary
5. Save summary to `notes/{filename}-summary.md`
6. On the configured rollup day, generate cross-topic rollup

### File Detection

Supported input formats:
- PDF (`.pdf`) — extract text, then summarize
- Markdown (`.md`) — read directly
- HTML (`.html`, `.htm`) — strip tags, then summarize
- Plain text (`.txt`) — read directly

Match source files to summaries by stem, ignoring date subdirectory: `sources/2026-02-04/paper.pdf` → `notes/paper-summary.md`

### Claude Invocation

For each new file, call Claude with:

```
Summarize this {document_type} for a research digest.

Focus on: {topic.summary_focus}

Structure your summary as:
1. Key Findings (2-3 sentences)
2. Methodology (study design, sample, approach)
3. Notable Data (specific statistics, effect sizes)
4. Relevance (why this matters)
5. Follow-up (open questions, related work)

Be specific about numbers. Don't hedge on findings the paper states clearly.
If effect sizes are reported, include them. If methodology has limitations
the authors acknowledge, note them.
```

### Weekly Rollup Logic

On the configured rollup day (default: Sunday), generate `digests/weekly/week-of-{date}.md`:

1. Collect all summaries generated in the past 7 days across all topics
2. Group by topic
3. For each topic: list highlights, identify cross-cutting themes
4. Include counts: papers reviewed, candidates found, topics active

## Scheduling

### Windows (Task Scheduler)

```powershell
# Create search task — runs weekday mornings
schtasks /create /tn "ResearchSearch" /tr "python C:\path\to\research\scripts\search.py" /sc daily /st 06:00

# Create summarization task — runs every evening
schtasks /create /tn "ResearchSummarize" /tr "python C:\path\to\research\scripts\summarize.py" /sc daily /st 22:00
```

To modify or remove:
```powershell
schtasks /change /tn "ResearchSearch" /st 07:00
schtasks /delete /tn "ResearchSearch" /f
```

### macOS/Linux (cron)

```cron
# Search: weekdays at 6 AM
0 6 * * 1-5  cd /path/to/research && python scripts/search.py

# Summarize: every night at 10 PM
0 22 * * *   cd /path/to/research && python scripts/summarize.py
```

## Digest Templates

### Per-Topic Digest

Generated each time a topic runs, saved to `digests/{topic-name}/{YYYY-MM-DD}.md`:

```markdown
# {Topic Name} — Research Digest — {Date}
**Frequency:** {frequency} | **Period covered:** {last_run} to {today}

### New Candidates ({count})

**Downloaded & Summarized**
- [{Title}]({URL}) — {1-line summary} ({source})
  → `sources/{date}/{filename}` | `notes/{filename}-summary.md`

**Not Downloaded (paywalled/restricted)**
- [{Title}]({URL}) — {1-line summary} ({source})

### Key Statistics Surfaced
- {stat 1}
- {stat 2}

### Emerging Themes
{Patterns observed across this period's readings — 2-3 sentences}

---
*Generated by research pipeline. {downloaded} of {total} candidates downloaded and summarized.*
```

### Cross-Topic Rollup

Generated on a configurable schedule (default: weekly), saved to `digests/rollups/week-of-{date}.md`:

```markdown
# Weekly Research Rollup — Week of {Date}

## Overview
- **Topics tracked:** {count}
- **Topics that ran this week:** {list with frequencies}
- **Total candidates found:** {count}
- **Total downloaded & summarized:** {count}

## {Topic Name} ({frequency})

**{N} items summarized since last rollup**

### Key Findings
- {Finding 1 with source attribution}
- {Finding 2 with source attribution}

---

## Cross-Topic Patterns
{Any themes that span multiple research topics — include only when genuine connections exist}
```

## Logging

All scripts log to `logs/search.log` with format:

```
[{timestamp}] [{script}] [{level}] {message}
[2026-02-04 06:00:01] [search] [INFO] Starting search run for 3 topics
[2026-02-04 06:00:03] [search] [INFO] arxiv: 4 new candidates for ai-safety
[2026-02-04 06:00:05] [search] [ERROR] google_scholar: rate limited, skipping
[2026-02-04 06:00:08] [search] [INFO] Run complete. 7 new candidates total.
```

Keep logs for 30 days. Rotate or archive older logs.

## utils.py Shared Functions

Core utilities both scripts use:

- `load_config()` — Parse `config.yaml`, validate required fields
- `normalize_url(url)` — Strip trailing slashes, query params, anchors for dedup
- `is_seen(url, topic)` — Check URL against `.seen_urls`
- `mark_seen(url, topic)` — Add URL to `.seen_urls`
- `log(script, level, message)` — Append to `logs/search.log`
- `is_topic_due(topic_config)` — Check if topic should run based on frequency and last_run
- `get_last_run(topic)` — Read last run timestamp from `logs/last_run_{topic}.txt`
- `set_last_run(topic)` — Update last run timestamp after successful run
- `today_folder(topic)` — Return/create `sources/{YYYY-MM-DD}/` path for today's downloads
- `extract_text(filepath)` — Read content from PDF, HTML, MD, or TXT
