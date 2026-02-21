---
name: blog-featured-images
description: Generates branded featured images for blog posts in the KAIAK "Warm
  Editorial" style. Covers brand colors (5-pillar palette), typography (Poppins),
  illustration rules (flat geometric, no 3D), color logic (warm=problems,
  cool=solutions), canvas specs (1200x630px), and visual concept design. Use when
  creating featured images, designing Open Graph graphics, planning visual concepts
  for blog posts, or reviewing image designs against brand guidelines. Includes the
  master prompt for Claude Desktop image generation.
---

# Blog Featured Images

Generates branded featured images for KAIAK blog posts. Each image is a visual metaphor for the article's core concept — flat, geometric, editorial — using the 5-pillar color system on a warm cream canvas.

## Core Philosophy

1. **Visual metaphors over literal data.** Every image tells the article's story through conceptual imagery — concentric ripples, battery drains, timeline comparisons — not bar charts or generic illustrations.
2. **Color carries meaning.** Warm colors (orange, amber) signal stress, problems, and before-states. Cool colors (teal, emerald, violet) signal calm, solutions, and after-states. Every graphic has a built-in narrative.
3. **Editorial, not decorative.** Images should look like they belong in a premium newsletter (think Lenny's Newsletter), not a stock photo library. Flat, geometric, readable at thumbnail size, zero clutter.

## Brand Aesthetic

**"Warm Editorial"** — clean, calm, confident. A well-designed infographic from a curated editorial publication. Flat, warm, generous whitespace. Works on both light and dark mode pages.

**Where these images appear:**
- Open Graph meta tags — social sharing previews (LinkedIn, Twitter, Facebook)
- RSS feed — image per post for Flipboard
- Blog post cards — featured image on the listing page
- LinkedIn newsletter — header images for adapted posts

## Color System

### 5-Pillar Palette

| Pillar | Label | Hex | Color | Role |
|--------|-------|-----|-------|------|
| practical-ai | Practical AI | `#0891B2` | Teal | Cool / solutions |
| systems-thinking | Systems Thinking | `#D97706` | Amber | Warm / stress |
| leadership | Leadership | `#059669` | Emerald | Cool / solutions |
| education | AI in Education | `#EA580C` | Orange | Warm / stress |
| no-admin-life | The No-Admin Life | `#7C3AED` | Violet | Cool / solutions |

### Color Logic

- **Warm colors** (orange, amber) = stress, before states, resistance, problems
- **Cool colors** (teal, emerald, violet) = calm, after states, systems, solutions
- All 5 colors at full saturation — no mixing down
- NO rose, pink, or red tones
- NO gradients

### Text Colors

- **All text:** pure black `#000000` — colors are for shapes and fills only
- **Secondary text** (units, sublabels, watermark): slate `#475569`
- **Background:** warm cream `#FAF0E6`

## Typography

- **Primary:** Poppins Bold — headers, stats, primary labels (48-72pt for stats)
- **Secondary:** Poppins Medium — labels, annotations
- **Small text:** Poppins Regular — sublabels, watermark
- All text pure black for maximum readability
- All text must be readable at 400px wide (social thumbnail size)

## Illustration Style

- **FLAT.** No 3D, no isometric, no shadows, no glossy surfaces
- Clean geometric shapes with rounded corners (radius 14-16px)
- Thin outlines (1-2px) on shapes, pixel-perfect
- Pill-shaped labels with soft colored fills and black text
- Bold, vibrant colors at full saturation — must pop in RSS feeds and carousels
- Visual metaphors over literal data visualization
- Thin horizontal rules or lines for structure
- Think "editorial infographic" not "decorative illustration"

## What NOT to Do

- No 3D, isometric, glassmorphism, shadows, or glow effects
- No gradients, lens flares, or particle effects
- No photographic elements or realistic people/faces
- No generic AI imagery (robot heads, neural network blobs, glowing brains)
- No stock illustration style, clip art, or corporate Memphis
- No hand-drawn or sketchy effects
- No dark backgrounds
- No busy compositions — if in doubt, remove elements
- No rose/pink/red colors
- No colored text — all text must be black
- No thin/light fonts (Cabin Sketch, Comic Neue, DejaVu Sans Mono are too lightweight)
- No blog post titles in the graphic (the CMS displays these)
- No pillar pills or category tags in the graphic (the CMS displays these)
- No fake data or statistics not from the actual article
- No personal/non-leadership decisions ("what to wear", "what to eat")

## Canvas & Layout

**Dimensions:** 1200 x 630 px (Open Graph standard)

```
+--------------------------------------------------+
|                                                  |
|  [VISUAL CONTENT — visual metaphor, before/after,|
|   battery comparison, concentric ripples, timeline|
|   comparison, etc. Full canvas with generous      |
|   padding. No title, no pillar tag.]             |
|                                                  |
|                             kaiak.io             |
|                             (slate, bottom-right)|
+--------------------------------------------------+
```

- Visual content occupies the full canvas
- Padding: at least 48px on all sides
- kaiak.io watermark: bottom-right, subtle, slate color
- Stats right-aligned on header lines, not overlapping visual elements

## Master Prompt

Use this prompt in Claude Desktop with reference images attached. Request images in batches of 3-5 using the Per-Post Request Format below.

```
You are creating featured editorial graphics for KAIAK (kaiak.io), a blog about AI in education, school leadership, and systems thinking written for school leaders.

I have attached reference images showing the visual style I want. Study them carefully. Here are the specific rules:

AESTHETIC: "Warm Editorial" — clean, calm, confident. Think: a well-designed infographic from a premium newsletter (Lenny's Newsletter is a good reference). Flat, warm, generous whitespace, zero clutter. The image should feel like it belongs in a curated editorial publication, not a tech blog.

CANVAS: 1200 x 630 px

BACKGROUND: Warm cream (#FAF0E6). Solid, clean, no texture or noise. This must look natural on a white/light webpage and read as a clean card on a dark background.

COLOR RULES:
- Text: Pure black (#000000) for ALL text — headers, stats, labels, annotations. No colored text.
- Secondary text (units, sublabels): Slate (#475569)
- Multi-color brand palette for shapes and fills — use the 5 pillar colors strategically:
  * Teal #0891B2 (Practical AI)
  * Amber #D97706 (Systems Thinking)
  * Emerald #059669 (Leadership)
  * Orange #EA580C (AI in Education)
  * Violet #7C3AED (No-Admin Life)
- Color logic: warm colors (orange, amber) = stress/before/resistance/problems; cool colors (teal, emerald, violet) = calm/after/systems/solutions
- All 5 pillar colors deployed at full saturation — no mixing down
- NO rose, pink, or red tones
- NO gradients

TYPOGRAPHY:
- All text in Poppins Bold (geometric sans-serif, heavy weight)
- Poppins Medium for secondary labels
- Poppins Regular for small annotations
- NO titles in the graphic — the blog post title is NOT in the image
- NO pillar pills/tags — the pillar label is NOT in the image
- All text pure black for maximum readability
- Stats/numbers: large and bold (48-72pt) for visual punch
- "kaiak.io" watermark: Slate (#475569) at bottom-right corner, subtle
- All text must be readable at 400px wide (social thumbnail size)
- CRITICAL: No text may overlap with any visual element. Stats should be right-aligned on header lines or placed clearly outside shapes.

ILLUSTRATION STYLE:
- FLAT. No 3D, no isometric, no shadows, no glossy surfaces.
- Clean geometric shapes — pixel-perfect, no hand-drawn or sketchy effects
- Thin outlines (1-2px) on shapes
- Rounded corners (radius 14-16px) on rectangles
- Pill-shaped labels with soft colored fills for annotations
- Visual metaphors over data visualization — use conceptual imagery that tells the post's story
- Think "editorial infographic" not "decorative illustration"

CONTENT RULES — STRICT:
- NO blog post titles in the graphic
- NO pillar pills or category tags
- NO fake data or statistics not from the article
- ALL text/stats must be verified against the actual article content
- The graphic should be a VISUAL METAPHOR for the article's core concept
- It should make someone curious about the article without giving everything away

LAYOUT:
- Visual content: occupies the full canvas with generous padding (48px all sides)
- "kaiak.io": bottom-right, subtle watermark
- The composition should be scroll-stopping — vibrant enough to catch attention in a feed
- Before/after comparisons, concentric ripples, battery metaphors, timeline comparisons — use the visual metaphor that best fits the article
- Stats right-aligned on header lines, not overlapping visual elements

WHAT NOT TO DO:
- No 3D, no isometric perspective, no glassmorphism
- No photographic elements, no realistic people or faces
- No generic AI imagery (robot heads, neural networks, glowing brains)
- No stock illustration style, no clip art, no corporate Memphis
- No gradients, no lens flares, no particle effects, no glow effects
- No dark backgrounds
- No busy compositions — if in doubt, remove elements
- No blog post titles in the image
- No pillar category pills/tags in the image
- No rose/pink/red colors
- No colored text — all text must be black
- No hand-drawn or sketchy effects
- No personal/non-leadership decisions (e.g., "what to wear", "what to eat") — keep all content leadership-focused
```

## Per-Post Request Format

```
Post: [exact title]
Pillar: [pillar name]
Visual: [describe the specific visual metaphor for this post]
```

**Example:**

```
Post: The Meeting Audit: How to Reclaim 5 Hours a Week
Pillar: Systems Thinking
Visual: A weekly calendar strip with meeting blocks in warm colors (orange/amber).
Some blocks crossed out. Freed hours shown as teal-highlighted open space.
A "5 hrs/week" stat right-aligned on the header line. Before/after feel —
busy warm tones transitioning to calm cool tones.
```

See [visual-concepts.md](references/visual-concepts.md) for pre-designed visual concepts for all 36+ posts.

## Design Principles

### What Works

- **Visual metaphors** — concentric ripples, battery drain, timeline comparisons tell the story better than bar charts
- **Multi-color brand palette** — all 5 pillar colors in each graphic creates vibrant, scroll-stopping images
- **Color logic** — warm for problems, cool for solutions gives every graphic a built-in narrative
- **Bold stats** (48-72pt) from the article as large focal numbers create visual anchors
- **Poppins Bold** — heavy geometric sans-serif with maximum readability at all sizes
- **All text in black** — no colored text, colors are for shapes and fills only
- **Thin 1px outlines** — clean, crisp, polished look
- **Pill-shaped labels** — soft colored fill with black text for annotations
- **Stats right-aligned on header lines** — keeps layout clean, avoids overlap
- **Thick borders and full saturation** — needed for visibility in small thumbnails

### What Doesn't Work

- **Rose/pink tones** — too many colors, removed from palette
- **Colored text** — reduces readability; all text must be pure black
- **Hand-drawn/sketchy effects** — wobble and imperfect lines look messy, not editorial
- **Thin/light fonts** — Cabin Sketch, Comic Neue too thin; DejaVu Sans Mono too lightweight
- **Monochrome accent** — single color per graphic is too subtle for feeds
- **Overlapping text on shapes** — stats must be positioned clear of visual elements
- **Personal/non-leadership decisions** — "what to wear", "what to eat" don't belong
- **Titles in graphics** — CMS shows these, creates redundancy
- **Pillar pills** — CMS shows category labels already
- **Fake data** — all numbers must come from the actual article

## Text Verification Checklist

Before finalizing any graphic, verify against the MDX source file:

1. All statistics match the article exactly
2. All quoted phrases are from the article
3. Decision/strategy labels match the article's terminology
4. Timeline references (hours, minutes, frequencies) are accurate
5. No text overlaps with any visual element

## Quick Commands

**Generate an image for a blog post:**
> Generate a featured image for this post: [paste title and pillar]. Design a visual concept that captures the core idea.

**Design visual concepts for multiple posts:**
> Here are 5 posts that need featured images: [list titles and pillars]. Design visual concepts for each following the brand guidelines.

**Review an image against brand guidelines:**
> Review this image against the KAIAK brand guidelines. Check colors, typography, layout, and style rules.

**Get the master prompt for Claude Desktop:**
> Give me the full master prompt for generating blog featured images in Claude Desktop.

**Add a completed image to a blog post:**
> I've generated an image for [post title]. What frontmatter do I need to add?
