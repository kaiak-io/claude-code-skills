---
name: content-research-writer
description: Research partner for content creation. Handles tactical setup, pre-mortem strategy checks, outline frameworks, inline citation standards, source quality evaluation, and research methodology. Use when planning, researching, or sourcing evidence for any content piece. Works alongside content-voice-style (for writing quality) and mdx-web-publishing (for formatting and SEO/GEO).
---

# Content Research Writer

Research partner for planning and sourcing content — from initial concept validation to verified citations.

## Tactical Setup

Before outlining, answer these five questions:

1. **What's the specific pain point?** Not "AI in schools" — too vague. "Teachers making daily decisions about AI without any guidance" is specific.
2. **What are the 2-4 tactical takeaways?** What will they DO differently after reading?
3. **What's your unique angle?** Why should they read YOUR take?
4. **What evidence do you have?** Data, case studies, personal experience.
5. **What personal moments can you include?** Confessions, mistakes, realizations, shifts.

## Pre-Mortem (Strategy Check)

Before drafting, ask:

- **Why might a reader ignore this?** Be honest about the competition for attention.
- **Is the pain point actually a minor annoyance?** If it's not keeping them up at night, reconsider.
- **Have 10 other people already written this exact headline?** If yes, what's your unique angle or data?

If you can't answer these convincingly, refine the concept before drafting.

## Outline Framework

```markdown
# [Working Title]

## The Hook (2-3 sentences max)
- The Problem: [Specific, felt pain]
- The Promise: "Here's exactly how to [specific outcome]"

## The Meat

### Tactic 1: [Action-oriented title]
- **The move**: [What to actually do]
- **Why it works**: [Brief rationale]
- **Example**: [Concrete illustration]
- [VISUAL SPEC: description]

### Tactic 2: [Action-oriented title]
- **The move**: [What to actually do]
- **Watch out for**: [Common pitfall]
- **Example**: [Concrete illustration]

### Tactic 3: [Action-oriented title]
- **The move**: [What to actually do]
- **The proof**: [Data point or case study]

## The Bottom Line
- Summary as single paragraph (not bullets)
- The "so what" — why this matters NOW
- One clear next step

## Research Gaps
- [ ] Need data on [specific claim]
- [ ] Find example of [concept in action]
- [ ] Source for [assertion]
```

## Citation Standard

Non-negotiable. Every data-backed claim uses **inline hyperlinked citations** in the prose.

**The pattern:** `[Source Name](URL) + context + **bold statistic**`

**Do this:**
```markdown
[RAND's 2025 study](url) found that **54% of students** now use AI for school.
[PwC's 2025 Global AI Jobs Barometer](url) analyzed nearly a billion job postings.
Workers with AI skills earn **56% more** than peers without.
```

**Never this:**
```markdown
Research shows that most students use AI (1).
Studies indicate teachers lack training.
According to experts, AI is changing education.
```

What makes citations work:
- Source is named and hyperlinked
- Context establishes credibility (sample size, methodology hint)
- Key stat is **bolded** for scannability
- Flows naturally in prose — not a footnote

## Source Quality Hierarchy

1. **Peer-reviewed research** — Nature, Scientific Reports, academic journals
2. **Major research institutions** — RAND, McKinsey, Harvard, Brookings
3. **Government/international reports** — U.S. Dept of Education, UNESCO, OECD
4. **Reputable industry research** — PwC, Cengage, Gartner, IDC
5. **Quality journalism** — NPR, PBS, NYT, WSJ (for context, not primary claims)

**Avoid:** Blog posts, LinkedIn articles, unsourced aggregator sites, vendor self-promotion disguised as research.

## Citation Density Targets

| Content Type | Target Sources | Stat Frequency |
|--------------|----------------|----------------|
| Newsletter (500-800 words) | 2-3 sources | Every ~300 words |
| Blog Post (1,000-2,000 words) | 6-9 sources | Every ~200 words |
| Pillar Post (2,500-4,000 words) | 10-15 sources | Every ~150 words |

Every post over 1,000 words ends with a References section:

```markdown
---
## References
1. [Title of Source](URL) - Organization Name
2. [Title of Source](URL) - Organization Name
```

## Source Verification

Before publishing, verify all sources. For the full verification workflow, see [source-evaluation.md](references/source-evaluation.md).

Quick checks:
- [ ] Every link clicked and loads
- [ ] Stats match what the source actually says
- [ ] Publication dates are current
- [ ] No vendor self-promotion disguised as research
- [ ] Stats traced to primary sources, not secondary aggregators
- [ ] Reference list at end matches inline citations
