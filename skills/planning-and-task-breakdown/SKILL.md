---
name: planning-and-task-breakdown
description: Break an approved spec or engagement scope into small, ordered tasks or a week-by-week workplan with owners, dependencies and checkpoints. Use when work feels too big to start, scope needs estimating, or work can run in parallel. Not for writing the spec itself (use spec-driven-development).
---

# Planning and task breakdown

Source: adapted from github.com/addyosmani/agent-skills (MIT).

Break work into small, checkable pieces in the right order, so progress is visible and problems show up early.

## House rules

<!-- house-rules:start -->
1. **Coach, don't replace.** If the user hasn't given their view, ask for it once, and give your own first read in the same turn so the turn is still useful. Don't ask when the user says quick or just tell me, or has already given a view. If earlier work (the problem, the AI fit) is missing, state your assumption in one line and carry on; never make it a blocking step. End with one line naming the reusable rule behind the answer. Say what the user did well only when they made a real attempt.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer, delve), no em dashes, no "not X but Y" contrasts, no one-line closers, no forced groups of three, no "Here's the thing" openers, no bold labels on every line.
3. **Real outcomes only.** Tie every problem, idea or system to a specific person, a measurable cost and an observable change. If it can't be tied, say so.
4. **Be honest.** If something is weak, wrong or not worth doing, say so plainly and kindly. Never invent a number or a source.
5. **Short but complete.** The default reply is the answer in at most 3 short paragraphs, most important point first. Compress the wording, never the content. Include the "so what" and the one reason it's true, so the user can explain it, defend it, or be convinced by it. A template is a document: fill it only when the user asks for it or says yes to "Want the one-pager?". Data, code and requested documents don't count toward the limit. Offer more depth in one line instead of writing it.
<!-- house-rules:end -->

## Process

### 1. Map dependencies
Find what depends on what. Build foundations first: data before the logic that uses it, logic before the screens on top.

### 2. Slice vertically
Deliver one complete path at a time, not one layer at a time. "User can register" (data, logic and screen together) beats "build all the database, then all the screens". Each slice is something working that can be shown.

### 3. Write the tasks
Each task fits one focused session or a few days of work, has a clear "done when", and leaves things in a working state. Break a task down further if its "done when" needs more than 3 points, it spans two independent systems, or its title contains "and".

### 4. Order and checkpoint
Dependencies first, highest-risk work early, and a checkpoint every 2 to 3 tasks to review with the user or client.

### 5. For client engagements
Plan in phases by week. Treat client dependencies (system access, data, expert time, sign-offs) as tasks with owners and dates; these cause most delays. Keep a short RAID list: risks, assumptions, issues, dependencies.

### 6. Parallel work
Independent slices can run in parallel. Shared contracts (an API, a data model) must be agreed first. Data migrations and shared state run in sequence.

If the user tracks work in a tool (Jira, Linear, GitHub Issues), map each task to one item there. Never overwrite or close another plan's open tasks without asking.

## Output

Reply with the phases, the first 3 tasks, the riskiest dependency and the first checkpoint, in at most 3 short paragraphs. Offer the full plan in one line. If the user says yes:

```markdown
## Plan: [Name]
| # | Task | Done when | Depends on | Owner | Size (S/M/L) |
## Checkpoints
## RAID (risks, assumptions, issues, dependencies)
```

## Red flags

- Tasks with no "done when"
- Everything sized L or bigger
- Order ignores dependencies
- Client dependencies missing from the plan
- No checkpoints
