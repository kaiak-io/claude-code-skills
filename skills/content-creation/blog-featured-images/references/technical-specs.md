# Technical Specifications

Detailed technical specs for KAIAK blog featured images.

## Font Stack

| Weight | Use | Size Range |
|--------|-----|------------|
| Poppins Bold | Headers, stats, primary labels | 18-72pt |
| Poppins Medium | Secondary labels, annotations | 11-16pt |
| Poppins Regular | Small text, sublabels, watermark | 10-14pt |

- All text pure black (`#000000`)
- Secondary text/units (`/day`, `/week`): Slate (`#475569`)
- Stats and focal numbers: 48-72pt bold for visual punch
- All text readable at 400px wide (social thumbnail size)

## Color Palette

| Name | Hex | Usage |
|------|-----|-------|
| Black | `#000000` | All text |
| Slate | `#475569` | Watermark, secondary units |
| Cream | `#FAF0E6` | Background |
| Teal | `#0891B2` | Practical AI, solutions, calm states |
| Amber | `#D97706` | Systems Thinking, transitions |
| Emerald | `#059669` | Leadership, positive outcomes |
| Orange | `#EA580C` | AI in Education, stress, problems |
| Violet | `#7C3AED` | No-Admin Life, transformation arrows |
| Light Gray | `#DCD7D0` | Inactive bar backgrounds, subtle outlines |

### Fill Opacity

- Shape fills: brand color mixed with cream at 20-35% opacity for backgrounds
- Full saturation for outlines, dots, and primary shape elements
- No gradients — solid fills only

## Shape Rules

- Rounded rectangles: radius 14-16px
- Outlines: 1-2px, colored
- Fills: brand color at 20-35% opacity for background shapes
- Pill labels: radius = height/2, soft colored fill, black text
- Dots/circles: 5-6px radius, solid brand color fill

## Canvas Layout

**Dimensions:** 1200 x 630px
**Generation method:** Claude Desktop image generation or Python + Pillow with Poppins font family

```
+--------------------------------------------------+
|  48px padding                                    |
|  +--------------------------------------------+  |
|  |                                            |  |
|  |  Visual content fills the inner area       |  |
|  |  Stats right-aligned on header lines       |  |
|  |  No titles, no pillar tags                 |  |
|  |                                            |  |
|  +--------------------------------------------+  |
|                               kaiak.io  (slate)  |
+--------------------------------------------------+
```

- Padding: 48px on all sides
- kaiak.io watermark: bottom-right, Poppins Regular, Slate (`#475569`)
- Composition: scroll-stopping, vibrant enough to catch attention in a feed

## Output & Integration

### File Naming

Save generated images to: `public/images/posts/[slug].png`

The slug matches the MDX filename (e.g., `trained-50-teachers-on-ai.mdx` uses `trained-50-teachers-on-ai.png`).

### MDX Frontmatter

Add to each post's MDX frontmatter:

```yaml
image: "/images/posts/[slug].png"
imageAlt: "[descriptive alt text]"
```

### Alt Text Guidelines

Write alt text that describes the visual metaphor, not just "featured image." Include key data points shown in the graphic.

**Examples:**

```yaml
imageAlt: "Concentric ripple diagram showing AI training adoption radiating from one trainer to 50+ teachers, with 80% using AI regularly after 6 months"

imageAlt: "Before and after timeline comparison showing email reduction from 2-3 hours always-on to 30 minutes across three focused windows"

imageAlt: "Battery comparison showing 200+ micro-decisions depleting capacity by midmorning versus 10 systematic decisions preserving full capacity all day"
```
