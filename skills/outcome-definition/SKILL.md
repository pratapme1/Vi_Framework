---
name: outcome-definition
description: Turn goals and features into measurable outcomes, success metrics and guardrails, with baselines and targets. Use when defining success for a product, project or AI system, writing OKRs, or when "done" means "shipped".
---

# Outcome definition

Shipping a feature is an output. People behaving differently because of it is an outcome. The business result that follows is the impact. This skill makes sure work is judged on the last two.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view before giving yours. Explain why each step matters, so the user can do it alone next time. End with one line on what they did well and one thing to practise.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer), no em dashes, no "not X but Y" contrasts.
3. **Real outcomes only.** Every metric ties to a change for a specific person and to a business result.
4. **Be honest.** If there's no baseline or no way to measure, say so. That becomes the first task.
5. **Short but complete.** Any explanation is at most 2 to 3 short paragraphs. Compress the wording, not the facts. Offer more depth in one line instead of writing it.

## Process

### 1. Ask the user first
"If this works, what will be different, and for whom? How would you notice?"

### 2. Separate output, outcome and impact
- **Output:** what we ship (a chatbot, a dashboard, a new process)
- **Outcome:** what people do differently (agents resolve tickets without escalating)
- **Impact:** the business result (support cost per ticket falls)

If the user's goal is an output, ask "so that what?" until you reach an outcome.

### 3. Write the outcome statement

> [Who] will [change in behaviour] from [baseline] to [target] by [date], measured by [metric and source].

### 4. Build the metric tree
- **Impact metric:** revenue, cost, risk or satisfaction. Moves slowly.
- **Outcome metrics:** the behaviour change. Moves in weeks.
- **Leading indicators:** things the team can move week to week that predict the outcome (adoption, usage, time to first value).
- **Guardrails:** what must not get worse (quality, error rate, cost, customer satisfaction, team workload).

### 5. Get the baseline
Every metric needs today's number. If nobody has it, measuring it is the first task, before any target is set.

### 6. Set targets
Base them on the baseline, comparable cases and what's realistic in the time. A range is fine. A target with no baseline is a wish.

### 7. For AI systems, connect the layers
Link offline eval results to live product outcomes to business impact. Example: grounded-answer rate (eval) leads to tickets resolved without escalation (outcome) leads to lower cost per ticket (impact). Add trust and adoption metrics: do people use it, accept its outputs, and come back?

### 8. Plan the measurement
For each metric: data source, owner, how often it's checked, and how you'll know the change came from this work (a control group, an A/B test, or a before-and-after with comparison). Name how each metric could be gamed.

## Output

A 2 to 3 sentence summary the user could say to a sponsor, then:

```markdown
## Outcome statement
[One sentence from step 3]

## Metrics
| Metric | Type (impact / outcome / leading / guardrail) | Baseline | Target | Source | Owner |

## How we'll know it was us
[Attribution method]

## Gaming risks
[How each key metric could be gamed, and the counter-check]

## First step
[Usually: get the missing baselines]
```

## Red flags

- Success defined as shipping
- No baseline
- Only lagging business metrics, nothing the team can move this month
- No guardrails
- Vanity metrics (logins, page views) as the main measure
- AI quality measured only offline, with no link to real outcomes
