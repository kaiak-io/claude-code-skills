#!/usr/bin/env python3
"""
Search script for the research pipeline.
Queries configured sources, downloads accessible content, and generates digests.
"""

import os
import sys
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, date, timedelta
from pathlib import Path
import json
import re

# Add scripts dir to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    load_config, log, setup_logging, is_topic_due, set_last_run,
    today_folder, is_url_seen, mark_url_seen, get_digests_dir,
    sanitize_filename, normalize_url
)


def search_arxiv(keywords: list, max_results: int = 20, days_back: int = 7) -> list:
    """Search arXiv for papers matching keywords."""
    results = []

    # Build query: combine keywords with OR
    query_parts = [f'all:"{kw}"' for kw in keywords]
    query = " OR ".join(query_parts)
    encoded_query = urllib.parse.quote(query)

    url = f"http://export.arxiv.org/api/query?search_query={encoded_query}&sortBy=submittedDate&sortOrder=descending&max_results={max_results}"

    try:
        log("search", "info", f"Querying arXiv: {keywords}")
        response = urllib.request.urlopen(url, timeout=30)
        xml_data = response.read()
        root = ET.fromstring(xml_data)

        # Parse entries
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        cutoff_date = datetime.now() - timedelta(days=days_back)

        for entry in root.findall("atom:entry", ns):
            try:
                title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
                summary = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
                published = entry.find("atom:published", ns).text
                link = entry.find("atom:id", ns).text  # arXiv ID URL

                # Get PDF link
                pdf_link = None
                for link_elem in entry.findall("atom:link", ns):
                    if link_elem.get("title") == "pdf":
                        pdf_link = link_elem.get("href")
                        break

                # Get authors
                authors = []
                for author in entry.findall("atom:author", ns):
                    name = author.find("atom:name", ns)
                    if name is not None:
                        authors.append(name.text)

                # Parse date and filter
                pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
                if pub_date.replace(tzinfo=None) < cutoff_date:
                    continue

                results.append({
                    "title": title,
                    "authors": authors,
                    "abstract": summary[:500] + "..." if len(summary) > 500 else summary,
                    "url": link,
                    "pdf_url": pdf_link,
                    "published": pub_date.strftime("%Y-%m-%d"),
                    "source": "arxiv"
                })
            except Exception as e:
                log("search", "warning", f"Failed to parse arXiv entry: {e}")
                continue

        log("search", "info", f"arXiv returned {len(results)} results")
        time.sleep(3)  # Rate limiting

    except Exception as e:
        log("search", "error", f"arXiv search failed: {e}")

    return results


def search_rss(feeds: list, days_back: int = 7) -> list:
    """Search RSS feeds for new entries."""
    results = []

    try:
        import feedparser
    except ImportError:
        log("search", "warning", "feedparser not installed, skipping RSS")
        return results

    cutoff_date = datetime.now() - timedelta(days=days_back)

    for feed_url in feeds:
        try:
            log("search", "info", f"Parsing RSS feed: {feed_url}")
            feed = feedparser.parse(feed_url)

            for entry in feed.entries[:20]:  # Limit per feed
                try:
                    title = entry.get("title", "Untitled")
                    link = entry.get("link", "")
                    summary = entry.get("summary", entry.get("description", ""))

                    # Parse date
                    published = entry.get("published_parsed") or entry.get("updated_parsed")
                    if published:
                        pub_date = datetime(*published[:6])
                        if pub_date < cutoff_date:
                            continue
                        pub_str = pub_date.strftime("%Y-%m-%d")
                    else:
                        pub_str = date.today().isoformat()

                    # Clean summary (remove HTML tags)
                    summary = re.sub(r"<[^>]+>", "", summary)[:500]

                    results.append({
                        "title": title,
                        "authors": [entry.get("author", "Unknown")],
                        "abstract": summary,
                        "url": link,
                        "pdf_url": None,
                        "published": pub_str,
                        "source": "rss"
                    })
                except Exception as e:
                    log("search", "warning", f"Failed to parse RSS entry: {e}")
                    continue

            time.sleep(1)  # Be nice to servers

        except Exception as e:
            log("search", "error", f"RSS feed failed ({feed_url}): {e}")

    log("search", "info", f"RSS returned {len(results)} results")
    return results


def search_brave(keywords: list, max_results: int = 10) -> list:
    """Search Brave Search API for web articles."""
    results = []
    api_key = os.getenv("BRAVE_SEARCH_KEY")

    if not api_key:
        log("search", "warning", "BRAVE_SEARCH_KEY not set, skipping web search")
        return results

    try:
        import requests
    except ImportError:
        log("search", "warning", "requests not installed, skipping web search")
        return results

    query = " ".join(keywords)

    try:
        log("search", "info", f"Querying Brave Search: {query}")
        headers = {"X-Subscription-Token": api_key}
        params = {
            "q": query,
            "count": max_results,
            "freshness": "pw"  # Past week
        }
        response = requests.get(
            "https://api.search.brave.com/res/v1/web/search",
            headers=headers,
            params=params,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()

        for result in data.get("web", {}).get("results", []):
            results.append({
                "title": result.get("title", ""),
                "authors": [result.get("profile", {}).get("name", "Unknown")],
                "abstract": result.get("description", "")[:500],
                "url": result.get("url", ""),
                "pdf_url": None,
                "published": date.today().isoformat(),
                "source": "web"
            })

        log("search", "info", f"Brave Search returned {len(results)} results")

    except Exception as e:
        log("search", "error", f"Brave Search failed: {e}")

    return results


def download_content(result: dict, save_dir: Path) -> bool:
    """Attempt to download content from a search result."""
    url = result.get("pdf_url") or result.get("url")
    if not url:
        return False

    filename = sanitize_filename(result["title"])

    try:
        # Try PDF first if available
        if result.get("pdf_url"):
            pdf_path = save_dir / f"{filename}.pdf"
            if not pdf_path.exists():
                log("search", "info", f"Downloading PDF: {result['title'][:50]}...")
                urllib.request.urlretrieve(result["pdf_url"], pdf_path)
                time.sleep(1)
                return True

        # Otherwise save as markdown with the abstract
        md_path = save_dir / f"{filename}.md"
        if not md_path.exists():
            content = f"""# {result['title']}

**Source:** {result['url']}
**Published:** {result['published']}
**Authors:** {', '.join(result.get('authors', ['Unknown']))}

## Abstract

{result.get('abstract', 'No abstract available.')}

---
*Downloaded by research pipeline on {date.today().isoformat()}*
"""
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True

    except Exception as e:
        log("search", "warning", f"Download failed for {result['title'][:30]}: {e}")
        return False

    return False


def update_candidates(topic: str, results: list, base_dir: Path):
    """Append new candidates to the topic's candidates.md file."""
    candidates_file = base_dir / "topics" / topic / "candidates.md"
    candidates_file.parent.mkdir(parents=True, exist_ok=True)

    # Create file with header if it doesn't exist
    if not candidates_file.exists():
        with open(candidates_file, "w", encoding="utf-8") as f:
            f.write(f"# Research Candidates: {topic}\n\n")
            f.write("All search results with download status.\n\n---\n\n")

    with open(candidates_file, "a", encoding="utf-8") as f:
        for result in results:
            entry = f"""
### {result['title']}
**Authors:** {', '.join(result.get('authors', ['Unknown']))}
**Published:** {result['published']}
**Source:** {result['source']}
**URL:** {result['url']}

{result.get('abstract', 'No abstract available.')}

**Status:** {'[x] Downloaded' if result.get('downloaded') else '[ ] To review'}

---
"""
            f.write(entry)


def generate_digest(topic: str, results: list, base_dir: Path, config: dict):
    """Generate a digest for this run."""
    digests_dir = get_digests_dir(base_dir) / topic
    digests_dir.mkdir(parents=True, exist_ok=True)

    digest_file = digests_dir / f"{date.today().isoformat()}.md"

    downloaded = [r for r in results if r.get("downloaded")]
    not_downloaded = [r for r in results if not r.get("downloaded")]

    topic_config = config["topics"].get(topic, {})
    frequency = topic_config.get("frequency", "weekly")

    content = f"""# {topic.replace('-', ' ').title()} — Research Digest — {date.today().isoformat()}

**Frequency:** {frequency} | **Sources searched:** {', '.join(topic_config.get('sources', []))}

## New Candidates ({len(results)})

### Downloaded & Ready for Summary ({len(downloaded)})
"""

    for r in downloaded:
        content += f"- [{r['title'][:80]}]({r['url']}) — {r['source']}\n"

    content += f"\n### Not Downloaded - Paywalled/Restricted ({len(not_downloaded)})\n"

    for r in not_downloaded:
        content += f"- [{r['title'][:80]}]({r['url']}) — {r['source']}\n"

    content += f"""

## Next Steps

1. Run `python scripts/summarize.py` to generate summaries for downloaded content
2. Review paywalled items above and retrieve manually if important
3. Check `topics/{topic}/notes/` for generated summaries

---
*Generated by research pipeline on {datetime.now().strftime('%Y-%m-%d %H:%M')}*
"""

    with open(digest_file, "w", encoding="utf-8") as f:
        f.write(content)

    log("search", "info", f"Digest saved: {digest_file}")
    return digest_file


def process_topic(topic: str, topic_config: dict, base_dir: Path, config: dict):
    """Process a single topic: search, download, generate digest."""
    log("search", "info", f"Processing topic: {topic}")

    all_results = []
    sources = topic_config.get("sources", ["arxiv"])
    keywords = topic_config.get("keywords", [])
    frequency = topic_config.get("frequency", "weekly")

    # Determine days to look back based on frequency
    days_back = {
        "daily": 2,
        "every_2_days": 3,
        "every_3_days": 4,
        "weekly": 8,
        "biweekly": 15
    }.get(frequency, 8)

    # Search each source
    if "arxiv" in sources:
        all_results.extend(search_arxiv(keywords, days_back=days_back))

    if "rss" in sources and topic_config.get("rss_feeds"):
        all_results.extend(search_rss(topic_config["rss_feeds"], days_back=days_back))

    if "web" in sources:
        all_results.extend(search_brave(keywords))

    # Filter out already-seen URLs
    new_results = []
    for result in all_results:
        if not is_url_seen(result["url"], topic, base_dir):
            new_results.append(result)
            mark_url_seen(result["url"], topic, base_dir)

    log("search", "info", f"{len(new_results)} new candidates (filtered {len(all_results) - len(new_results)} duplicates)")

    if not new_results:
        log("search", "info", f"No new content for {topic}")
        set_last_run(topic, base_dir)
        return

    # Try to download each result
    save_dir = today_folder(topic, base_dir)
    for result in new_results:
        result["downloaded"] = download_content(result, save_dir)

    # Update candidates file
    update_candidates(topic, new_results, base_dir)

    # Generate digest
    generate_digest(topic, new_results, base_dir, config)

    # Mark topic as run
    set_last_run(topic, base_dir)

    downloaded_count = sum(1 for r in new_results if r.get("downloaded"))
    log("search", "info", f"Topic {topic} complete: {downloaded_count}/{len(new_results)} downloaded")


def main():
    """Main entry point for the search script."""
    # Determine base directory (where config.yaml lives)
    base_dir = Path.cwd()
    if not (base_dir / "config.yaml").exists():
        base_dir = Path(__file__).parent.parent
        if not (base_dir / "config.yaml").exists():
            print("Error: config.yaml not found. Run from research directory or copy config.yaml.example")
            sys.exit(1)

    # Setup logging
    setup_logging(base_dir / "logs")
    log("search", "info", "=" * 50)
    log("search", "info", "Starting search run")

    # Load config
    try:
        config = load_config(base_dir / "config.yaml")
    except Exception as e:
        log("search", "error", f"Failed to load config: {e}")
        sys.exit(1)

    # Process each topic that is due
    topics_run = 0
    for topic_name, topic_config in config.get("topics", {}).items():
        if is_topic_due(topic_config, topic_name, base_dir):
            process_topic(topic_name, topic_config, base_dir, config)
            topics_run += 1
        else:
            log("search", "info", f"Skipping {topic_name} (not due yet)")

    log("search", "info", f"Search run complete. {topics_run} topics processed.")


if __name__ == "__main__":
    main()
