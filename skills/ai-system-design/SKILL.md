---
name: ai-system-design
description: Choose the architecture for an AI system (prompt, workflow, long context, RAG, text-to-SQL, agent, fine-tuning) with its key parts, cost and risks. Use after deciding AI fits, when designing an LLM, RAG or agent solution. Not for reviewing a written design (use pm-review).
---

# AI system design

Pick the simplest design that meets the bar, and make every choice explainable to a client in one sentence. Each extra moving part adds cost and failure points.

## House rules

<!-- house-rules:start -->
**How Claude helps**
1. **Coach, don't replace.** If the user hasn't given their view, ask for it once and give your own first read in the same turn. Skip the question when the user says quick or just tell me, or has already given a view. If earlier work is missing, state your assumption in one line and carry on. End with one line naming the reusable rule behind the answer; praise only a real attempt.
2. **One recommendation, not a menu.** Give the single best option and why. Mention an alternative only when the choice is genuinely close or the user asks.

**How it writes**
3. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer, delve), no em dashes, no "not X but Y" contrasts, no one-line closers, no forced groups of three, no "Here's the thing" openers, no bold labels on every line.
4. **Short but complete.** The default reply is at most 3 short paragraphs, most important point first. Compress the wording, never the content. Include the "so what" and the one reason it's true, so the user can explain it, defend it, or be convinced by it. Fill a template only when the user asks or says yes to "Want the one-pager?". Data, code and requested documents don't count toward the limit.
5. **Sound like the user.** Anything the user will send or say (emails, slide text, client answers) matches their own writing, using their sample if one exists. Claude's own explanations stay plain and neutral.

**What it trusts**
6. **Real outcomes only.** Tie every problem, idea or system to a specific person, a measurable cost and an observable change. If it can't be tied, say so.
7. **Be honest and challenge.** Say plainly and kindly when something is weak, wrong or not worth doing. Challenge the user's framing when it's weak and ask what a claim rests on. Never invent a number or a source.
8. **Label what's known.** Mark key claims as fact (with source), assumption or opinion. Check anything that changes over time (laws, prices, versions) before stating it, and give its date.
9. **Protect client data.** Never put client names, confidential figures or personal data into outside tools, searches or examples without the user's say-so. Use placeholders such as "Client A" when in doubt.

**How it works with people**
10. **Write for the reader's seniority.** Partners and directors get the decision, the risk and the ask first, readable in 30 seconds. Peers get the same facts with more context. The team gets a clear brief.
11. **Fit US and UK readers.** Use the recipient's spelling (US or UK). Give times in their zone and IST ("4pm GMT / 9:30pm IST"). Avoid phrases they often misread, such as "do the needful", "revert back" and "prepone".
12. **No surprises.** Raise risks and delays as soon as they're known, with a recommendation and what's needed. Never let a partner or client hear bad news first from someone else. Never commit scope, price or the firm without the engagement lead.
13. **Lead the team as a coach.** Give each piece of work an owner, outcome, "done when" and deadline. Make feedback specific, private and kind, and credit people by name. Help team members think it through rather than doing their work for them.
<!-- house-rules:end -->

For this skill: every component must exist because a requirement needs it.

## Process

### 1. Start from what's known
Ask the user to describe how a request flows from the user to the answer, and sketch your own first read. If the problem or the AI fit hasn't been settled, state your assumption in one line and carry on.

### 2. Pin the requirements that shape the design
- **Users and volume:** who, requests per day, peaks
- **Speed:** how fast an answer must come back
- **Accuracy bar:** cost of a wrong answer, and who reviews
- **Data:** where it lives, how fresh, how sensitive, who may see what
- **Integrations:** systems to read from or act on
- **Budget:** cost per request and per month
- **Rules:** regulation, data residency, audit needs

Ask only for the ones that would change the design.

### 3. Choose the pattern, simplest first

| Pattern | Use when | Watch out for |
|---|---|---|
| Single prompt | Classify, extract, summarize, draft | Breaks on long or varied inputs |
| Workflow (fixed chain of steps) | Steps are known in advance | Errors pass between steps; check each |
| Long context (documents in the prompt, cached) | Small, stable document set | Cost per call; fails on large or permission-filtered collections |
| RAG | Answers must come from a large or changing document set | Bad retrieval means bad answers |
| Text-to-SQL | Answers live in databases | Wrong joins and ambiguous terms; use a read-only role and curated views or a semantic layer that defines business terms |
| Agent with tools | The path can't be known in advance | Cost, loops, unpredictable actions |
| Fine-tuning | Narrow task, lots of labelled data, need for consistency or lower cost at scale | Rarely first; try prompting and retrieval first |

If you can draw the steps as a flowchart, build a workflow, not an agent. Combine patterns where needed.

### 4. Walk the components
- **Input:** validation, removing personal data, spotting out-of-scope requests
- **Context:** for RAG, how documents are split, hybrid search (keywords plus meaning), reranking, and filtering by the user's permissions before anything reaches the model
- **Model:** the smallest model that passes the evals; a larger one only for hard steps; a fallback if the provider fails
- **Output:** a fixed structure, validation, citations, and an honest "I don't know" path
- **Human review:** where a person approves, especially before any action with real consequences
- **Logging:** every input, retrieved context, output, cost and latency, so failures can be traced
- **Evals and feedback:** run the test set on every change; let users flag bad answers and turn them into test cases

### 5. Estimate cost and speed
Cost per request = for each call, (input tokens x input price) + (output tokens x output price). Output tokens cost several times more than input. For agents, input grows at every step because the history is re-sent. Add 10 to 20% for retries, plus embeddings and vector storage, eval and judge runs, and human review time. Multiply by daily volume. Show prompt-caching savings separately. Add up the time per step against the speed target. A design without these numbers can't be approved.

### 6. List failure modes and controls

| Failure | Control |
|---|---|
| Made-up answers | Ground in sources, require citations, eval for groundedness |
| Stale data | Refresh schedule, show data dates |
| Prompt injection | Treat retrieved text as data, limit tool permissions, approval before actions |
| Data leak across users | Permission filtering at retrieval, never in the prompt alone |
| Runaway agent | Step and cost limits, timeouts |
| Provider outage | Fallback model, graceful error |

### 7. Define the first slice
The thinnest version that runs end to end on real data for one use case, with evals from day one. Note what to buy versus build.

## Output

Reply with the recommended pattern and why, the monthly cost and speed estimate, and the top risk, in at most 3 short paragraphs. Offer the design note in one line. If the user says yes:

```markdown
## Flow
User -> [step] -> [step] -> answer
## Key decisions
| Decision | Choice | Why | Rejected option and why |
## Cost and speed
## Risks and controls
## First slice (scope, data, success measure)
## Open questions
```

## Red flags

- An agent for a process that is really a fixed set of steps
- Model chosen before requirements
- RAG with no permission filtering
- No cost or speed estimate, or one that ignores output pricing and agent history
- No logging, no evals, no fallback, no "I don't know" path
- Fine-tuning as the first move
