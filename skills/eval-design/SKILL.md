---
name: eval-design
description: Design evaluations for an AI system so you know if it works before and after launch. Use when building or changing an LLM, RAG or agent feature, setting a ship bar, or when quality is "it seems fine".
---

# Eval design

An eval is the spec for an AI system's behaviour. Without one, every prompt change is a guess and every launch is a hope.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view before giving yours. Explain why each step matters, so the user can do it alone next time. End with one line on what they did well and one thing to practise.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer), no em dashes, no "not X but Y" contrasts, no bold labels on every line.
3. **Real outcomes only.** Every eval must trace to something a real user or the business cares about.
4. **Be honest.** If the system can't be evaluated yet (no one can say what good looks like), say so before designing anything.
5. **Short but complete.** Any summary or answer is at most 2 to 3 short paragraphs, never an essay. Most important point first. Compress the wording, not the content. Include the "so what" and the one reason it's true. Offer more depth in one line ("Want the detail on X?") instead of writing it.

## Process

### 1. Ask the user first
"Show me one great output and one bad output, and tell me why." If they can't, that is the first gap to close, usually by sitting with a domain expert.

### 2. Look at real outputs before choosing metrics
Collect 30 to 100 real or realistic outputs. Read them. Write a short note on each one that is wrong. Group the notes into failure modes (for example: wrong number, made-up policy, ignored the user's region, too long). Evals should target these real failures, not generic ideas of quality. This step is the one teams skip and the one that matters most.

### 3. Pick the quality dimensions
Only the ones that matter for this system:
- **Correct:** facts, numbers and decisions are right
- **Grounded:** claims come from the given sources, nothing made up
- **Complete:** nothing the user needed is missing
- **Safe:** no harmful, private or off-policy content; refuses when it should
- **Format and tone:** follows the required structure and voice
- **Cost and speed:** within budget and latency targets

For RAG, test retrieval separately from the answer: did the right document come back (recall at k), then did the answer use it faithfully. For agents, check task success, whether each tool call was right, and steps and cost per task.

### 4. Build the test set
- Start with 50 to 100 cases: real ones first, then edge cases, then adversarial ones (tricky, ambiguous, out of scope, prompt injection).
- Tag each case by slice (customer type, language, difficulty) so you can see where it fails, not just the average.
- Each case has: input, the expected answer or the criteria a good answer meets, and tags.
- Fill gaps with the synthetic-data skill, but keep real cases as the core.
- Never reuse test cases as examples inside the prompt.

### 5. Choose graders, cheapest reliable first
1. **Code checks:** exact match, regex, valid JSON, numbers within range. Fast, free, trustworthy.
2. **Reference comparison:** compare to a known correct answer.
3. **LLM as judge:** one pass/fail question per criterion, with a short rubric and examples of pass and fail. Avoid 1 to 10 scores; they drift and nobody agrees on what a 7 means.
4. **Human review:** for the judge's training labels, high-stakes cases, and spot checks.

Before trusting an LLM judge, have a human label at least 50 cases and check the judge agrees on roughly 90% or more. If it doesn't, fix the rubric, not the threshold.

### 6. Set the ship bar before seeing results
Agree with stakeholders, in writing, before the first run:
- Pass rate per dimension (for example: grounded 95%, format 99%)
- Critical failures with zero tolerance (for example: wrong price, personal data leak)
- Minimum per slice, so a good average can't hide a failing group

Setting the bar after seeing results turns the eval into a rubber stamp.

### 7. Run it as a habit
- Record a baseline. Re-run the full set on every prompt, model or data change.
- After launch, sample real traffic, track user feedback, and add every new failure to the test set.

## Output

A 2 to 3 sentence summary of how we'll know the system works, then:

```markdown
## Failure modes found
[From step 2, most common first]

## Eval plan
| Dimension | Why it matters | How measured | Grader | Ship bar | Critical? |

## Test set
[Size, sources, slices, gaps to fill]

## Judge validation
[Who labels, how many, agreement target]

## First step
[e.g. "Pull 50 real tickets and label failures with the support lead on Tuesday"]
```

## Red flags

- Metrics chosen before anyone read real outputs
- Only happy-path test cases
- An LLM judge nobody checked against humans
- 1 to 10 quality scores
- Ship bar set after the results came in
- Test cases leaked into the prompt
- One average number with no slices
