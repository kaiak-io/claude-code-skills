# Source Evaluation & Verification Workflow

Detailed reference for verifying sources before publication.

## Link Verification Process

For every source in the draft:

1. **Click every link** — Confirm it loads and points to the expected content
2. **Check publication dates** — Ensure sources are current (prefer last 12-18 months for fast-moving topics like AI)
3. **Trace stats to primary sources** — If a stat is cited from a secondary source (news article, blog), find the original study
4. **Archive fragile links** — Consider web.archive.org for sources that may disappear

## Handling Unverifiable Statistics

If a commonly-cited stat lacks an authoritative source:

1. **Find an alternative** — Search for similar data from reputable sources
2. **Soften the language** — "approximately" or "around" instead of exact figures
3. **Remove if necessary** — Better to omit than cite unreliable data
4. **Document the gap** — Note for future research

## Source Quality Red Flags

Avoid sources that are:

- **Industry vendors citing their own surveys** (e.g., security camera company publishing education stats)
- **Aggregator sites without primary citations** (they often distort or fabricate numbers)
- **Outdated** (pre-2023 for fast-moving topics like AI)
- **Paywalled with no way to verify claims** (if you can't read it, you can't cite it accurately)
- **Circular citations** (Source A cites Source B which cites Source A)

## The Hallucination Problem

AI frequently invents links, misattributes quotes, and cites sources that don't exist. Every reference needs manual verification.

**Before adding any AI-suggested link or citation:**
1. Click the link — does it actually load?
2. Find the claim — does the source actually say what you're attributing to it?
3. Check the date — is this still current/relevant?
4. Verify the author — is this person real and did they actually say this?

If you can't verify it, don't use it. A missing citation is better than a fake one.

## Citation Cross-Check

Before finalizing any piece:

- [ ] Every inline citation has a working URL
- [ ] Stats match what the source actually says (not paraphrased loosely)
- [ ] No stats are attributed to wrong sources
- [ ] Reference list at end matches inline citations exactly
- [ ] No duplicate citations with different URLs
- [ ] Quoted text matches the original word-for-word

## Finding Evidence

Prioritize in this order:

1. **Your own experience** — Most valuable, can't be replicated
2. **Named case studies** — "Airbnb does X" beats "companies do X"
3. **Specific data** — "43% improvement" beats "significant improvement"
4. **Expert quotes** — Named person > "experts say"

## Research Output Template

When conducting research for a piece, organize findings:

```markdown
## Research: [Topic]

### Key Data Points
- **[Stat]**: [Source, Year] — Verified / Needs check
- **[Stat]**: [Source, Year] — Verified / Needs check

### Usable Examples
- **[Company/Person]**: [What they did] — [Result]

### Expert Perspective
- "[Quote]" — [Name, Role] — Quote verified at [link]

### Gaps Still Needed
- [ ] [Specific missing piece]

### Links to Verify Before Publish
- [ ] [URL 1]
- [ ] [URL 2]
```
