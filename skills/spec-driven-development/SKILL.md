---
name: "spec-driven-development"
description: "Write a spec or PRD before building. Use when starting a feature or project, when requirements are vague, or when scoping a V1 or a change to something shipped."
---

# Spec-Driven Development

Source: github.com/addyosmani/agent-skills (MIT), adapted to work on its own in chat and for product work as well as code.

Write a structured spec before anything gets built. The spec is the shared source of truth: what we're building, why, and how we'll know it's done.

**Skip it for:** one-line fixes, typos, or changes whose requirements are unambiguous and self-contained.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view before giving yours. Explain why each step matters, so the user can do it alone next time. End with one line on what they did well and one thing to practise.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer), no em dashes, no "not X but Y" contrasts, no bold labels on every line, no closing summaries that repeat the point.
3. **Real outcomes only.** Every spec must tie to a specific person, a measurable cost and an observable change. If it can't, say so.
4. **Be honest.** If a requirement is weak, vague or not worth building, say it plainly and kindly.
5. **Short but complete.** Any summary or answer is at most 2 to 3 short paragraphs, never an essay. Most important point first. Leave nothing important out: compress the wording, not the content. Explain like you would to a smart person outside the field, with the "so what" and the one reason it's true, so the user can explain it, defend it, or be convinced by it. Spec sections stay to one or two lines each. If more depth exists, offer it in one line ("Want the detail on X?") instead of writing it.

## The gated workflow

SPECIFY -> PLAN -> TASKS -> BUILD. The human reviews and approves each phase before the next starts.

### Phase 0: Scope check (only when needed)

Most requests are one capability; skip straight to Specify. Decompose first only when one request bundles several independently testable capabilities (separate users or data, acceptance criteria that cluster into groups that could ship separately).

Then propose a short capability map before writing any spec:

```markdown
# Capability Map: [Initiative]

| Module id | Responsibility | Depends on |
|---|---|---|
| identity | Accounts, sessions, SSO | - |
| billing | Plans, invoices, payments | identity |

Build order: identity -> billing
```

Rules: stable kebab-case ids, dependencies point one way (two modules that need each other are one module), contracts live in the provider module's spec. The human approves the map, then each module gets its own spec in build order.

### Phase 1: Specify

1. **Surface assumptions first**, before writing spec content:
```
ASSUMPTIONS I'M MAKING:
1. ...
2. ...
-> Correct me now or I'll proceed with these.
```
Never silently fill in ambiguous requirements.

2. **Ask clarifying questions** until the objective, user, and definition of done are concrete.

3. **Reframe vague requirements as testable success criteria.**
```
REQUIREMENT: "Make the dashboard faster"
SUCCESS CRITERIA:
- Dashboard loads in < 2.5s on 4G
- Initial data load < 500ms
-> Are these the right targets?
```

4. **Write the spec** with this template. For product or business work, the PRD sections matter most; include the technical sections only when software is being built.

```markdown
# Spec: [Name] - V[N]

## Objective
[What and why. Who the user is. User stories or acceptance criteria.]

## Success Criteria
[Specific, testable conditions and metrics]

## Scope
[What's in this version]

## Out of Scope (Deferred)
[The V2 backlog: one line each, what and why deferred]

## Boundaries
- Always: [...]
- Ask first: [...]
- Never: [...]

## Technical (software only)
[Tech stack with versions; build/test/lint commands; project structure; one code snippet showing style; testing strategy]

## Risks and Dependencies
[...]

## Open Questions
[Anything needing human input]
```

5. **Stop after the spec.** Summarize it, list open questions, ask for approval, and end the turn. Do not start planning or building in the same turn.

### Phase 2: Plan

With the approved spec: identify major components and dependencies, set the build order, note risks and mitigations, mark what can run in parallel, and define checkpoints. Use the planning-and-task-breakdown skill for the detail. The human approves the plan.

### Phase 3: Tasks

Break the plan into tasks that each fit one focused session, with acceptance criteria and a verification step, ordered by dependency:

```markdown
- [ ] Task: [Description]
  - Acceptance: [What must be true when done]
  - Verify: [How to confirm]
```

### Phase 4: Build

One task at a time, checking each against its acceptance criteria.

## Keeping the spec alive

Update the spec first when decisions or scope change, then build. Keep it versioned alongside the work.

## V1 scoping and follow-up changes

- Label every spec with its version. New ideas mid-build go to Out of Scope (Deferred); re-scoping happens between versions, not during one.
- A change to something already shipped gets its own small delta spec, not an edit of the original:

```markdown
# Spec Delta: [Change]
Status: proposed
## Objective
## Current Behavior
## New Behavior
## Success Criteria (including what must NOT change)
## Boundaries (only the deltas)
```

After it ships, fold the outcome into the original spec and set the delta's status to implemented.

## Common rationalizations

| Rationalization | Reality |
|---|---|
| "This is simple, no spec needed" | Simple work needs a short spec, not none. Two lines of acceptance criteria is fine. |
| "I'll write it after" | That's documentation. The value is forcing clarity before work starts. |
| "Requirements will change anyway" | That's why the spec is living. An outdated spec beats no spec. |
| "The user knows what they want" | Clear requests still hide assumptions. The spec surfaces them. |
| "Good idea, I'll fold it into this version" | That's how V1 slips. Park it under Deferred. |

## Red flags

- Building with no written requirements
- Features appearing that aren't in the spec
- Writing the spec and starting the plan in the same turn
- One spec covering several independently testable capabilities
- Editing a shipped spec instead of writing a delta

## Verification

- [ ] Assumptions were surfaced and confirmed
- [ ] Success criteria are specific and testable
- [ ] Boundaries (Always / Ask first / Never) are defined
- [ ] Deferred ideas are captured, not silently dropped or included
- [ ] The human approved the spec in a later turn