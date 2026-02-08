# Automated Research Pipeline

A research automation system that searches academic sources, downloads accessible content, generates AI summaries, and delivers digests via email or Google Drive.

## Quick Start

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your topics**
   ```bash
   cp config.yaml.example config.yaml
   # Edit config.yaml with your research topics and keywords
   ```

3. **Set up environment variables** (optional, for web search and email)
   ```bash
   cp .env.example .env
   # Add your API keys
   ```

4. **Run the pipeline**
   ```bash
   python scripts/search.py      # Find and download new sources
   python scripts/summarize.py   # Generate summaries with Claude
   python scripts/deliver.py     # Send emails and sync to Drive
   ```

## Requirements

- Python 3.10+
- [Claude Code CLI](https://github.com/anthropics/claude-code) for summarization
- Optional: rclone for Google Drive sync

## How It Works

### 1. Search (`search.py`)

Queries configured sources based on topic frequency:
- **arXiv**: Free academic preprints (no API key needed)
- **RSS feeds**: Blogs, newsletters, lab updates
- **Web search**: Recent articles via Brave Search API (requires key)

Downloads accessible content to `topics/{topic}/sources/{date}/`. Generates a digest in `digests/{topic}/{date}.md`.

### 2. Summarize (`summarize.py`)

Scans downloaded sources and generates structured summaries using Claude CLI:
- Key findings
- Methodology (if applicable)
- Notable data points
- Relevance and implications
- Follow-up questions

Saves summaries to `topics/{topic}/notes/`. Generates weekly rollups on the configured day.

### 3. Deliver (`deliver.py`)

Pushes content to configured destinations:
- **Email**: Gmail SMTP, Resend, or SendGrid
- **Google Drive**: Via rclone sync

## Directory Structure

```
research/
├── config.yaml              # Your configuration
├── .env                     # API keys (gitignored)
├── scripts/
│   ├── search.py           # Source discovery and download
│   ├── summarize.py        # AI summarization
│   ├── deliver.py          # Email and Drive delivery
│   └── utils.py            # Shared utilities
├── topics/
│   └── {topic-name}/
│       ├── sources/        # Downloaded content by date
│       │   └── 2026-02-08/
│       ├── notes/          # Generated summaries
│       ├── candidates.md   # All search results
│       └── .seen_urls      # Deduplication tracker
├── digests/
│   ├── {topic-name}/       # Per-topic digests
│   └── rollups/            # Weekly cross-topic rollups
└── logs/
    ├── pipeline.log        # Combined log
    └── last_run_{topic}.txt # Frequency tracking
```

## Configuration

### Topics

```yaml
topics:
  my-topic:
    frequency: weekly       # daily, every_2_days, every_3_days, weekly, biweekly
    keywords:
      - "search term 1"
      - "search term 2"
    sources:
      - arxiv
      - rss
      - web                 # Requires BRAVE_SEARCH_KEY
    rss_feeds:
      - "https://example.com/feed.xml"
    summary_focus: "specific angle or priority for summaries"
```

### Delivery

```yaml
settings:
  delivery:
    email:
      enabled: true
      provider: gmail       # gmail, resend, or sendgrid
      recipient: "you@example.com"
      send_on: digest       # digest or rollup
    drive:
      enabled: true
      method: rclone
      remote_name: gdrive
      remote_path: "Research"
```

## Environment Variables

Create a `.env` file:

```bash
# Web search (optional)
BRAVE_SEARCH_KEY=your_key_here

# Email - Gmail
GMAIL_ADDRESS=you@gmail.com
GMAIL_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx

# Email - Resend (alternative)
RESEND_API_KEY=re_xxxxxxxx

# Email - SendGrid (alternative)
SENDGRID_API_KEY=SG.xxxxxxxx
```

## Scheduling

### Windows (Task Scheduler)

```powershell
# Run search weekday mornings
schtasks /create /tn "ResearchSearch" /tr "python C:\path\to\scripts\search.py" /sc daily /st 06:00

# Run summarize and deliver evenings
schtasks /create /tn "ResearchProcess" /tr "python C:\path\to\scripts\summarize.py && python C:\path\to\scripts\deliver.py" /sc daily /st 22:00
```

### macOS/Linux (cron)

```cron
# Search: weekdays at 6 AM
0 6 * * 1-5  cd /path/to/research && python scripts/search.py

# Summarize and deliver: every night at 10 PM
0 22 * * *   cd /path/to/research && python scripts/summarize.py && python scripts/deliver.py
```

## NotebookLM Integration

The pipeline doesn't directly push to NotebookLM (no API), but you can:

1. Enable Google Drive sync
2. Create a NotebookLM notebook per topic
3. Add the Drive `notes/` folder as a source
4. NotebookLM indexes summaries for Q&A and audio overviews

## Troubleshooting

**"config.yaml not found"**
Run from the research directory or copy `config.yaml.example` to `config.yaml`.

**"Claude CLI not found"**
Install with: `npm install -g @anthropic-ai/claude-code`

**"rclone not found"**
Install from https://rclone.org/install/ and configure with `rclone config`.

**Rate limiting on arXiv**
The script includes a 3-second delay between requests. If you're still getting blocked, increase the delay in `search.py`.

**No summaries generated**
Check that:
1. Claude CLI is installed and working (`claude --version`)
2. Source files exist in `topics/{topic}/sources/`
3. Files have sufficient content (>100 characters)
