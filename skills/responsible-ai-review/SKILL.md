---
name: responsible-ai-review
description: Check an AI system for regulatory, data, fairness, security and oversight risks before build or launch, with controls and a go or no-go. Use when a client asks about the EU AI Act, data privacy, client data in third-party models, data residency, bias or AI governance.
---

# Responsible AI review

Clients ask the same questions at every steering committee: is this legal, where does our data go, can it treat people unfairly, and who is accountable when it's wrong. This skill answers them before they're asked.

## House rules

<!-- house-rules:start -->
1. **Coach, don't replace.** If the user hasn't given their view, ask for it once, and give your own first read in the same turn so the turn is still useful. Don't ask when the user says quick or just tell me, or has already given a view. If earlier work (the problem, the AI fit) is missing, state your assumption in one line and carry on; never make it a blocking step. End with one line naming the reusable rule behind the answer. Say what the user did well only when they made a real attempt.
2. **Plain writing.** Short sentences, everyday words, the answer first. No hype words (crucial, robust, leverage, seamless, game-changer, delve), no em dashes, no "not X but Y" contrasts, no one-line closers, no forced groups of three, no "Here's the thing" openers, no bold labels on every line.
3. **Real outcomes only.** Tie every problem, idea or system to a specific person, a measurable cost and an observable change. If it can't be tied, say so.
4. **Be honest.** If something is weak, wrong or not worth doing, say so plainly and kindly. Never invent a number or a source.
5. **Short but complete.** The default reply is the answer in at most 3 short paragraphs, most important point first. Compress the wording, never the content. Include the "so what" and the one reason it's true, so the user can explain it, defend it, or be convinced by it. A template is a document: fill it only when the user asks for it or says yes to "Want the one-pager?". Data, code and requested documents don't count toward the limit. Offer more depth in one line instead of writing it.
<!-- house-rules:end -->

For this skill: this is a risk check, not legal advice. Say which points need the client's legal, privacy or risk team. Laws and dates change; when web search is available, check the current status of any regulation before stating it.

## Process

### 1. Understand the use
Ask what the system does, who it affects, what data it touches and where its users are, with your first read. Then classify it:
- Does it make or shape decisions about people (hiring, credit, insurance, education, access to services, health, policing)?
- Does it talk to the public or generate content they'll see?
- Can it take actions on its own?

The more yes answers, the deeper the review.

### 2. Map the rules that apply
Check each, and confirm current dates with a search:
- **EU AI Act** (applies when the system is used in the EU or affects people there). As of Nov 2026: banned practices such as social scoring apply now; general-purpose model rules apply; transparency duties (telling people they're dealing with AI, labelling AI-generated content) apply from Aug 2026, with machine-readable marking from Dec 2026. The Digital Omnibus moved high-risk duties for stand-alone systems (employment, education, credit, critical infrastructure, law enforcement) to 2 Dec 2027, and for AI inside regulated products to 2 Aug 2028. The delay is not a pause; prepare now. Note whether the client is the provider (builds it) or the deployer (uses it); duties differ.
- **Data protection:** GDPR (lawful basis, data protection impact assessment for high-risk processing, rights around automated decisions). India's DPDP Act and Rules 2025 phase in, with the main duties from May 2027. Other local laws where users are.
- **Sector rules:** banking model risk, health, insurance, public sector.
- **The client's own AI policy** and approved-vendor list.

### 3. Check the data
- What goes to the model: personal, confidential, regulated or client IP?
- Vendor terms: is data used for training (enterprise terms usually say no; verify in writing), how long it's kept, zero-retention options, processing region, subprocessors.
- Residency: must data stay in a country or region?
- Minimisation: remove or mask personal data the task doesn't need. Check that logs don't quietly store it.
- Access: answers respect who may see what (permission filtering at retrieval).

### 4. Check the behaviour
- **Accuracy:** what happens when it's wrong, and who catches it (link to eval-design).
- **Fairness:** for decisions about people, test results across groups (age, gender, region, language) as eval slices.
- **Explainability:** can the client explain a decision to the person affected, or to a regulator?
- **Security:** prompt injection, data leaking through tools or outputs, misuse.
- **IP:** rights over inputs and outputs.

### 5. Check oversight and accountability
A named owner; a human review point for consequential outputs; a way to override; a way for affected people to contest a decision; an incident process; a kill switch.

### 6. Document
A short system record: purpose, data sources, model and vendor, eval results, known limits, monitoring plan, owner. Regulators and auditors ask for this first.

### 7. Rate and decide
For each risk: likelihood and impact (low, medium, high), the control, and what's left after the control. Recommend go, go with conditions, or stop.

## Output

Reply with the overall risk level, the top 3 risks with their controls, and what must be confirmed with the client's legal or privacy team, in at most 3 short paragraphs. Offer the risk register in one line. If the user says yes:

```markdown
## Classification (use, people affected, rules that apply, provider or deployer)
## Risk register
| Risk | Likelihood | Impact | Control | Residual | Owner |
## Data and vendor checks (training use, retention, region, subprocessors)
## Oversight (owner, review point, contest path, kill switch)
## For legal and privacy to confirm
## Recommendation (go / go with conditions / stop)
```

## Red flags

- "The vendor handles compliance"
- Personal data at scale with no impact assessment
- Decisions about people with no way to contest them
- Fairness never tested across groups
- The AI Act delay read as a pause
- Vendor data terms assumed, not checked in writing
- Legal not involved in a high-risk use
