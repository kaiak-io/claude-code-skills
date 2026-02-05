---
name: automated-research
description: Builds and manages an automated research pipeline that searches academic and web sources on configured topics, summarizes new content, and delivers research digests via email, Google Drive, and NotebookLM. Use when setting up research automation, configuring search topics, creating search or summarization scripts, generating research digests, or setting up delivery integrations.
---

# Automated Research Pipeline

Builds a fully automated system: search for new content, download what's accessible, summarize everything, and deliver a digest.

## Core Design

**Search → Download → Summarize → Digest → Deliver**

1. **Search** — Query configured sources (arXiv, web, Google Scholar, RSS) for new content matching your keywords.
2. **Download** — Auto-fetch all freely accessible content (web articles, arXiv abstracts, RSS entries). Save to `sources/` as markdown. Log anything behind paywalls or auth walls for manual retrieval.
3. **Summarize** — Generate structured summaries for all new downloads via Claude. Save to `notes/`.
4. **Digest** — Compile digest on the topic's configured frequency with candidates, download status, key statistics, and emerging themes.
5. **Deliver** — Push digests to email, sync sources and summaries to Google Drive, and feed into NotebookLM for audio overviews and cross-source Q&A.

The pipeline downloads everything it can access. Paywalled or restricted content is flagged in the digest for you to retrieve manually.

## Folder Structure

```
research/
├── config.yaml                 # Topics, keywords, sources, schedule
├── scripts/
│   ├── search.py               # Queries sources for new content
│   ├── summarize.py            # Generates summaries of downloads
│   └── utils.py                # Shared: dedup, logging, file handling
├── topics/
│   └── {topic-name}/
│       ├── sources/
│       │   └── {YYYY-MM-DD}/   # Downloads organized by date fetched
│       ├── notes/              # Generated summaries (flat, accumulate over time)
│       └── candidates.md       # All search results with download status
├── digests/                    # Digests generated per topic frequency
└── logs/
```

## Config Format

Schedule is set per topic. Each topic runs on its own frequency — the pipeline checks which topics are due on each run.

```yaml
settings:
  summary_model: claude-sonnet
  digest_format: markdown       # markdown or obsidian
  digest_location: ./digests

topics:
  ai-in-education:
    keywords:
      - "AI in education"
      - "generative AI students"
      - "AI education policy"
    sources: [arxiv, google_scholar, web]
    frequency: weekly            # Run once per week
    summary_focus: "methodology, effect sizes, and policy implications"

  ai-safety:
    keywords:
      - "AI alignment"
      - "language model safety"
    sources: [arxiv, web]
    frequency: every_3_days      # Run every 3 days
    summary_focus: "methodology and effect sizes"

  product-discovery:
    keywords:
      - "continuous discovery habits"
    sources: [web, rss]
    frequency: daily             # Run every day
    rss_feeds:
      - "https://example.com/feed.xml"
    summary_focus: "practical frameworks and case studies"

# Frequency options: daily, every_2_days, every_3_days, weekly, biweekly
# The script runs daily but only processes topics that are due
```

## Summary Output

Each summary follows this structure:

```markdown
# {Title}
**Source:** {URL or filename}  |  **Date:** {Publication date}  |  **Summarized:** {Today}

## Key Findings
{2-3 sentence overview}

## Methodology
{Study design, sample, approach}

## Notable Data
{Specific statistics, effect sizes, quantitative findings}

## Relevance
{Why this matters — 1-2 sentences}

## Follow-up
{Open questions, related work to find}
```

Summaries focus on what the user specified in `summary_focus`. Default emphasis: methodology and effect sizes, not just conclusions.

## Building the Pipeline

When setting up a new pipeline:

1. Ask the user for: topics, keywords per topic, which sources to search, and where to put the research folder
2. Create the folder structure
3. Generate `config.yaml` from their inputs
4. Write `search.py`, `summarize.py`, and `utils.py`
5. Set up scheduling (Windows Task Scheduler or cron)
6. Run a test search to verify everything works

When adding a topic: update `config.yaml`, create the topic folder, run a test search.

## Quick Commands

**Set up a new pipeline:**
```
Set up an automated research pipeline for these topics: [list topics and keywords].
```

**Add a research topic:**
```
Add a new research topic "[name]" with keywords: [list].
```

**Run search now:**
```
Run the search script and generate today's research digest.
```

**Summarize new downloads:**
```
Check for new downloads in my research topics and generate summaries.
```

**Generate weekly rollup:**
```
Generate this week's research summary across all topics.
```

**Set up email delivery:**
```
Set up email delivery for my research digests using Gmail.
```

**Set up Google Drive sync:**
```
Set up Google Drive sync for my research pipeline so NotebookLM can access the sources.
```

## References

- [pipeline-architecture.md](references/pipeline-architecture.md) — Script logic, scheduling, error handling, digest templates
- [search-sources.md](references/search-sources.md) — Source-specific APIs, configuration, rate limits
- [delivery-integrations.md](references/delivery-integrations.md) — Email delivery, Google Drive sync, NotebookLM integration
