---
name: "planning-and-task-breakdown"
description: "Break a spec or clear requirements into small, ordered tasks with acceptance criteria. Use when work feels too big to start, scope needs estimating, or work can run in parallel."
---

# Planning and Task Breakdown

Source: github.com/addyosmani/agent-skills (MIT), adapted to work on its own in chat.

Decompose work into small, verifiable tasks with explicit acceptance criteria. Each task should be small enough to do and check in one focused session.

**Skip it for:** single changes with obvious scope, or when the spec already has well-defined tasks.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view of the order and risks before giving yours. Explain why each step matters, so the user can do it alone next time. End with one line on what they did well and one thing to practise.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer), no em dashes, no "not X but Y" contrasts, no bold labels on every line, no closing summaries that repeat the point.
3. **Real outcomes only.** Every task must move toward an observable result for a real person. Cut tasks that don't.
4. **Be honest.** If the plan is too big, too risky or out of order, say it plainly and kindly.
5. **Short but complete.** Any summary or answer is at most 2 to 3 short paragraphs, never an essay. Most important point first. Leave nothing important out: compress the wording, not the content. Explain like you would to a smart person outside the field, with the "so what" and the one reason it's true, so the user can explain it, defend it, or be convinced by it. Task descriptions stay to one or two lines. If more depth exists, offer it in one line ("Want the detail on X?") instead of writing it.

## Process

### 1. Plan before doing

Read the spec or requirements and any existing material. Identify existing patterns, dependencies, risks, and unknowns. Do not start the work itself while planning; the output is a plan and a task list.

### 2. Map the dependency graph

Show what depends on what. Build order follows the graph bottom-up: foundations first.

```
Data model
  -> API / integration
       -> UI or process step
  -> Migration / seed data
```

### 3. Slice vertically

Deliver one complete path at a time, not one layer at a time.

Bad (horizontal): all the database, then all the API, then all the UI, then connect.
Good (vertical): user can register (data + API + UI), then user can log in, then user can create an item.

Each slice delivers something working and testable.

### 4. Write each task

```markdown
## Task [N]: [Short title]

**Description:** One paragraph on what this accomplishes.

**Acceptance criteria:**
- [ ] [Specific, testable condition]
- [ ] [Specific, testable condition]

**Verification:** [How to confirm: test, build, manual check, stakeholder sign-off]

**Dependencies:** [Task numbers, or None]

**Owner:** [If known]

**Size:** [XS / S / M / L]
```

### 5. Order and checkpoint

1. Dependencies satisfied first
2. Each task leaves things in a working state
3. A checkpoint after every 2-3 tasks
4. Highest-risk tasks early (fail fast)

```markdown
## Checkpoint: After Tasks 1-3
- [ ] Everything built so far works end to end
- [ ] Review with the human before continuing
```

## Sizing

| Size | Scope | Example |
|---|---|---|
| XS | One small change | Add a validation rule |
| S | One component or step | Add one API endpoint |
| M | One feature slice | Registration flow |
| L | Multi-part feature | Search with filters and paging |
| XL | Too large: break it down | - |

Break a task down further when it needs more than one focused session, its acceptance criteria won't fit in 3 bullets, it spans two independent systems, or its title contains "and".

## Plan template

```markdown
# Plan: [Name]

Source spec: [link or name, if any]

## Overview
[One paragraph]

## Key Decisions
- [Decision and rationale]

## Tasks
### Phase 1: Foundation
- [ ] Task 1 ...
### Checkpoint: Foundation
### Phase 2: Core
- [ ] Task 3 ...
### Checkpoint: Core
### Phase 3: Polish
- [ ] Task 5 ...
### Checkpoint: Complete

## Risks and Mitigations
| Risk | Impact | Mitigation |
|---|---|---|

## Open Questions
```

If the person tracks work in a tool (Jira, Linear, GitHub Issues), map each task to one item there and keep the plan's task list as an index of those items. Never overwrite or close another plan's open tasks without asking.

## Parallel work

- Safe to parallelize: independent slices, tests for finished work, documentation
- Must be sequential: data migrations, shared state, dependency chains
- Needs coordination: anything sharing a contract (define the contract first)

## Common rationalizations

| Rationalization | Reality |
|---|---|
| "I'll figure it out as I go" | That's how rework happens. 10 minutes of planning saves hours. |
| "The tasks are obvious" | Write them anyway; it surfaces hidden dependencies. |
| "I can hold it in my head" | Written plans survive across sessions and people. |

## Red flags

- Tasks like "implement the feature" with no acceptance criteria
- No verification steps or checkpoints
- Everything sized L or XL
- Order ignores dependencies

## Verification

- [ ] Every task has acceptance criteria and a verification step
- [ ] Dependencies are ordered correctly
- [ ] Checkpoints exist between phases
- [ ] The human approved the plan