---
name: sop-generator
description: Generates structured Standard Operating Procedures from process descriptions, verbal walkthroughs, or existing documentation. Produces human-readable and AI-readable SOPs in markdown format. Use when documenting workflows, codifying tribal knowledge, creating onboarding materials, or building process libraries. Supports both organizational SOPs and AI agent SOPs (the Agent SOP format used by AWS Strands and similar systems).
---

# SOP Generator

Turns process descriptions into structured, actionable Standard Operating Procedures.

## Core Philosophy

1. **Tribal knowledge is a liability.** If only one person knows how to do it, the organization is fragile. SOPs fix this.
2. **SOPs should be written for the person doing the work**, not the person who designed the process.
3. **Good SOPs are testable.** Someone unfamiliar with the process should be able to follow the SOP and get the expected result.

## Input Types

The skill accepts any of these as starting input:

- **Verbal description** — "Here's how we handle parent complaints..."
- **Rough notes** — bullet points, meeting notes, Slack messages describing a process
- **Existing document** — an outdated SOP, a wiki page, an email chain
- **Observation** — "Watch me do this and document the steps"

## SOP Output Format

Every SOP follows this structure:

```markdown
# [Process Name]

**Owner:** [Role responsible for maintaining this SOP]
**Last updated:** [Date]
**Version:** [X.X]
**Applies to:** [Who uses this SOP]

## Purpose

[One sentence: what this process accomplishes and why it matters.]

## When to Use

- [Trigger condition 1]
- [Trigger condition 2]
- [Trigger condition 3]

## Prerequisites

- [ ] [What must be true before starting]
- [ ] [Access, tools, or approvals needed]

## Steps

### Step 1: [Action verb + what to do]

[Clear instruction. One action per step.]

**Expected result:** [What you should see or have after this step]

### Step 2: [Action verb + what to do]

[Clear instruction.]

**If [exception condition]:** [What to do instead]

**Expected result:** [What you should see]

### Step 3: [Action verb + what to do]

[Continue pattern...]

## Decision Points

| If... | Then... |
|-------|---------|
| [Condition A] | [Action A] |
| [Condition B] | [Action B] |
| [Unclear / edge case] | Escalate to [role] |

## Common Mistakes

- **[Mistake 1]** — [Why it happens and how to avoid it]
- **[Mistake 2]** — [Why it happens and how to avoid it]

## Verification

How to confirm the process was completed correctly:
- [ ] [Check 1]
- [ ] [Check 2]

## Related SOPs

- [Link to upstream process]
- [Link to downstream process]
```

## Writing Rules

1. **Start each step with an action verb.** "Open," "Send," "Review," "Enter" — not "The next thing to do is..."
2. **One action per step.** If a step has "and" in it, split it.
3. **Include decision points.** Real processes have branches. Document them as tables.
4. **Name specific tools.** "Open Aeries" not "Open the student information system."
5. **Include expected results.** After each step, say what the person should see. This catches errors early.
6. **Document exceptions.** The happy path is easy. SOPs earn their value when things go wrong.
7. **Use checklists for prerequisites and verification.** Checkboxes make it easy to track completion.

## AI Agent SOP Format

For SOPs intended to be followed by AI agents (Claude Code, AWS Strands, etc.), adjust the format:

```markdown
# [Process Name]

## Context
[What the agent needs to understand about this process]

## Trigger
[When the agent should execute this SOP]

## Steps

1. [Precise instruction with tool/command specifics]
   - Input: [what the agent receives]
   - Output: [what the agent should produce]
   - Validation: [how to verify the step succeeded]

2. [Next instruction...]

## Error Handling
- If [error condition]: [recovery action]
- If [unknown error]: [escalation — alert human, log, or stop]

## Constraints
- [What the agent must NOT do]
- [Rate limits, permissions, scope boundaries]
```

Key differences from human SOPs: more explicit about inputs/outputs, stricter error handling, explicit constraints to prevent unintended actions.

## Quick Commands

**Generate SOP from description:**
```
Here's how we handle [process]: [description]. Generate a structured SOP from this.
```

**Convert rough notes to SOP:**
```
Here are my notes on [process]: [paste notes]. Turn this into a proper SOP.
```

**Create AI agent SOP:**
```
I want an AI agent to handle [task]. Generate an Agent SOP that Claude Code could follow.
```

**Review and improve existing SOP:**
```
Here's our current SOP for [process]: [paste]. Review it — flag missing steps,
unclear instructions, and undocumented decision points.
```

## References

- [sop-templates.md](references/sop-templates.md) — Domain-specific SOP templates for education, operations, and content workflows
