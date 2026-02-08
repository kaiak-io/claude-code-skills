"""
Shared utilities for the research pipeline.
"""

import os
import yaml
import logging
from datetime import datetime, date
from pathlib import Path
from urllib.parse import urlparse, urlunparse
from dotenv import load_dotenv

load_dotenv()

# Configure logging
def setup_logging(log_dir: Path):
    """Set up logging to file and console."""
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "pipeline.log"

    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def log(script: str, level: str, message: str):
    """Log a message with script context."""
    logger = logging.getLogger(script)
    getattr(logger, level.lower())(message)


def load_config(config_path: Path = None) -> dict:
    """Load and validate config.yaml."""
    if config_path is None:
        # Look for config.yaml in current directory or parent
        for path in [Path("config.yaml"), Path("../config.yaml"), Path(__file__).parent.parent / "config.yaml"]:
            if path.exists():
                config_path = path
                break

    if config_path is None or not config_path.exists():
        raise FileNotFoundError("config.yaml not found. Copy config.yaml.example to config.yaml and configure.")

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Validate required fields
    required = ["settings", "topics"]
    for field in required:
        if field not in config:
            raise ValueError(f"Missing required config field: {field}")

    return config


def normalize_url(url: str) -> str:
    """Normalize URL for deduplication - strip trailing slashes, query params, anchors."""
    parsed = urlparse(url)
    # Keep scheme, netloc, and path only
    normalized = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))
    return normalized.lower()


def get_seen_urls(topic: str, base_dir: Path) -> set:
    """Get set of already-seen URLs for a topic."""
    seen_file = base_dir / "topics" / topic / ".seen_urls"
    if not seen_file.exists():
        return set()

    with open(seen_file, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())


def mark_url_seen(url: str, topic: str, base_dir: Path):
    """Mark a URL as seen for a topic."""
    seen_file = base_dir / "topics" / topic / ".seen_urls"
    seen_file.parent.mkdir(parents=True, exist_ok=True)

    with open(seen_file, "a", encoding="utf-8") as f:
        f.write(normalize_url(url) + "\n")


def is_url_seen(url: str, topic: str, base_dir: Path) -> bool:
    """Check if URL has been seen before."""
    seen_urls = get_seen_urls(topic, base_dir)
    return normalize_url(url) in seen_urls


def get_last_run(topic: str, base_dir: Path) -> datetime | None:
    """Get the last run timestamp for a topic."""
    last_run_file = base_dir / "logs" / f"last_run_{topic}.txt"

    if not last_run_file.exists():
        return None

    with open(last_run_file, "r", encoding="utf-8") as f:
        timestamp_str = f.read().strip()
        try:
            return datetime.fromisoformat(timestamp_str)
        except ValueError:
            return None


def set_last_run(topic: str, base_dir: Path):
    """Update the last run timestamp for a topic."""
    logs_dir = base_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    last_run_file = logs_dir / f"last_run_{topic}.txt"
    with open(last_run_file, "w", encoding="utf-8") as f:
        f.write(datetime.now().isoformat())


FREQUENCY_DAYS = {
    "daily": 1,
    "every_2_days": 2,
    "every_3_days": 3,
    "weekly": 7,
    "biweekly": 14
}

def is_topic_due(topic_config: dict, topic_name: str, base_dir: Path) -> bool:
    """Check if a topic should run based on its frequency and last run."""
    frequency = topic_config.get("frequency", "weekly")
    interval_days = FREQUENCY_DAYS.get(frequency, 7)

    last_run = get_last_run(topic_name, base_dir)

    if last_run is None:
        return True  # Never run before

    days_since = (datetime.now() - last_run).days
    return days_since >= interval_days


def today_folder(topic: str, base_dir: Path) -> Path:
    """Get or create today's sources folder for a topic."""
    today_str = date.today().isoformat()
    folder = base_dir / "topics" / topic / "sources" / today_str
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def get_topics_dir(base_dir: Path) -> Path:
    """Get the topics directory."""
    topics_dir = base_dir / "topics"
    topics_dir.mkdir(parents=True, exist_ok=True)
    return topics_dir


def get_digests_dir(base_dir: Path) -> Path:
    """Get the digests directory."""
    digests_dir = base_dir / "digests"
    digests_dir.mkdir(parents=True, exist_ok=True)
    return digests_dir


def extract_text(filepath: Path) -> str:
    """Extract text content from a file (PDF, HTML, MD, TXT)."""
    suffix = filepath.suffix.lower()

    if suffix == ".pdf":
        try:
            import PyPDF2
            with open(filepath, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text.strip()
        except ImportError:
            log("utils", "warning", "PyPDF2 not installed, cannot extract PDF text")
            return ""
        except Exception as e:
            log("utils", "error", f"Failed to extract PDF text: {e}")
            return ""

    elif suffix in [".html", ".htm"]:
        try:
            from bs4 import BeautifulSoup
            with open(filepath, "r", encoding="utf-8") as f:
                soup = BeautifulSoup(f.read(), "html.parser")
                # Remove script and style elements
                for tag in soup(["script", "style", "nav", "header", "footer"]):
                    tag.decompose()
                return soup.get_text(separator="\n", strip=True)
        except ImportError:
            log("utils", "warning", "BeautifulSoup not installed, cannot extract HTML text")
            return ""
        except Exception as e:
            log("utils", "error", f"Failed to extract HTML text: {e}")
            return ""

    elif suffix in [".md", ".txt", ".markdown"]:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    else:
        log("utils", "warning", f"Unsupported file type: {suffix}")
        return ""


def markdown_to_html(markdown_text: str) -> str:
    """Convert markdown to HTML for email."""
    try:
        import markdown
        return markdown.markdown(markdown_text)
    except ImportError:
        # Fallback: wrap in pre tag
        return f"<pre>{markdown_text}</pre>"


def sanitize_filename(name: str) -> str:
    """Make a string safe for use as a filename."""
    # Remove or replace problematic characters
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, "_")
    # Limit length
    return name[:100].strip()
