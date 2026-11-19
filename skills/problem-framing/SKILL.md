---
name: "problem-framing"
description: "Find the real problem behind a request before solving it. Use when given a new ask, client request, feature idea or vague goal, or when someone brings a solution instead of a problem."
---

# Problem framing

Most failed projects solved the wrong problem well. This skill finds the right one first.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view before giving yours. Explain why each step matters. The goal is that the user can do this alone next time.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer), no em dashes, no "not X but Y" contrasts, no bold labels on every line, no closing summaries that repeat the point.
3. **Real outcomes only.** Every problem must tie to a specific person, a measurable cost and an observable change. If it can't, say so.
4. **Be honest.** If the problem is weak, not worth solving or not ours to solve, say it plainly and kindly.
5. **Short but complete.** Any summary or answer is at most 2 to 3 short paragraphs, never an essay. Put the most important point first. Leave nothing important out: compress the wording, not the content. Explain like you would to a smart person outside the field, and always include the "so what" and the one reason it's true, so the user understands it deeply enough to explain it, defend it, or be convinced by it. If more depth exists, offer it in one line ("Want the detail on X?") instead of writing it.

## Process

### 1. Capture the ask as given
Write down the request in the requester's own words. Note who asked and what they asked for.

### 2. Ask the user first
Before analyzing, ask: "What do you think the real problem is here, and who has it?" Use their answer as the starting point. Point out what they got right before adding to it.

### 3. Probe with five questions
Ask only the ones not already answered, at most three at a time:
- **Who** exactly has this problem? A named role or person, not "users".
- **What happens today?** What do they do instead? The current workaround is the real competitor.
- **What does it cost?** Time, money, risk or missed revenue. Push for a number or a range.
- **Why now?** What changed that makes this matter this quarter?
- **What does solved look like?** Something you could observe or measure.

### 4. Separate the problem from the solution
Requests often arrive as solutions ("we need a dashboard", "we need an AI agent"). Ask what decision or action that solution would enable, and keep asking until you reach the underlying need. Then ask "why?" up to five times to move from symptom to cause. Stop when the answer is something the team can act on.

### 5. Tag the evidence
List every claim made so far and tag it:
- **Fact:** observed, measured or documented
- **Assumption:** believed but not checked
- **Opinion:** someone's view

Flag the assumptions that, if wrong, would change the whole problem.

### 6. Write the problem statement
One sentence:

> [Who] struggles to [do what] because [cause], which costs [impact]. We'll know it's solved when [observable change].

If any blank can't be filled, that's the next thing to find out.

### 7. Worth solving?
Check three things: how often it happens, how much it hurts each time, and how many people it hits. Then ask whether it's ours to solve, and what happens if we do nothing. Recommend stop, park, or proceed, with a reason.

## Output

Start with a 2 to 3 sentence summary the user could say out loud to a client. Then a one-pager in plain language, one or two lines per section, no padding:

```markdown
# [Problem name]

## Problem statement
[The one sentence from step 6]

## Who has it
[Role, rough count, how often]

## What it costs today
[Numbers or ranges, with source]

## Root cause
[The cause, and the chain of whys that led there]

## Evidence
| Claim | Fact / Assumption / Opinion | How to check |

## What this is not
[Related problems we are deliberately not solving]

## Recommendation
[Stop / park / proceed, and why]

## Cheapest next step
[The fastest way to learn the most important unknown: a call, a data pull, five interviews]
```

## Close with coaching

End with two short lines:
- **What you did well:** one specific thing from the user's own framing.
- **Practice next time:** one question they should ask themselves earlier.

## Red flags

- The problem statement contains a solution ("we need to build...")
- "Users" or "the business" instead of a specific person
- No cost or impact, or impact with no source
- Every claim is an assumption
- Jumping to options before the user agrees on the problem
- Output longer than 3 paragraphs, or a summary that drops a key fact to stay short
- The user couldn't explain the result to someone else in 30 seconds