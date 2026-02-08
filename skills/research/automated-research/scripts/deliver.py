#!/usr/bin/env python3
"""
Delivery script for the research pipeline.
Sends digests via email and syncs to Google Drive.
"""

import os
import sys
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date
from pathlib import Path

# Add scripts dir to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from utils import (
    load_config, log, setup_logging, get_digests_dir, markdown_to_html
)


def get_latest_digest(topic: str, base_dir: Path) -> tuple:
    """Get the latest digest file for a topic. Returns (path, content) or (None, None)."""
    digests_dir = get_digests_dir(base_dir) / topic

    if not digests_dir.exists():
        return None, None

    # Find most recent digest file
    digest_files = sorted(digests_dir.glob("*.md"), reverse=True)
    if not digest_files:
        return None, None

    latest = digest_files[0]
    with open(latest, "r", encoding="utf-8") as f:
        content = f.read()

    return latest, content


def send_email_gmail(topic: str, digest_content: str, config: dict) -> bool:
    """Send digest via Gmail SMTP."""
    gmail_address = os.getenv("GMAIL_ADDRESS")
    gmail_password = os.getenv("GMAIL_APP_PASSWORD")

    if not gmail_address or not gmail_password:
        log("deliver", "error", "GMAIL_ADDRESS and GMAIL_APP_PASSWORD environment variables required")
        return False

    recipient = config.get("recipient", gmail_address)

    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Research Digest: {topic.replace('-', ' ').title()} — {date.today().isoformat()}"
        msg["From"] = gmail_address
        msg["To"] = recipient

        # Plain text version
        msg.attach(MIMEText(digest_content, "plain"))

        # HTML version
        html_content = markdown_to_html(digest_content)
        msg.attach(MIMEText(html_content, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_address, gmail_password)
            server.send_message(msg)

        log("deliver", "info", f"Email sent to {recipient} for {topic}")
        return True

    except Exception as e:
        log("deliver", "error", f"Gmail send failed: {e}")
        return False


def send_email_resend(topic: str, digest_content: str, config: dict) -> bool:
    """Send digest via Resend API."""
    api_key = os.getenv("RESEND_API_KEY")

    if not api_key:
        log("deliver", "error", "RESEND_API_KEY environment variable required")
        return False

    try:
        import resend
        resend.api_key = api_key

        from_email = config.get("from_email", "research@resend.dev")
        recipient = config.get("recipient")

        if not recipient:
            log("deliver", "error", "No recipient configured for email delivery")
            return False

        resend.Emails.send({
            "from": from_email,
            "to": recipient,
            "subject": f"Research Digest: {topic.replace('-', ' ').title()} — {date.today().isoformat()}",
            "html": markdown_to_html(digest_content),
            "text": digest_content
        })

        log("deliver", "info", f"Email sent via Resend to {recipient} for {topic}")
        return True

    except ImportError:
        log("deliver", "error", "resend package not installed. Run: pip install resend")
        return False
    except Exception as e:
        log("deliver", "error", f"Resend send failed: {e}")
        return False


def send_email_sendgrid(topic: str, digest_content: str, config: dict) -> bool:
    """Send digest via SendGrid API."""
    api_key = os.getenv("SENDGRID_API_KEY")

    if not api_key:
        log("deliver", "error", "SENDGRID_API_KEY environment variable required")
        return False

    try:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail

        from_email = config.get("from_email", "research@yourdomain.com")
        recipient = config.get("recipient")

        if not recipient:
            log("deliver", "error", "No recipient configured for email delivery")
            return False

        message = Mail(
            from_email=from_email,
            to_emails=recipient,
            subject=f"Research Digest: {topic.replace('-', ' ').title()} — {date.today().isoformat()}",
            html_content=markdown_to_html(digest_content)
        )

        sg = SendGridAPIClient(api_key)
        sg.send(message)

        log("deliver", "info", f"Email sent via SendGrid to {recipient} for {topic}")
        return True

    except ImportError:
        log("deliver", "error", "sendgrid package not installed. Run: pip install sendgrid")
        return False
    except Exception as e:
        log("deliver", "error", f"SendGrid send failed: {e}")
        return False


def send_email(topic: str, digest_content: str, email_config: dict) -> bool:
    """Send email using configured provider."""
    provider = email_config.get("provider", "gmail").lower()

    if provider == "gmail":
        return send_email_gmail(topic, digest_content, email_config)
    elif provider == "resend":
        return send_email_resend(topic, digest_content, email_config)
    elif provider == "sendgrid":
        return send_email_sendgrid(topic, digest_content, email_config)
    else:
        log("deliver", "error", f"Unknown email provider: {provider}")
        return False


def sync_to_drive_rclone(base_dir: Path, drive_config: dict) -> bool:
    """Sync research folder to Google Drive using rclone."""
    remote_path = drive_config.get("remote_path", "Research")
    remote_name = drive_config.get("remote_name", "gdrive")

    try:
        # Check if rclone is available
        result = subprocess.run(["rclone", "version"], capture_output=True)
        if result.returncode != 0:
            log("deliver", "error", "rclone not found. Install from https://rclone.org/install/")
            return False

        # Sync digests folder
        digests_dir = base_dir / "digests"
        if digests_dir.exists():
            cmd = ["rclone", "sync", str(digests_dir), f"{remote_name}:{remote_path}/digests"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                log("deliver", "warning", f"rclone sync digests failed: {result.stderr}")

        # Sync topics folder (sources and notes)
        topics_dir = base_dir / "topics"
        if topics_dir.exists():
            cmd = ["rclone", "sync", str(topics_dir), f"{remote_name}:{remote_path}/topics"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                log("deliver", "warning", f"rclone sync topics failed: {result.stderr}")

        log("deliver", "info", f"Drive sync complete to {remote_name}:{remote_path}")
        return True

    except FileNotFoundError:
        log("deliver", "error", "rclone not found in PATH")
        return False
    except Exception as e:
        log("deliver", "error", f"Drive sync failed: {e}")
        return False


def get_topics_that_ran_today(config: dict, base_dir: Path) -> list:
    """Get topics that have a digest from today."""
    today_str = date.today().isoformat()
    topics_with_digests = []

    for topic_name in config.get("topics", {}).keys():
        digest_file = get_digests_dir(base_dir) / topic_name / f"{today_str}.md"
        if digest_file.exists():
            topics_with_digests.append(topic_name)

    return topics_with_digests


def main():
    """Main entry point for the delivery script."""
    # Determine base directory
    base_dir = Path.cwd()
    if not (base_dir / "config.yaml").exists():
        base_dir = Path(__file__).parent.parent
        if not (base_dir / "config.yaml").exists():
            print("Error: config.yaml not found. Run from research directory.")
            sys.exit(1)

    # Setup logging
    setup_logging(base_dir / "logs")
    log("deliver", "info", "=" * 50)
    log("deliver", "info", "Starting delivery run")

    # Load config
    try:
        config = load_config(base_dir / "config.yaml")
    except Exception as e:
        log("deliver", "error", f"Failed to load config: {e}")
        sys.exit(1)

    delivery_config = config.get("settings", {}).get("delivery", {})

    # Email delivery
    email_config = delivery_config.get("email", {})
    if email_config.get("enabled", False):
        send_on = email_config.get("send_on", "digest")

        if send_on == "digest":
            # Send email for each topic that ran today
            topics_today = get_topics_that_ran_today(config, base_dir)
            for topic in topics_today:
                digest_path, digest_content = get_latest_digest(topic, base_dir)
                if digest_content:
                    send_email(topic, digest_content, email_config)
        elif send_on == "rollup":
            # Only send weekly rollup
            rollup_dir = get_digests_dir(base_dir) / "rollups"
            today_rollup = rollup_dir / f"week-of-{date.today().isoformat()}.md"
            if today_rollup.exists():
                with open(today_rollup, "r", encoding="utf-8") as f:
                    content = f.read()
                send_email("weekly-rollup", content, email_config)
    else:
        log("deliver", "info", "Email delivery disabled")

    # Google Drive sync
    drive_config = delivery_config.get("drive", {})
    if drive_config.get("enabled", False):
        method = drive_config.get("method", "rclone")
        if method == "rclone":
            sync_to_drive_rclone(base_dir, drive_config)
        else:
            log("deliver", "warning", f"Drive sync method '{method}' not implemented, use 'rclone'")
    else:
        log("deliver", "info", "Drive sync disabled")

    log("deliver", "info", "Delivery run complete")


if __name__ == "__main__":
    main()
