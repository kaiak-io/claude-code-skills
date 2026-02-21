---
name: content-orchestrator
description: Coordinates the full content creation pipeline from research through publication and distribution. Knows about and delegates to the other content skills — automated-research, content-research-writer, content-voice-style, blog-featured-images, mdx-web-publishing, and linkedin-post-generator. Use when planning a content piece end-to-end, running the full pipeline, or checking which step comes next. This is the conductor — the other skills are the instruments.
---

# Content Orchestrator

Runs the full content pipeline from idea to published post to social distribution. Coordinates six specialist skills.

## The Pipeline

```
RESEARCH → PLAN → DRAFT → REVIEW → PUBLISH → DISTRIBUTE
   ↓         ↓       ↓        ↓         ↓          ↓
automated  content  content  content  blog-featured linkedin
-research  -research -voice  -voice   -images +    -post
           -writer  -style   -style   mdx-web      -generator
                                      -publishing
```

Each stage has a clear input, a clear output, and a handoff to the next stage.

## Stage 1: RESEARCH

**Skill:** `automated-research`
**Input:** Topic idea or content pillar
**Output:** Research digest with downloaded sources and summaries

### What to do

1. Check the research pipeline for existing material on this topic
   - Look in `research/topics/{pillar}/notes/` for relevant summaries
   - Check `research/digests/{pillar}/` for recent digests
2. If existing research is sufficient, move to Stage 2
3. If not, run a targeted search:
   ```
   Run the research pipeline for [topic] with keywords: [list]
   ```
4. Review the digest and downloaded sources

### Handoff to Stage 2
Deliver: relevant source summaries, key statistics, notable quotes, research gaps identified.

## Stage 2: PLAN

**Skill:** `content-research-writer`
**Input:** Research findings + content idea
**Output:** Tactical setup + outline

### What to do

1. Run the tactical setup (5 questions):
   - What's the specific pain point?
   - What are the 2-4 tactical takeaways?
   - What's the unique angle?
   - What evidence do we have?
   - What personal moments can we include?

2. Run the pre-mortem:
   - Why might a reader ignore this?
   - Is the pain point actually a minor annoyance?
   - Have 10 other people written this exact headline?

3. Generate the outline using the framework from content-research-writer
4. Identify citation targets (6-9 for evergreen, 10-15 for pillar)
5. Map personal narrative moments to specific sections

### Handoff to Stage 3
Deliver: completed outline with research gaps filled, citations mapped, personal moments placed.

## Stage 3: DRAFT

**Skills:** `content-research-writer` + `content-voice-style`
**Input:** Outline with citations and narrative moments
**Output:** Full draft

### What to do

1. Draft each section following the outline
2. Apply inline citations using the citation standard:
   `[Source Name](URL) + context + **bold statistic**`
3. Insert personal narrative moments (2-6 depending on length)
4. Apply the bold-first rule to all bullet points
5. Write the hook — specific moment, not thesis statement
6. Write the close — genuine, no hedge

### Handoff to Stage 4
Deliver: complete draft with inline citations, personal moments, and proper formatting.

## Stage 4: REVIEW

**Skill:** `content-voice-style`
**Input:** Complete draft
**Output:** Reviewed and polished draft

### What to do

1. Run the anti-slop filter against the full banned phrases list
2. Check for structural tells (Triple Header, Hollow Transition, Hedged Conclusion)
3. Verify voice markers — does this sound peer-to-peer?
4. Run the calibration questions:
   - Does this sound like something I'd actually say?
   - Would I be embarrassed to read this aloud?
   - Is this how I'd explain it to a peer over coffee?
5. Check pattern staleness against last 3 posts
6. Run section feedback framework on any weak sections
7. Verify all citations:
   - Every link loads
   - Stats match what the source says
   - Publication dates are current

### Handoff to Stage 5
Deliver: polished draft that passes all quality checks.

## Stage 5: PUBLISH

**Skills:** `blog-featured-images` + `mdx-web-publishing`
**Input:** Polished draft
**Output:** Published post with featured image on the website

### What to do

1. Generate the featured image using `blog-featured-images`:
   - Find the visual concept in `references/visual-concepts.md` or design a new one
   - Use the master prompt in Claude Desktop with the per-post request format
   - Save to `public/images/posts/[slug].png`
2. Add MDX frontmatter (title, description, date, pillar, keywords, interlinks, `image`, `imageAlt`)
3. Apply JSX components (callouts, grids, hero section if applicable)
4. Enforce visual cadence — visual element every 300-500 words
5. Run SEO checklist:
   - Primary keyword in title, first 100 words, 1-2 H2s
   - Meta description: 150-160 chars
   - Clean heading hierarchy
   - Internal links to 2-3 related posts
6. Run GEO checklist:
   - Core answer in first 50 words
   - Stats with named sources every 150-200 words
   - Question-based headings
   - FAQ section (pillar posts)
7. Add references section
8. Publish

### Handoff to Stage 6
Deliver: live URL of published post.

## Stage 6: DISTRIBUTE

**Skill:** `linkedin-post-generator`
**Input:** Published post
**Output:** LinkedIn post + other distribution assets

### What to do

1. Generate LinkedIn post in practitioner-sharing style:
   - Pull one specific thing you did or learned
   - Write conversationally — not a summary of the post
   - Mention supporting material goes in comments
   - Target 1,300-1,400 characters
2. Generate repurposing assets (from mdx-web-publishing):
   - LinkedIn carousel script (5 slides)
   - Spiky point of view post (200 words)
   - Newsletter tease (150 words)
3. Schedule for optimal times (Tue-Thu, 8-10 AM)

## Running the Full Pipeline

### From scratch
```
I want to write about [topic] for the [pillar] pillar. Run the full content pipeline.
```

### From existing research
```
I have research on [topic] from the automated-research pipeline.
Pick up at Stage 2 (PLAN) and run through publication.
```

### From a draft
```
Here's a draft I wrote about [topic]: [paste]. Run Stages 4-6 (REVIEW → PUBLISH → DISTRIBUTE).
```

### Just distribution
```
I just published [post title] at [URL]. Generate the LinkedIn post and distribution assets.
```

## Pipeline Status Check

When asked "where are we?" on a piece of content, report:

```markdown
## Content Pipeline Status: [Title]

| Stage | Status | Notes |
|-------|--------|-------|
| 1. RESEARCH | Done | 6 sources, 4 summarized |
| 2. PLAN | Done | Outline approved, 8 citations mapped |
| 3. DRAFT | In progress | 3 of 5 sections drafted |
| 4. REVIEW | Pending | — |
| 5. PUBLISH | Pending | — |
| 6. DISTRIBUTE | Pending | — |

**Next step:** Complete Section 4 (draft) and run anti-slop filter.
```

## Content Calendar View

When managing multiple pieces, track them:

```markdown
## Content Calendar

| Title | Pillar | Stage | Target Date | Notes |
|-------|--------|-------|-------------|-------|
| [Post 1] | practical-ai | DRAFT | Feb 10 | Waiting on one source |
| [Post 2] | leadership | RESEARCH | Feb 14 | Research pipeline ran |
| [Post 3] | education | PLAN | Feb 17 | Outline in progress |
```
