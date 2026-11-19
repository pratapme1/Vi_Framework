---
name: ai-system-design
description: Choose the architecture for an AI system (prompt, workflow, RAG, text-to-SQL, agent, fine-tuning) and its key parts, costs and risks. Use after deciding AI fits, when designing or reviewing an LLM, RAG or agent solution.
---

# AI system design

Pick the simplest design that meets the bar, and make every choice explainable to a client in one sentence. Complexity is a cost, not a feature.

## House rules (apply to everything this skill produces)

1. **Coach, don't replace.** Ask for the user's own view before giving yours. Explain why each choice matters, so the user can design the next one alone. End with one line on what they did well and one thing to practise.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer), no em dashes, no "not X but Y" contrasts, no bold labels on every line.
3. **Real outcomes only.** Every component must exist because a requirement needs it.
4. **Be honest.** If the design is too complex, too costly or untestable, say so.
5. **Short but complete.** Any summary or answer is at most 2 to 3 short paragraphs, never an essay. Most important point first. Compress the wording, not the content. Include the "so what" and the one reason it's true. Offer more depth in one line ("Want the detail on X?") instead of writing it.

## Process

### 1. Check the inputs
You need a clear problem (problem-framing) and a verdict that AI fits (ai-fit-check). If either is missing, do that first.

### 2. Ask the user first
"Describe in your own words how a request flows from the user to the answer." Build on their sketch.

### 3. Pin the requirements that shape the design
- **Users and volume:** who, how many requests per day, peaks
- **Speed:** how fast must an answer come back
- **Accuracy bar:** cost of a wrong answer, and who reviews
- **Data:** where it lives, how fresh it must be, how sensitive, who is allowed to see what
- **Integrations:** systems to read from or act on
- **Budget:** acceptable cost per request and per month
- **Rules:** regulation, data residency, audit needs

### 4. Choose the pattern, simplest first

| Pattern | Use when | Watch out for |
|---|---|---|
| Single prompt | Classify, extract, summarize, draft | Breaks on long or varied inputs |
| Workflow (fixed chain of steps) | Steps are known in advance | Errors pass between steps; check each |
| RAG | Answers must come from your documents | Bad retrieval means bad answers |
| Text-to-SQL | Answers live in databases | Wrong joins, access control, ambiguous terms |
| Agent with tools | The path can't be known in advance | Cost, loops, unpredictable actions |
| Fine-tuning | Narrow task, lots of labeled data, need for consistency or lower cost at scale | Rarely the first step; try prompting and RAG first |

Rule of thumb: if you can draw the steps as a flowchart, build a workflow, not an agent. Combine patterns when needed (for example, a workflow where one step uses RAG).

### 5. Walk the components
- **Input:** validation, removing personal data, detecting out-of-scope requests
- **Context:** for RAG, how documents are split, hybrid search (keywords plus meaning), reranking, and filtering by the user's permissions before anything reaches the model
- **Model:** the smallest model that passes the evals; a larger one only for the hard steps; a fallback if the provider fails
- **Output:** a fixed structure (schema), validation, citations to sources, an honest "I don't know" path
- **Human in the loop:** where a person reviews or approves, especially before any action with real consequences
- **Observability:** log every input, retrieved context, output, cost and latency, so failures can be traced
- **Evals:** hooks to run the eval-design test set on every change
- **Feedback:** a way for users to flag bad answers, feeding new test cases

### 6. Estimate cost and speed
Cost per request = tokens in and out per call x number of calls x price. Multiply by daily volume. Add up the time each step takes against the speed target. Show the numbers; a design without them can't be approved.

### 7. List failure modes and controls

| Failure | Control |
|---|---|
| Made-up answers | Ground in sources, require citations, eval for groundedness |
| Stale or wrong data | Refresh schedule, show data dates |
| Prompt injection | Treat retrieved text as data, limit tool permissions, require approval for actions |
| Data leak across users | Permission filtering at retrieval, never in the prompt alone |
| Runaway agent | Step and cost limits, timeouts |
| Provider outage | Fallback model, graceful error message |

### 8. Define the first slice
The thinnest version that runs end to end on real data for one use case, with evals from day one. Note what to buy (platform services) versus build.

## Output

A 2 to 3 sentence summary the user could say to a client, then:

```markdown
## Flow
User -> [step] -> [step] -> answer   (simple text diagram)

## Key decisions
| Decision | Choice | Why | Rejected option and why |

## Cost and speed
[Per request and per month; latency per step vs target]

## Risks and controls
[Top 3 from step 7]

## First slice
[Scope, data, success measure]

## Open questions
```

## Red flags

- An agent for a process that is really a fixed set of steps
- Model chosen before requirements
- RAG with no permission filtering
- No cost or speed estimate
- No logging or eval hooks
- Fine-tuning as the first move
- No fallback and no "I don't know" path
