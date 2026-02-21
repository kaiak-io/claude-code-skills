<h1 align="center">Claude Code Skills</h1>

<p align="center">
  A curated collection of production-tested skills for <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, built by <a href="https://kaiak.io">KAIAK</a>.
</p>

<p align="center">
  <a href="https://awesome.re">
    <img src="https://awesome.re/badge.svg" alt="Awesome" />
  </a>
  <a href="https://makeapullrequest.com">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome" />
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License: MIT" />
  </a>
</p>

<p align="center">
  <a href="https://kaiak.io">
    <img src="https://img.shields.io/badge/Visit-kaiak.io-4F46E5?style=for-the-badge" alt="Visit kaiak.io" />
  </a>
  <a href="https://www.linkedin.com/company/kaiak/">
    <img src="https://img.shields.io/badge/Follow_on_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Follow on LinkedIn" />
  </a>
</p>

---

Each skill follows the [Agent Skills](https://agentskills.io) open standard — compatible with Claude Code, GitHub Copilot, and OpenAI Codex CLI. Drop a skill folder into `.claude/skills/` and it just works.

---

## Contents

- [What Are Claude Skills?](#what-are-claude-skills)
- [Skills](#skills)
  - [Content Creation](#content-creation)
  - [Research](#research)
  - [Web Publishing](#web-publishing)
  - [Development](#development)
  - [Education](#education)
  - [Productivity](#productivity)
- [Getting Started](#getting-started)
- [How Skills Work](#how-skills-work)
- [Creating Your Own Skills](#creating-your-own-skills)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)

## What Are Claude Skills?

Claude Skills are markdown files that teach AI coding agents how to perform specific workflows. Each skill contains a `SKILL.md` with YAML frontmatter and structured instructions, plus optional reference files for detailed specs and examples.

Skills are portable. Create once, use across Claude Code, GitHub Copilot, and OpenAI Codex CLI.

## Skills

### Content Creation

- [LinkedIn Post Generator](skills/content-creation/linkedin-post-generator/) - Creates authentic LinkedIn posts in a practitioner-sharing style. Includes anti-engagement-bait filter, platform specs (character limits, algorithm signals, optimal posting times), and five post type templates with examples.
- [Content Research Writer](skills/content-creation/content-research-writer/) - Research partner for content creation. Handles tactical setup, pre-mortem strategy checks, outline frameworks, inline citation standards, source quality evaluation, and verification workflows.
- [Content Voice & Style](skills/content-creation/content-voice-style/) - Writing quality guard that enforces anti-AI-slop filtering (50+ banned phrases), voice preservation, personal narrative integration, bold-first formatting, and pattern staleness detection.
- [Content Orchestrator](skills/content-creation/content-orchestrator/) - Coordinates the full content pipeline from research through publication and distribution. Delegates to the other content skills — the conductor that runs the full RESEARCH → PLAN → DRAFT → REVIEW → PUBLISH → DISTRIBUTE workflow.
- [Blog Featured Images](skills/content-creation/blog-featured-images/) - Generates branded featured images for blog posts in the "Warm Editorial" style. Brand color system (5-pillar palette with color logic), Poppins typography, flat geometric illustration rules, canvas specs (1200x630px OG standard), master prompt for Claude Desktop generation, and visual concepts for 36+ posts organized by content pillar.

### Research

- [Automated Research Pipeline](skills/research/automated-research/) - Builds a search-download-summarize-digest-deliver pipeline across academic and web sources. Configurable per-topic scheduling (daily to biweekly), structured summaries, cross-topic rollups, email delivery, Google Drive sync, and NotebookLM integration for audio overviews and cross-source Q&A.

### Web Publishing

- [MDX Web Publishing](skills/web-publishing/mdx-web-publishing/) - Formatting and publishing for MDX-based blogs. Content type templates (evergreen and pillar posts), JSX component patterns, visual cadence rules, SEO/GEO optimization (including AI citability), and a repurposing protocol for LinkedIn carousels and newsletters.

### Education

- [Meeting Prep & Notes](skills/education/meeting-prep/) - Generates structured meeting agendas with time boxes and purpose tags (DECIDE, DISCUSS, INFORM, SOLVE, REVIEW). Converts rough notes into formatted minutes with decisions and action items. Templates for staff meetings, leadership teams, parent conferences, PLCs, and board presentations.

### Productivity

- [SOP Generator](skills/productivity/sop-generator/) - Turns process descriptions, rough notes, or verbal walkthroughs into structured Standard Operating Procedures. Supports both human-readable SOPs and AI Agent SOPs (the format used by AWS Strands). Includes education-specific templates for incident response, enrollment, and publishing workflows.

### Development

*Coming soon. [Contribute a skill &rarr;](CONTRIBUTING.md)*

## Getting Started

### Install a single skill

```bash
git clone https://github.com/kaiak-io/claude-code-skills.git
cp -r claude-code-skills/skills/content-creation/linkedin-post-generator/ \
  your-project/.claude/skills/linkedin-post-generator/
```

### Install all skills

```bash
for skill_dir in claude-code-skills/skills/*/*/; do
  cp -r "$skill_dir" "your-project/.claude/skills/$(basename $skill_dir)/"
done
```

### Windows (PowerShell)

```powershell
git clone https://github.com/kaiak-io/claude-code-skills.git
Get-ChildItem -Directory claude-code-skills\skills\*\* | ForEach-Object {
  Copy-Item -Recurse $_.FullName "your-project\.claude\skills\$($_.Name)\"
}
```

### Verify

Start Claude Code in your project directory. Skills load automatically and activate when relevant to your task.

See [INSTALL.md](INSTALL.md) for detailed instructions and troubleshooting.

## How Skills Work

Skills use **progressive disclosure** to stay efficient:

1. **Metadata scan** (~100 tokens) - Claude reads the YAML frontmatter to decide if a skill is relevant
2. **Full SKILL.md** (<5K tokens) - Complete instructions load when the skill activates
3. **Reference files** (variable) - Supporting details load only when needed

You can install dozens of skills without bloating Claude's context window. Only what's needed gets loaded.

### Skill structure

```
skill-name/
├── SKILL.md              # Required: YAML frontmatter + instructions
└── references/           # Optional: supporting detail files
    ├── detailed-spec.md
    └── examples.md
```

### SKILL.md format

```yaml
---
name: skill-name
description: When and how to use this skill. This is the activation trigger —
  Claude reads this to decide whether to load the full skill.
---

# Skill Title

Instructions for Claude on how to execute this workflow.
```

## Creating Your Own Skills

### Best practices

- **Keep SKILL.md under 500 lines.** Move detailed specs to `references/`.
- **Description is the activation trigger.** Be specific about when the skill applies. Include use-case phrases.
- **Concrete over abstract.** Include actual prompts, templates, and examples.
- **Test across model tiers.** Skills should work on both Sonnet and Opus.
- **Use gerund form for names.** `analyzing-code` not `code-analyzer`.

### Template

```markdown
---
name: my-skill
description: Clear description of what this skill does and when to activate it.
---

# My Skill

Brief overview.

## Core Workflow

Step-by-step instructions for Claude.

## Quick Commands

Example prompts users can try.
```

## Contributing

We welcome contributions. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Quick steps

1. Ensure your skill solves a real use case
2. Check for duplicates in existing skills
3. Follow the skill structure template
4. Test in a real Claude Code session
5. Submit a pull request

## Resources

### Official Documentation

- [Agent Skills Specification](https://agentskills.io) - The open standard these skills follow
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code) - Official Claude Code docs
- [Claude Skills Overview](https://www.anthropic.com/news/skills) - Official announcement
- [Agent Skills Engineering Blog](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) - Architecture deep dive

### Community

- [Anthropic Official Skills](https://github.com/anthropics/skills) - Reference implementations from Anthropic
- [obra/superpowers](https://github.com/obra/superpowers) - TDD workflow skills
- [Trail of Bits Skills](https://github.com/trailofbits/skills) - Security domain skills
- [VoltAgent Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills) - Curated list of 198+ skills

### From KAIAK

- [kaiak.io](https://kaiak.io) - AI-powered leadership and productivity for educators
- [Blog](https://kaiak.io/writing) - Practical AI, systems thinking, and leadership content

## License

MIT License. See [LICENSE](LICENSE) for details.

Individual skills may reference external content with different licenses — check each skill's folder for specifics.

---

<p align="center">
  <b>Built by <a href="https://kaiak.io">KAIAK</a> — AI-powered leadership for educators</b>
</p>
