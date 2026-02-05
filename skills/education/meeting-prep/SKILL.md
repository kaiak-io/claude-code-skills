---
name: meeting-prep
description: Generates meeting agendas, structures discussion topics, and transforms rough notes into formatted minutes with action items. Built for school leaders and educators who spend significant time in meetings. Use when preparing for meetings, processing meeting notes, or tracking follow-ups. Handles staff meetings, leadership team meetings, parent conferences, IEP meetings, board presentations, and PLCs.
---

# Meeting Prep & Notes

Turns meeting chaos into structured agendas, clear minutes, and tracked action items.

## Core Philosophy

1. **Meetings should produce decisions and actions**, not just discussion.
2. **Agendas prevent drift.** Every item has a purpose, a time box, and an expected outcome.
3. **Minutes are for people who weren't there.** Write them so someone absent knows exactly what was decided and what they need to do.

## Agenda Generation

### Input

Provide any combination of:
- Topics to discuss
- Decisions that need to be made
- Updates to share
- Problems to solve
- Time available

### Agenda Format

```markdown
# [Meeting Name] — [Date]

**Time:** [Start] - [End] ([Total] minutes)
**Location:** [Room / Video link]
**Attendees:** [Names or roles]
**Note-taker:** [Name]

---

## 1. [Topic] (X min) — [Purpose Tag]
**Lead:** [Name]
**Goal:** [What we need to walk out with — a decision, a plan, shared understanding]

Discussion prompts:
- [Specific question to address]
- [Specific question to address]

**Pre-read:** [Link to document, if applicable]

---

## 2. [Topic] (X min) — [Purpose Tag]
**Lead:** [Name]
**Goal:** [Expected outcome]

---

## Standing Items
- [ ] Review action items from last meeting (5 min)
- [ ] Upcoming dates and deadlines (3 min)
- [ ] Parking lot items (2 min)

---

**Total time allocated:** [X] of [Y] minutes
**Buffer:** [Y-X] minutes
```

### Purpose Tags

Every agenda item gets one tag:

| Tag | Meaning | How to Run It |
|-----|---------|---------------|
| **DECIDE** | A decision must be made in this meeting | Present options, discuss, vote or consensus |
| **DISCUSS** | Need input but decision comes later | Frame the question, hear perspectives, summarize |
| **INFORM** | One-way update, minimal discussion | Present, take questions, move on |
| **SOLVE** | Work through a problem together | Define problem, brainstorm, assign next steps |
| **REVIEW** | Evaluate work or progress | Present work, gather feedback, identify changes |

### Agenda Rules

1. **Time-box everything.** No agenda item without a time allocation.
2. **Decisions first.** Put DECIDE items early when energy is highest.
3. **INFORM items get 5 minutes max.** If it takes longer to present than read, send a document instead.
4. **Build in buffer.** Allocate 80% of available time. The other 20% handles overflow.
5. **Pre-reads for complex topics.** If an item needs background, send materials 24 hours before.

## Meeting Notes → Minutes

### Input

Provide any of:
- Rough handwritten-style notes
- Voice transcript
- Chat messages from the meeting
- Your memory of what happened

### Minutes Format

```markdown
# [Meeting Name] — Minutes — [Date]

**Attendees:** [Who was there]
**Absent:** [Who wasn't]
**Note-taker:** [Name]

---

## Decisions Made

1. **[Decision]** — [Brief context. Who decides. Any conditions or timeline.]
2. **[Decision]** — [Brief context.]

## Action Items

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| [Specific task] | [Name] | [Date] | Pending |
| [Specific task] | [Name] | [Date] | Pending |

## Discussion Summary

### [Topic 1]
[2-4 sentences capturing: what was discussed, key points raised, outcome or next step]

### [Topic 2]
[2-4 sentences]

## Parking Lot
- [Item deferred to future meeting]
- [Item that needs more research before deciding]

## Next Meeting
**Date:** [Date] | **Key agenda items:** [Preview of next meeting topics]
```

### Minutes Rules

1. **Decisions and action items come first.** These are what people actually need.
2. **Discussion summaries are summaries.** Not transcripts. Capture the conclusions, not every comment.
3. **Every action item has an owner and a due date.** "We should look into X" is not an action item. "Sarah will research X and report back by Friday" is.
4. **Name names.** "The team agreed" is useless for accountability. "Maria, James, and the principal agreed" is specific.
5. **Parking lot is real.** Items that got deferred should be visible so they don't disappear.

## Meeting-Specific Templates

### Staff Meeting
- Agenda weight: 60% INFORM, 20% DISCUSS, 20% DECIDE
- Typical duration: 45-60 minutes
- Include: celebrations/shout-outs (5 min), logistics updates, one substantive discussion topic

### Leadership Team
- Agenda weight: 40% DECIDE, 30% DISCUSS, 20% SOLVE, 10% INFORM
- Typical duration: 60-90 minutes
- Include: data review, strategic priorities check-in, resource allocation decisions

### Parent Conference
- Agenda weight: 30% INFORM, 40% DISCUSS, 30% DECIDE
- Typical duration: 20-30 minutes
- Structure: student strengths → areas of concern → data/evidence → plan → next steps
- Always end with: "Here's exactly what we're going to do, and here's when we'll check in again."

### PLC (Professional Learning Community)
- Agenda weight: 20% REVIEW, 40% SOLVE, 30% DISCUSS, 10% DECIDE
- Typical duration: 45-60 minutes
- Include: student work review, data analysis, instructional strategy discussion
- Focus question: "What are students learning, and how do we know?"

### Board Presentation
- Not a meeting to run — a meeting to prepare FOR
- Structure: context (2 min) → recommendation (1 min) → evidence (5 min) → Q&A (10 min)
- Prepare: one-page summary, 3-5 slides max, anticipated questions with answers

## Quick Commands

**Generate agenda from topics:**
```
I have a leadership team meeting on [date], 90 minutes. Topics: [list].
Generate a structured agenda with time boxes and purpose tags.
```

**Convert notes to minutes:**
```
Here are my rough notes from today's staff meeting: [paste].
Turn these into formatted minutes with decisions and action items pulled out.
```

**Prep for parent conference:**
```
I have a parent conference about [student]. Concerns: [list].
Strengths: [list]. Generate an agenda and talking points.
```

**Follow up on action items:**
```
Here are the minutes from our last meeting: [paste].
Which action items are due? Generate a follow-up email.
```
