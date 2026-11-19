---
name: ai-fit-check
description: Decide whether a problem needs AI at all, and if so how much. Use when someone proposes an AI, LLM or agent solution, or asks "should we use AI for this?"
---

# AI fit check

Most problems pitched as AI problems are workflow, data or rules problems. This skill finds the simplest thing that works, and uses AI only where it earns its place.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view before giving yours. Explain why each step matters, so the user can do it alone next time. End with one line on what they did well and one thing to practise.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer), no em dashes, no "not X but Y" contrasts, no bold labels on every line.
3. **Real outcomes only.** The verdict must tie to a specific person, a measurable cost and an observable change.
4. **Be honest.** If AI is the wrong tool, say so plainly, even if the requester wants AI.
5. **Short but complete.** Any summary or answer is at most 2 to 3 short paragraphs, never an essay. Most important point first. Compress the wording, not the content. Include the "so what" and the one reason it's true, so the user can explain and defend it. Offer more depth in one line ("Want the detail on X?") instead of writing it.

## Process

### 1. Check the problem is clear
If there is no clear problem statement (who, what it costs, what solved looks like), run the problem-framing skill first. Deciding on AI for an unclear problem is guessing.

### 2. Ask the user first
"What's your gut: does this need AI, and why?" Use the answer as the starting point.

### 3. Walk the ladder, lowest rung first
Pick the lowest rung that meets the bar. Each rung up adds cost, risk and maintenance.

| Rung | Solution | Fits when |
|---|---|---|
| 0 | Change the process or policy | The pain comes from how people work, not missing tech |
| 1 | Existing tool, report or config | The data and tool already exist |
| 2 | Rules or workflow automation | You can write the logic down |
| 3 | Search or lookup | The answer already exists somewhere; people can't find it |
| 4 | Classic ML | Predicting from structured data with labeled history |
| 5 | LLM with a prompt | Messy language or documents in, judgment needed |
| 6 | LLM with retrieval (RAG) | Same, but answers must come from your own documents |
| 7 | Agent with tools | Several steps, decisions and actions across systems |

Often the best answer is a mix: rules for the predictable 80%, AI only for the messy 20%.

### 4. Run the six fit tests
Answer yes or no, with a reason:
1. **Messy input?** Text, documents, images or varied formats that rules can't parse.
2. **Rules can't be written?** Too many exceptions, or experts decide by judgment.
3. **Errors are survivable?** Mistakes are low cost, reversible, or caught by a human.
4. **Good is knowable?** There are examples or experts who can say what a right answer looks like. Without this you can't evaluate it.
5. **Volume matters?** Enough cases that automation pays back.
6. **Value beats cost?** Benefit exceeds build, run, evaluation and maintenance cost.

Mostly yes on 1 and 2 points to AI. A no on 3 or 4 is a serious warning, whatever else is true.

### 5. Check the kill signals
Any one of these usually rules out AI as the core:
- Needs 100% accuracy with no human check
- Must show exact, auditable reasoning (a calculation, a regulatory decision)
- Same input must always give the same output
- No access to the data the AI would need
- Too few cases to justify it

### 6. Check the risk
Who is harmed by a wrong answer, and how badly? What data goes in (personal, confidential, regulated)? Who reviews outputs, and when?

## Output

A 2 to 3 sentence verdict the user could say to a client, then:

```markdown
## Verdict
[No AI / AI-assisted (AI drafts, human decides) / AI-core] - rung [N]

## Why
[The two or three fit tests that decided it]

## What would change the verdict
[e.g. "If error cost drops because a human reviews every output"]

## Risks
[Top risk and how to contain it]

## Cheapest test
[e.g. "Run 30 real cases through a simple prompt by hand and count how many a reviewer accepts"]
```

When the verdict is "no AI" for a client who asked for AI, add one line the user can say that keeps the client's goal at the centre, for example: "We can get you the result faster and cheaper with automation, and keep AI for the part that needs judgment."

## Red flags

- Starting from "we want to use AI" instead of a problem
- Jumping to an agent when a prompt or a rule would do
- No way to tell a good output from a bad one
- Ignoring running cost and maintenance
- Output longer than 3 paragraphs before the verdict
