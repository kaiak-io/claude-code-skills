# Search Sources Configuration

Source-specific setup, APIs, and configuration for the research pipeline.

## arXiv

**API:** Free, no key required.

**Endpoint:** `http://export.arxiv.org/api/query`

**Query parameters:**
- `search_query` — Keywords combined with AND/OR (e.g., `all:"AI alignment" AND all:"safety"`)
- `sortBy` — `submittedDate` for recency
- `sortOrder` — `descending`
- `max_results` — Cap at 20-50 per run to avoid noise
- `start` — Pagination offset

**Example query:**
```python
import urllib.request
import xml.etree.ElementTree as ET

base_url = "http://export.arxiv.org/api/query"
query = 'all:"AI alignment" AND all:"safety"'
params = f"search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results=20"
url = f"{base_url}?{params}"

response = urllib.request.urlopen(url)
root = ET.fromstring(response.read())
```

**Rate limiting:** 1 request per 3 seconds. Add `time.sleep(3)` between calls.

**Date filtering:** Parse `<published>` tag, compare against last run date.

**Category filtering (optional):** Append `cat:cs.AI` or `cat:cs.CL` to narrow results.

## Google Scholar

**No official API.** Options in order of preference:

### Option 1: SerpAPI (Recommended for reliability)
- Paid service with free tier (100 searches/month)
- Endpoint: `https://serpapi.com/search?engine=google_scholar`
- Returns structured JSON
- Handles rate limiting and CAPTCHAs

```python
from serpapi import GoogleSearch

params = {
    "engine": "google_scholar",
    "q": "continuous discovery habits",
    "as_ylo": 2025,  # Published after this year
    "num": 20,
    "api_key": "YOUR_KEY"
}
search = GoogleSearch(params)
results = search.get_dict()
```

### Option 2: scholarly (Free, less reliable)
- Python library, no API key needed
- Can get rate-limited or blocked by Google
- Best for low-volume, occasional searches

```python
from scholarly import scholarly

query = scholarly.search_pubs("AI alignment safety")
for i, paper in enumerate(query):
    if i >= 20:
        break
    print(paper['bib']['title'], paper['bib'].get('abstract', ''))
```

### Option 3: Manual trigger
- Run search weekly, open Google Scholar in browser
- Script generates the search URLs, you review in browser and download PDFs
- Most reliable, least automated

## Web Search

### Option 1: Brave Search API
- Free tier: 2,000 queries/month
- Good for recent articles, blog posts, reports

```python
import requests

headers = {"X-Subscription-Token": "YOUR_KEY"}
params = {"q": "AI safety research 2026", "freshness": "pd"}  # pd = past day
response = requests.get("https://api.search.brave.com/res/v1/web/search",
                        headers=headers, params=params)
```

### Option 2: Tavily API
- Built for AI agent research use cases
- Returns cleaned, relevant content
- Free tier: 1,000 API calls/month

```python
from tavily import TavilyClient

client = TavilyClient(api_key="YOUR_KEY")
results = client.search("AI alignment research", search_depth="advanced",
                        max_results=10, include_raw_content=True)
```

### Option 3: Claude's web search
- If running summarize.py through Claude Code, Claude can search directly
- No additional API key needed
- Less structured but works as a fallback

## RSS Feeds

**Library:** `feedparser` (free, no API key)

```python
import feedparser

feed = feedparser.parse("https://example.com/feed.xml")
for entry in feed.entries:
    title = entry.title
    link = entry.link
    published = entry.published_parsed
    summary = entry.get('summary', '')
```

**Good sources for RSS:**
- Research lab blogs (DeepMind, Anthropic, OpenAI)
- Industry newsletters
- ArXiv category feeds (e.g., `http://arxiv.org/rss/cs.AI`)
- Conference proceedings feeds
- Substack publications

**Date handling:** Compare `entry.published_parsed` against last run timestamp. Store last run time in `logs/last_run_{source}.txt`.

## API Key Management

Store API keys in environment variables, not in config.yaml:

```bash
# .env file (add to .gitignore)
SERPAPI_KEY=your_key_here
BRAVE_SEARCH_KEY=your_key_here
TAVILY_KEY=your_key_here
```

Load in scripts:
```python
import os
from dotenv import load_dotenv

load_dotenv()
serpapi_key = os.getenv("SERPAPI_KEY")
```

**Required packages:**
```
pip install feedparser python-dotenv requests
# Optional based on sources chosen:
pip install scholarly         # For Google Scholar without API
pip install google-search-results  # For SerpAPI
pip install tavily-python     # For Tavily
pip install PyPDF2            # For PDF text extraction
```

## Source Selection Guide

| Source | Best For | Cost | Reliability |
|--------|----------|------|-------------|
| arXiv | Academic preprints, CS/ML/AI research | Free | High |
| Google Scholar (SerpAPI) | Published papers across all fields | $50/mo+ | High |
| Google Scholar (scholarly) | Light academic search | Free | Medium |
| Brave Search | Web articles, blog posts, reports | Free tier | High |
| Tavily | AI-optimized web research | Free tier | High |
| RSS | Specific blogs, labs, newsletters | Free | High |

**Recommended starting setup:** arXiv (free) + Brave Search (free tier) + RSS feeds. Add Google Scholar via SerpAPI if you need broader academic coverage.
