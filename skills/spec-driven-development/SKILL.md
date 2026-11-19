---
name: spec-driven-development
description: Write a PRD or spec once a direction is chosen, covering objective, success criteria, scope, out of scope, risks and AI behaviour. Use before building a feature or project, or when scoping a V1 or a change to something shipped. Not for exploring ideas (use idea-refine) or breaking work into tasks (use planning-and-task-breakdown).
---

# Spec-driven development

Source: adapted from github.com/addyosmani/agent-skills (MIT).

Write the spec before anything gets built. It is the shared source of truth: what we're building, why, and how we'll know it's done. Skip it for small, unambiguous changes.

## House rules

<!-- house-rules:start -->
1. **Coach, don't replace.** If the user hasn't given their view, ask for it once, and give your own first read in the same turn so the turn is still useful. Don't ask when the user says quick or just tell me, or has already given a view. If earlier work (the problem, the AI fit) is missing, state your assumption in one line and carry on; never make it a blocking step. End with one line naming the reusable rule behind the answer. Say what the user did well only when they made a real attempt.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer, delve), no em dashes, no "not X but Y" contrasts, no one-line closers, no forced groups of three, no "Here's the thing" openers, no bold labels on every line.
3. **Real outcomes only.** Tie every problem, idea or system to a specific person, a measurable cost and an observable change. If it can't be tied, say so.
4. **Be honest.** If something is weak, wrong or not worth doing, say so plainly and kindly. Never invent a number or a source.
5. **Short but complete.** The default reply is the answer in at most 3 short paragraphs, most important point first. Compress the wording, never the content. Include the "so what" and the one reason it's true, so the user can explain it, defend it, or be convinced by it. A template is a document: fill it only when the user asks for it or says yes to "Want the one-pager?". Data, code and requested documents don't count toward the limit. Offer more depth in one line instead of writing it.
<!-- house-rules:end -->

## Process

### 1. Check scope
If one request bundles several capabilities that could ship and be tested separately (say identity, billing and reporting), propose a short list of modules with their dependencies and build order first, and spec each module separately once it's agreed.

### 2. Surface assumptions
List 3 to 5 assumptions and ask the user to correct them before writing the spec. Never fill an ambiguous requirement silently.

### 3. Turn vague requirements into testable criteria
"Make the dashboard faster" becomes "loads in under 2.5 seconds on a typical connection". Check the targets with the user.

### 4. Write the spec

```markdown
# Spec: [Name] - V[N]
## Objective (what, why, for whom)
## Success criteria (specific, testable)
## Scope
## Out of scope (deferred, one line each with the reason)
## Constraints (if software: systems, data, integrations, security, performance)
## AI behaviour (if AI: ship bar from eval-design, behaviour when the model is unsure, human review point, data sources and permissions)
## Risks and dependencies
## Open questions
```

Keep each section to one or two lines where possible.

### 5. Stop for approval
Summarize the spec and its open questions, and ask for approval. Planning starts only after the user approves.

## Keeping it alive

Update the spec first when decisions or scope change. New ideas that arrive mid-build go under Out of scope; re-scoping happens between versions, not during one. A change to something already shipped gets a short delta spec (objective, current behaviour, new behaviour, success criteria, what must not change) rather than an edit of the original. Fold it back into the original once it ships.

## Output

Reply with the objective, the 2 to 3 success criteria, the biggest open question and the assumptions to confirm, in at most 3 short paragraphs. Write the full spec when the user asks or confirms.

## Red flags

- Building with no written success criteria
- Features appearing that aren't in the spec
- Mid-build ideas added to the current version
- An AI feature with no ship bar or no "unsure" behaviour
- Planning started before the spec was approved
