# JSX Patterns Reference

Full code examples for JSX components in MDX content. Use these instead of markdown tables and unsupported MDX components.

## Hero Section Pattern

For posts with compelling statistics. Place immediately after frontmatter:

```jsx
<div style={{background: 'linear-gradient(135deg, #fef3c7 0%, #fde68a 100%)', borderRadius: '12px', padding: '24px', marginBottom: '32px', border: '1px solid #f59e0b'}}>

**The hook statement.** [Stat one](https://source-url.com) with context—[stat two](https://source-url.com) with more context, and [stat three](https://source-url.com) drives it home.

</div>
```

**Rules:**
- 2-4 key statistics, all linked to sources
- One bold opening statement
- Yellow/amber gradient (the "warning/attention" color)
- Stats should create tension or urgency
- Don't repeat the same stats in the hero and the auto-rendered frontmatter description

## Two-Column Comparison Grid

Use for before/after, do/don't, pros/cons. Replaces markdown tables for these use cases:

```jsx
<div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px', margin: '2rem 0'}}>

<div style={{background: '#fef2f2', borderRadius: '8px', padding: '20px', borderLeft: '4px solid #ef4444'}}>

**Before/Problem/Don't**

Content here. Can include bullets:
- Point one
- Point two

</div>

<div style={{background: '#f0fdf4', borderRadius: '8px', padding: '20px', borderLeft: '4px solid #22c55e'}}>

**After/Solution/Do**

Content here. Can include bullets:
- Point one
- Point two

</div>

</div>
```

## Multi-Card Grid

For 3+ items (categories, steps, options):

```jsx
<div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '16px', margin: '2rem 0'}}>

<div style={{background: '#f0fdf4', borderRadius: '8px', padding: '20px', borderLeft: '4px solid #22c55e'}}>

**Card Title One**

Description or content here.

</div>

<div style={{background: '#f0fdf4', borderRadius: '8px', padding: '20px', borderLeft: '4px solid #22c55e'}}>

**Card Title Two**

Description or content here.

</div>

<div style={{background: '#f0fdf4', borderRadius: '8px', padding: '20px', borderLeft: '4px solid #22c55e'}}>

**Card Title Three**

Description or content here.

</div>

</div>
```

## Color Options

| Purpose | Background | Border | Emoji |
|---------|------------|--------|-------|
| Negative/Before/Problem | `#fef2f2` | `#ef4444` | (none) |
| Positive/After/Solution | `#f0fdf4` | `#22c55e` | (none) |
| Neutral/Category | `#f3f4f6` | `#6b7280` | — |
| Warning/Caution | `#fef3c7` | `#f59e0b` | (none) |
| Info/Highlight | `#eff6ff` | `#3b82f6` | (none) |

## JSX Tables

Markdown tables may not render properly in MDX. Use JSX inline styles:

```jsx
<table style={{width: '100%', borderCollapse: 'collapse', marginBottom: '24px'}}>
  <thead>
    <tr style={{backgroundColor: '#f8f9fa'}}>
      <th style={{border: '1px solid #ddd', padding: '12px', textAlign: 'left'}}>Header 1</th>
      <th style={{border: '1px solid #ddd', padding: '12px', textAlign: 'left'}}>Header 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style={{border: '1px solid #ddd', padding: '12px'}}>Cell 1</td>
      <td style={{border: '1px solid #ddd', padding: '12px'}}>Cell 2</td>
    </tr>
  </tbody>
</table>
```

## Callout Component

The only MDX component confirmed to work:

```jsx
<Callout type="tip" title="Your Title Here">
Content here. Keep to 2-3 sentences max.
</Callout>
```

**Types:** `tip` (green), `warning` (yellow), `story` (blue)

## Visual Spec Comments

Use JSX comments for designer/production instructions (won't render):

```jsx
{/* [VISUAL SPEC: Bar chart comparing AI adoption rates (2024) vs (2025).
Data points: Students=66%→92%, Teachers=41%→53%.
Caption: "The gap between student and teacher adoption is widening."] */}
```

## Internal Post Links

Use your site's blog path prefix for internal post links:

```markdown
See the [post title](/blog/post-slug) for more.
```
