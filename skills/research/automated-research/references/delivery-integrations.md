# Delivery & Integration Reference

How to push research digests to email, Google Drive, and NotebookLM instead of just saving files locally.

## Email Delivery

### Option 1: Resend (Recommended — simplest)

Free tier: 100 emails/day. No server setup needed.

```python
import resend

resend.api_key = os.getenv("RESEND_API_KEY")

def send_digest(topic, digest_content, recipient):
    """Send a research digest via email."""
    resend.Emails.send({
        "from": "research@yourdomain.com",
        "to": recipient,
        "subject": f"Research Digest: {topic} — {date.today()}",
        "html": markdown_to_html(digest_content),
        "text": digest_content
    })
```

Setup:
1. Sign up at resend.com
2. Verify your domain (or use their test domain)
3. Get API key → store in `.env`
4. `pip install resend`

### Option 2: Gmail via SMTP

No third-party service needed. Uses your existing Gmail account.

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_digest_gmail(topic, digest_content, recipient):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Research Digest: {topic} — {date.today()}"
    msg["From"] = os.getenv("GMAIL_ADDRESS")
    msg["To"] = recipient

    msg.attach(MIMEText(digest_content, "plain"))
    msg.attach(MIMEText(markdown_to_html(digest_content), "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("GMAIL_ADDRESS"), os.getenv("GMAIL_APP_PASSWORD"))
        server.send_message(msg)
```

Setup:
1. Enable 2FA on your Google account
2. Generate an App Password: Google Account → Security → App Passwords
3. Store in `.env`: `GMAIL_ADDRESS` and `GMAIL_APP_PASSWORD`
4. No additional packages needed (uses Python stdlib)

### Option 3: SendGrid

Free tier: 100 emails/day.

```python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_digest_sendgrid(topic, digest_content, recipient):
    message = Mail(
        from_email="research@yourdomain.com",
        to_emails=recipient,
        subject=f"Research Digest: {topic} — {date.today()}",
        html_content=markdown_to_html(digest_content)
    )
    sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
    sg.send(message)
```

### Email Digest Format

The email version of the digest should be scannable in an inbox:

```html
<h2>Research Digest: {Topic} — {Date}</h2>
<p><strong>{N} new sources found</strong> | {downloaded} downloaded | {summarized} summarized</p>

<h3>Top Findings</h3>
<ul>
  <li><a href="{url}">{Title}</a> — {one-line summary}</li>
  <li><a href="{url}">{Title}</a> — {one-line summary}</li>
</ul>

<h3>Key Statistics</h3>
<ul>
  <li>{stat 1}</li>
  <li>{stat 2}</li>
</ul>

<h3>Emerging Themes</h3>
<p>{2-3 sentences}</p>

<hr>
<p><em>Full digest and source files available in Google Drive: <a href="{drive_link}">Open folder</a></em></p>
```

## Google Drive Integration

### Option 1: rclone (Simplest — no code)

Syncs a local folder to Google Drive automatically.

```bash
# One-time setup
rclone config
# Follow prompts: name=gdrive, type=drive, scope=drive

# Sync research folder to Drive
rclone sync ./research/digests gdrive:Research/digests
rclone sync ./research/topics gdrive:Research/topics
```

Add to the scheduled task so it runs after the pipeline:
```bash
python scripts/search.py && python scripts/summarize.py && rclone sync ./research gdrive:Research
```

### Option 2: Google Drive API (Programmatic)

More control over where files go and how they're organized.

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_drive(file_path, folder_id):
    """Upload a file to a specific Google Drive folder."""
    creds = Credentials.from_authorized_user_file("token.json")
    service = build("drive", "v3", credentials=creds)

    file_metadata = {
        "name": os.path.basename(file_path),
        "parents": [folder_id]
    }
    media = MediaFileUpload(file_path, mimetype="text/markdown")
    service.files().create(body=file_metadata, media_body=media).execute()
```

Setup:
1. Create a Google Cloud project
2. Enable the Drive API
3. Create OAuth credentials (Desktop app)
4. Run initial auth flow to generate `token.json`
5. `pip install google-auth google-auth-oauthlib google-api-python-client`

### Drive Folder Structure

Mirror the local structure in Drive:

```
Research/
├── digests/
│   ├── ai-in-education/
│   ├── leadership/
│   └── rollups/
├── topics/
│   ├── ai-in-education/
│   │   ├── sources/
│   │   └── notes/
│   └── leadership/
│       ├── sources/
│       └── notes/
└── _latest-rollup.md        # Always-updated link to most recent rollup
```

## NotebookLM Integration

NotebookLM doesn't have a public API for direct uploads. The integration works through Google Drive:

### Workflow: Pipeline → Drive → NotebookLM

```
Research pipeline runs
  → Digests and sources saved locally
    → rclone syncs to Google Drive
      → NotebookLM notebook sources from the Drive folder
        → NotebookLM generates audio overviews, Q&A, deep summaries
```

### Setup

1. Set up Google Drive sync (see above)
2. Create a NotebookLM notebook for each research pillar
3. In each notebook, add the corresponding Drive folder as a source:
   - Add source → Google Drive → Select `Research/topics/{pillar}/notes/`
4. NotebookLM will index all summaries in that folder
5. When new summaries sync to Drive, refresh the notebook sources

### What NotebookLM Adds

NotebookLM provides capabilities the basic pipeline doesn't:

- **Audio overviews** — Generates a podcast-style summary of your research. Listen during commute.
- **Cross-source Q&A** — Ask questions across all your research: "What do the studies say about teacher AI training?"
- **Citation grounding** — Answers reference specific sources, reducing hallucination.
- **Thematic synthesis** — Identifies patterns across sources that individual summaries might miss.

### Recommended NotebookLM Notebooks

Create one notebook per pillar:

| Notebook | Drive Source Folder | Use For |
|----------|-------------------|---------|
| AI in Education | `Research/topics/ai-in-education/notes/` | Policy updates, research findings |
| Leadership | `Research/topics/leadership/notes/` | Frameworks, decision-making models |
| Systems Thinking | `Research/topics/systems-thinking/notes/` | Org design, process codification |
| No-Admin Life | `Research/topics/no-admin-life/notes/` | Productivity, workload reduction |
| Practical AI | `Research/topics/practical-ai/notes/` | Tools, workflows, implementation |
| Weekly Rollup | `Research/digests/rollups/` | Cross-pillar themes and patterns |

### NotebookLM Prompts That Work Well

Once sources are loaded:

```
"What are the three most important findings from this week's research?"
"What do these sources say about [specific question]?"
"Where do the sources disagree?"
"Generate an audio overview of the latest research on [topic]."
"What gaps exist in my research — what questions aren't answered by these sources?"
```

## Config Updates

Add delivery settings to `config.yaml`:

```yaml
settings:
  summary_model: claude-sonnet
  digest_format: markdown
  digest_location: ./digests

  delivery:
    email:
      enabled: true
      provider: gmail              # gmail, resend, or sendgrid
      recipient: "you@example.com"
      send_on: digest              # digest = after each topic digest, rollup = weekly only
    drive:
      enabled: true
      method: rclone               # rclone or api
      remote_path: "Research"
    notebooklm:
      enabled: true                # Just a flag — actual setup is manual in NotebookLM
      drive_path: "Research"       # Confirms Drive path for NotebookLM to source from
```

## Delivery Script: deliver.py

Runs after search and summarize, handles all delivery:

```python
def deliver(config):
    """Push digests and sources to configured destinations."""

    if config["delivery"]["email"]["enabled"]:
        for topic in get_topics_that_ran_today(config):
            digest = read_latest_digest(topic)
            send_email(topic, digest, config["delivery"]["email"])
            log("deliver", "INFO", f"Email sent for {topic}")

    if config["delivery"]["drive"]["enabled"]:
        sync_to_drive(config["delivery"]["drive"])
        log("deliver", "INFO", "Drive sync complete")
```

Full scheduled command becomes:
```bash
python scripts/search.py && python scripts/summarize.py && python scripts/deliver.py
```

## Required Packages

```
pip install resend              # If using Resend for email
pip install sendgrid            # If using SendGrid for email
pip install markdown            # For converting digest markdown to HTML email
pip install google-auth google-auth-oauthlib google-api-python-client  # If using Drive API
# rclone: install separately via https://rclone.org/install/
```

## Environment Variables

```bash
# .env file (add to .gitignore)
GMAIL_ADDRESS=you@gmail.com
GMAIL_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
RESEND_API_KEY=re_xxxxxxxx
SENDGRID_API_KEY=SG.xxxxxxxx
```
