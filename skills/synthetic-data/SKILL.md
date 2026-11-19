---
name: synthetic-data
description: Create realistic synthetic data for testing, evals, demos or prototypes when real data is scarce, sensitive or missing edge cases. Use when you need test cases, sample records, fake documents or user queries.
---

# Synthetic data

Synthetic data fills gaps. It never replaces real data. Its job is to cover the cases you haven't seen yet, without exposing anyone's private information.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view before giving yours. Explain why each step matters, so the user can do it alone next time. End with one line on what they did well and one thing to practise.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer), no em dashes, no "not X but Y" contrasts, no bold labels on every line.
3. **Real outcomes only.** Every dataset must serve a stated purpose: a test, a demo or a decision.
4. **Be honest.** Say where synthetic data will mislead, and when real data is the only answer.
5. **Short but complete.** Any summary or answer is at most 2 to 3 short paragraphs, never an essay. Most important point first. Compress the wording, not the content. Include the "so what" and the one reason it's true. Offer more depth in one line ("Want the detail on X?") instead of writing it. Data itself goes in a file or table and doesn't count toward the limit.

## Process

### 1. Ask the user first
"What is this data for, and what real data do you already have?" The purpose decides everything:
- **Eval test cases:** coverage of failure modes and edge cases matters most
- **Demo or prototype:** realism and a believable story matter most
- **Load or integration test:** volume, valid formats and relationships matter most
- **Training data:** quality and balance matter most, and the risk is highest

### 2. Start from real examples
Gather 10 to 30 real examples, with personal details removed. Note what varies between them. A model asked to invent data from nothing produces clean, average, repetitive cases that look nothing like real life.

### 3. Define the dimensions first
List the ways real cases differ, then combine them. This is what stops the data being samey.

| Dimension | Values |
|---|---|
| Persona | new customer, power user, angry customer |
| Intent | refund, status check, complaint, out of scope |
| Difficulty | simple, multi-part, ambiguous |
| Style | formal, casual, typos, very short |

Pick combinations that cover the slices that matter, especially the risky ones. You don't need every combination.

### 4. Generate in two steps
1. Write one line per combination describing the case.
2. Turn each line into a full, natural record.

Ask for realism on purpose: typos, missing details, two questions in one, wrong assumptions, mixed languages where relevant. Then add hard cases on purpose: out of scope, contradictory, very long, empty fields, wrong format, and attempts to trick the system (prompt injection).

**For tables and records:** keep the real schema, realistic value ranges and distributions, and relationships that hold (totals add up, IDs match across tables, dates are in order). Add real-world mess: blanks, duplicates, inconsistent formats. Use obviously fake names, emails and numbers. Never copy real personal data.

When code tools are available, write a small script that produces the data as CSV or JSONL, so it can be regenerated and versioned.

### 5. Check quality before using it
- Read at least 20 to 30 records yourself. Ask a domain expert: "Could this be real?"
- Remove duplicates and near-duplicates.
- Check coverage against the dimensions table. Fill holes.
- Check every expected answer or label by hand on a sample. The generating model makes mistakes too.
- Don't let the same model generate the data and grade the system without a human check in between.

### 6. Label and store it
Tag every record as synthetic, with its dimension values and its expected output or criteria. Keep it separate from real data. Version it. As real production data arrives, replace synthetic cases with real ones.

## Output

A 2 to 3 sentence summary of what was made and what it covers, then:

```markdown
## Purpose
[What this data is for]

## Dimensions
| Dimension | Values |

## Sample
[5 representative records, including at least one hard case]

## Generation prompt
[The reusable prompt or script, so the user can make more]

## Quality check
[What was checked, what was removed, known gaps]

## Limits
[Where this data could mislead]
```

## Red flags

- Generated from nothing, with no real examples as a base
- All records clean, polite and average
- No hard or adversarial cases
- Expected answers never checked by a person
- Real personal data copied in
- Synthetic data used as the only evidence that a system works
