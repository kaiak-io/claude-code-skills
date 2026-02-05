# Contributing

Contributions are welcome. Whether you're fixing a typo, improving an existing skill, or submitting a new one.

## Submitting a New Skill

### Requirements

1. **Follow the Agent Skills standard.** Each skill needs:
   - A folder with a descriptive kebab-case name
   - A `SKILL.md` with YAML frontmatter (`name` and `description` required)
   - Optional `references/` directory for supporting files

2. **The description field matters.** This is how Claude decides whether to activate your skill. Be specific about when and how it should be used.

3. **Keep SKILL.md under 500 lines.** Move detailed specs and examples to `references/`.

4. **Test it.** Use the skill in a real Claude Code session before submitting.

### Structure

```
your-skill-name/
├── SKILL.md              # Required
└── references/           # Optional
    └── detailed-spec.md
```

### SKILL.md Template

```yaml
---
name: your-skill-name
description: Clear description of what this skill does and when to use it.
  Include specific trigger phrases so Claude knows when to activate it.
---

# Skill Title

Brief overview of what this skill does.

## Core Workflow

Step-by-step instructions for Claude to follow.

## Quick Commands

Example prompts users can try.
```

## Improving Existing Skills

- Fix errors, update outdated information, improve clarity
- Add missing reference material
- Improve description fields for better activation accuracy

## Pull Request Guidelines

- One skill per PR unless closely related
- Brief description of what the skill does and why it's useful
- If modifying an existing skill, explain what changed and why

## Quality Standards

- No vendor self-promotion disguised as skills
- Skills should be useful beyond the author's specific setup
- Instructions should be specific and actionable
- Reference files should contain concrete examples
