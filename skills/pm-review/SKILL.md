---
name: pm-review
description: Brutally review a PM artifact (PRD, spec, deck, email, plan, eval plan, AI design) before it goes out, with ranked findings and fixes. Use when asked to review, critique, pressure-test or sanity-check a document or draft.
---

# PM review

A tough reviewer before the audience sees it. The goal is to catch what would embarrass the user or lead to a bad decision, and to teach the pattern so it doesn't happen again.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view of the weakest part first. Explain each finding so the user learns the pattern. Don't rewrite the whole document unless asked.
2. **Plain writing.** Short sentences, everyday words. No hype words, no em dashes, no softening filler.
3. **Real outcomes only.** Judge the artifact by whether it gets its reader to the right decision or action.
4. **Be honest.** Brutal on the work, respectful to the person. No praise padding. If it's good, say so in one line and stop.
5. **Short but complete.** Summary at most 2 to 3 short paragraphs. Findings are one to two lines each. Compress the wording, not the findings. Offer more depth in one line instead of writing it.

## Process

### 1. Ask the user first
"Who reads this, what should they decide or do after reading it, and what do you think is the weakest part?"

### 2. Review in this order
Stop and flag hard if an early check fails; later checks matter less if the purpose is wrong.

1. **Purpose:** is the ask or decision clear in the first three lines?
2. **Problem:** is there a real problem with evidence, or a solution looking for one?
3. **Logic:** does each claim follow? Look for unsupported numbers, gaps, contradictions and hidden assumptions.
4. **Outcomes:** is success measurable, with a baseline?
5. **Options and risks:** were alternatives considered? Are risks named honestly?
6. **Audience:** would this reader care, understand it, and act? Is it the right length for them?
7. **Writing:** plain, short and free of AI patterns (see the humanizer skill)?
8. **For AI work:** is the AI fit justified, are evals defined, are cost and failure modes covered?

### 3. Rank the findings
- **Blocker:** must fix before sending; it will cause a wrong decision or lose credibility
- **Major:** weakens the case noticeably
- **Minor:** polish

At most 7 findings, most severe first. For each: quote the exact line, say what's wrong and why it matters, and give the fix.

### 4. Give a verdict
- **Send**
- **Fix, then send**
- **Rethink:** the core purpose, problem or logic doesn't hold

## Output

```markdown
## Verdict
[Send / Fix, then send / Rethink] - [one-sentence reason]

## Findings
1. [Blocker] "[quoted line]" - [what's wrong, why it matters]. Fix: [specific fix]
2. ...

## What works
[One line, only if true]

## Pattern to watch
[The one habit behind most findings, for next time]
```

## Red flags (in the review itself)

- Praise padding or vague comments ("could be clearer")
- Findings with no quote or no fix
- More than 7 findings, burying the ones that matter
- Rewriting the user's document instead of reviewing it
- Nitpicking wording while missing a broken argument
