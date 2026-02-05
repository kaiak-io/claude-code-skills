# Installation Guide

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and working
- A project directory where you use Claude Code

## Quick Install

### Single skill

Copy the skill folder into your project's `.claude/skills/` directory. The folder must include both `SKILL.md` and its `references/` directory.

**macOS/Linux:**
```bash
git clone https://github.com/kaiak-io/claude-code-skills.git

cp -r claude-code-skills/skills/content-creation/linkedin-post-generator/ \
  your-project/.claude/skills/linkedin-post-generator/
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/kaiak-io/claude-code-skills.git

Copy-Item -Recurse claude-code-skills\skills\content-creation\linkedin-post-generator\ `
  your-project\.claude\skills\linkedin-post-generator\
```

### All skills

**macOS/Linux:**
```bash
for skill_dir in claude-code-skills/skills/*/*/; do
  cp -r "$skill_dir" "your-project/.claude/skills/$(basename $skill_dir)/"
done
```

**Windows (PowerShell):**
```powershell
Get-ChildItem -Directory claude-code-skills\skills\*\* | ForEach-Object {
  Copy-Item -Recurse $_.FullName "your-project\.claude\skills\$($_.Name)\"
}
```

## Verifying Installation

After copying skills, start Claude Code in your project directory. You can verify skills are loaded:

```
What skills do you have available?
```

Claude should list the installed skills by name.

## Directory Structure After Install

```
your-project/
├── .claude/
│   └── skills/
│       ├── linkedin-post-generator/
│       │   ├── SKILL.md
│       │   └── references/
│       │       ├── post-types.md
│       │       └── linkedin-specs.md
│       ├── content-research-writer/
│       │   ├── SKILL.md
│       │   └── references/
│       │       └── source-evaluation.md
│       └── ...
├── src/
└── ...
```

## Customizing Skills

Skills are plain markdown. To customize:

1. Open `SKILL.md` in any text editor
2. Modify instructions, add your preferences, adjust workflows
3. Edit reference files for detailed specs
4. Changes take effect on next Claude Code session

Common customizations:
- Adjust the LinkedIn post voice to match your style
- Add your citation format to the research writer
- Modify the SEO/GEO checklist for your platform
- Add custom keywords to the research pipeline config

## Troubleshooting

**Skills not detected:**
- Confirm `.claude/skills/` exists in your project root
- Each skill needs a `SKILL.md` file (exact name, case-sensitive)
- Restart Claude Code after adding new skills

**Reference files not loading:**
- Copy the `references/` directory alongside `SKILL.md`
- Check that relative paths in SKILL.md match actual file locations

**Too many skills:**
- Skills use progressive disclosure — metadata scanning is ~100 tokens per skill
- Keep only skills relevant to your current project
- Total skill description budget defaults to 15,000 characters
