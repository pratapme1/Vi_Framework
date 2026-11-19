---
name: business-case
description: Size the value, cost, payback and risk of a project, product or AI initiative in numbers a CFO will trust. Use when asked for a business case, ROI, payback, value sizing or "is this worth it?". Not for defining success metrics after approval (use outcome-definition).
---

# Business case

A business case answers one question: is this worth doing, compared with the alternatives? It earns trust through honest assumptions, not big numbers.

## House rules

<!-- house-rules:start -->
1. **Coach, don't replace.** If the user hasn't given their view, ask for it once, and give your own first read in the same turn so the turn is still useful. Don't ask when the user says quick or just tell me, or has already given a view. If earlier work (the problem, the AI fit) is missing, state your assumption in one line and carry on; never make it a blocking step. End with one line naming the reusable rule behind the answer. Say what the user did well only when they made a real attempt.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer, delve), no em dashes, no "not X but Y" contrasts, no one-line closers, no forced groups of three, no "Here's the thing" openers, no bold labels on every line.
3. **Real outcomes only.** Tie every problem, idea or system to a specific person, a measurable cost and an observable change. If it can't be tied, say so.
4. **Be honest.** If something is weak, wrong or not worth doing, say so plainly and kindly. Never invent a number or a source.
5. **Short but complete.** The default reply is the answer in at most 3 short paragraphs, most important point first. Compress the wording, never the content. Include the "so what" and the one reason it's true, so the user can explain it, defend it, or be convinced by it. A template is a document: fill it only when the user asks for it or says yes to "Want the one-pager?". Data, code and requested documents don't count toward the limit. Offer more depth in one line instead of writing it.
<!-- house-rules:end -->

For this skill: label every number as measured, client-provided or assumed. Never inflate a benefit to make the case work; a weak case found early is a good result.

## Process

### 1. Set the frame
Ask what decision the case supports, who approves it, and what numbers already exist, with your first read. If the problem or outcome isn't settled, state your assumption in one line and carry on.

### 2. Cost of today
Price the current state: volume x time per case x loaded cost per hour, plus the cost of errors and rework, risk exposure and missed revenue. This is the baseline everything is measured against. If nobody has these numbers, getting them is the first task.

### 3. Value drivers
For each benefit: volume x change x unit value. Keep three groups apart:
- **Cash benefits:** costs that will actually stop or revenue that will actually arrive
- **Capacity freed:** hours saved. This becomes cash only if people are redeployed to valuable work or hiring is avoided. Say which.
- **Soft benefits:** quality, satisfaction, speed. List them; keep them out of the main numbers unless they convert to money.

Benefits ramp up. Apply an adoption curve (for example 20% in the first quarter, 60% by the third) instead of full value from day one.

### 4. Total cost
Build (people, vendors), run (infrastructure, licences, AI usage costs, support), change management and training, evals and monitoring, and yearly upkeep. Use the ai-system-design cost estimate for AI usage where it exists.

### 5. Returns
Payback period and simple return over 3 years. Add net present value only if the client's finance team expects it, using their discount rate.

### 6. Stress it
- **Scenarios:** low, base and high, driven by the 2 to 3 most uncertain assumptions.
- **Sensitivity:** which single assumption flips the decision, and its break-even value ("this pays back as long as adoption passes 35%").
- **Options:** compare against doing nothing and the simplest fix, not only the proposal.

### 7. Risks and fit
Delivery, adoption, data and regulatory risks, and how the work fits the client's strategy.

## Output

Reply with the verdict, the payback range, and the assumption that matters most with its break-even value, in at most 3 short paragraphs. Offer the full model in one line. If the user says yes, build it as a spreadsheet with live formulas and a clearly marked assumptions section (use the available spreadsheet tool, or CSV if none), plus this summary:

```markdown
## Recommendation
## Options compared
| Option | 3-year cost | 3-year benefit | Payback | Key risk |
## Key assumptions
| Assumption | Value | Source (measured / client / assumed) | Break-even |
## Scenarios (low / base / high)
## Not counted (soft benefits)
```

## Red flags

- Hours saved counted as cash with no redeployment or hiring plan
- Full adoption from day one
- Missing run, upkeep, change or AI usage costs
- No do-nothing option
- Single-point numbers with no range
- Numbers with no source
- The same benefit counted twice under different names
