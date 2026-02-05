---
name: mdx-web-publishing
description: Formatting and publishing partner for MDX-based blog content. Handles MDX frontmatter, content pillar taxonomy, JSX component patterns, content type templates (Evergreen and Pillar posts), visual cadence, SEO/GEO optimization, and repurposing for distribution. Use when formatting drafts for a website, optimizing for search/AI discovery, or creating distribution assets. Works alongside content-research-writer (for sourcing) and content-voice-style (for writing quality).
---

# MDX Web Publishing

Formatting, optimization, and distribution for MDX-based blog content.

## MDX Frontmatter Template

```yaml
---
title: "Your Title Here"
description: "One sentence that hooks and promises value. 150-160 chars for SEO."
date: "YYYY-MM-DD"
pillar: "your-pillar-slug"
contentType: "evergreen"
readTime: "X min read"
featured: false
keywords: ["keyword one", "keyword two", "keyword three"]
interlinks:
  - "related-post-slug-one"
  - "related-post-slug-two"
  - "related-post-slug-three"
---
```

## Pillar Taxonomy

Customize these to match your site's content pillars. Example structure:

| Pillar | Slug | Use For |
|--------|------|---------|
| Practical AI | `practical-ai` | AI tools, prompts, workflows, implementation |
| Systems Thinking | `systems-thinking` | Processes, templates, organizational design |
| Leadership | `leadership` | Mindset, strategy, decision-making |
| Productivity | `productivity` | Personal productivity, work-life balance, time management |
| Education | `education` | Research-backed posts on teaching, policy, pedagogy |

Replace these with your own content pillars. The slug is used in frontmatter and URL routing.

## Component Patterns

Common MDX components. Test each in your framework before relying on them:

| Component | Notes |
|-----------|-------|
| `<Callout>` | Use `type="info\|warning\|tip"` with `title=""` |
| Before/After grids | Use JSX grid layout (see reference) |
| Comparison tables | Use JSX inline-styled tables for reliable rendering |

For full JSX code patterns (hero sections, grids, tables), see [jsx-patterns.md](references/jsx-patterns.md).

## Content Type Templates

### Evergreen Post (1,000-2,000 words, 8 min read)

```markdown
# [Title]
[Personal hook — specific moment, 2-3 sentences]
[Quick pivot to thesis]

## [First Major Point — insight-driven heading]
[~300-400 words with 1-2 inline citations]
[Personal example]
<Callout type="warning/tip/story">[Key insight]</Callout>

## [Second Major Point]
[~300-400 words with 1-2 inline citations]
[VISUAL: comparison or before/after]

## [Third Major Point]
[~300-400 words]

## Where to Start
**This week:** [Specific small action]
**This month:** [Medium commitment]
**This quarter:** [Larger initiative]
---
[CTA — one sentence, link to booking or resource]
---
## References
[Numbered list of all sources]
```

**Targets:** 6-9 citations, 2-4 personal moments, 3-4 MDX components, stats every ~200 words.

### Pillar Post (2,500-4,000 words, 12-18 min read)

```markdown
# [Comprehensive Title]
[Personal hook — the shift or realization]
[Opening stat — bold, from authoritative source]
[Thesis — what this covers and why it matters now]

## [The Current State / Reality]
[Data-dense section, multiple inline citations]
<Callout type="warning">[The gap or problem]</Callout>

## [Challenge/Opportunity 1]
[~400 words with citations, personal experience]
> *Deep dive: [Tactical Post Title](/blog/slug)*

## [Challenge/Opportunity 2-5]
[Continue pattern with deep dive links]

## [Framework / How to Think About This]
## [What Happens If You Don't Engage]

## Where to Start
**This week/month/quarter:** [Actions]
---
[CTA]
---
## References
[10-15 numbered sources]
---
## Frequently Asked Questions
### [Question someone would ask AI or Google]
[Direct 2-4 sentence answer with data]
[3-5 FAQs total]
```

**Targets:** 10-15 citations, 4-6 personal moments, 5-7 MDX components, stats every ~150 words, FAQ section required.

### Deep Dive Link Pattern

In pillar posts, link to tactical posts with:
```markdown
> *Deep dive: [Post Title](/blog/post-slug)*
```

## Visual Cadence

Insert a visual element every 300-500 words. Provide Visual Specs, not just labels:

```
[VISUAL SPEC: Bar chart comparing metric A (2024) vs (2025).
Data points: Category1=X%→Y%, Category2=X%→Y%.
Caption: "Description of what the visual shows."]
```

Use JSX comments in MDX files for specs that shouldn't render:
```jsx
{/* [VISUAL SPEC: description] */}
```

## SEO/GEO Quick Reference

For the full optimization guide, see [seo-geo-checklist.md](references/seo-geo-checklist.md).

**SEO essentials:**
- Primary keyword in title, first 100 words, and 1-2 H2s
- Meta description: 150-160 characters, compelling, includes keyword
- Clean H1 → H2 → H3 hierarchy
- Internal links to 2-3 related posts (descriptive anchor text, not "click here")
- Short, descriptive URL slugs

**GEO essentials (AI citability):**
- Core answer in first 40-60 words
- Stats with named sources every 150-200 words
- Clear, declarative sentences AI can lift directly
- Question-based headings matching how people prompt AI
- FAQ section on pillar content

## Repurposing Protocol

After a post is complete, generate these distribution assets:

**1. LinkedIn Carousel Script** — Extract 5 shifts/steps into slide-by-slide script (hook slide, 4-5 insight slides, summary + CTA slide)

**2. Spiky Point of View Post** — Take the most contrarian insight and turn it into a 200-word text-only LinkedIn/X post (contrarian opening → why conventional wisdom fails → your alternative → proof → engagement CTA)

**3. Newsletter Tease** — 150-word hook + link summary (problem statement → promise → one surprising stat → read more CTA)

## Workflow by Content Type

### Newsletter (500-800 words)
1. Hook → single tactic → CTA
2. Write in one session
3. 2-3 inline citations
4. One visual max

### Blog Post (1,000-2,000 words)
1. Tactical setup + pre-mortem
2. Outline with personal moments marked
3. Draft sections with inline citations
4. Add MDX components
5. Anti-slop pass
6. Citation verification
7. Final voice check
8. Run repurposing protocol

### Pillar Post (2,500-4,000 words)
1. Full outline with research gaps
2. Research phase — gather 10-15 sources
3. Draft in sections with inline citations
4. Add deep dive links to tactical posts
5. Write FAQ section
6. MDX component treatment
7. Full checklist review
8. Citation verification (every link clicked)
9. Run repurposing protocol
