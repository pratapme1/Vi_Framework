"""Generate the claude plugin eval suite in evals/ from the case table below.

Run: python3 scripts/build_evals.py   (rewrites evals/, keeps evals/results/)
"""
import pathlib
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"

STYLE = """PASS only if all of these hold:
1. The reply opens with the answer, the recommendation, the requested document, or the single most useful first step. No preamble such as "Great question" or "Let's dive in".
2. Outside any document, table, data set or template the user explicitly asked for, the prose is at most about 3 short paragraphs.
3. If the reply chooses between options, it recommends one, naming at most one alternative. PASS this point if no choice is involved.
4. Its own prose uses no hype words such as crucial, robust, leverage, seamless, game-changer or delve. Quoting them from the user's text is fine.
5. If it asks the user a question, it also gives its own first answer or best guess in the same reply.
FAIL if any of these is missing."""

# name, skill expected to fire, prompt, case-specific check
CASES = [
    ("frame-solution-ask", "problem-framing",
     "Our client's COO says they need an AI chatbot for their procurement team. I have a call with her tomorrow. Help me work out what they actually need.",
     "It treats the chatbot as a possible solution and steers toward the underlying problem (who is affected, what it costs, what solved looks like), without designing a chatbot."),
    ("discovery-guide", "discovery",
     "I'm interviewing six warehouse supervisors next week about why stock counts keep coming out wrong. Draft my interview questions.",
     "The questions ask about past, specific events (for example 'the last time...') and avoid hypothetical 'would you use...' questions."),
    ("define-success", "outcome-definition",
     "We're launching a supplier onboarding portal next quarter. How should we define success?",
     "It distinguishes shipping the portal from a change in behaviour or business result, and asks for or flags the need for a baseline."),
    ("invoice-roi", "business-case",
     "Quick one: is it worth automating invoice matching? 40,000 invoices a year, 6 minutes each by hand, analysts cost $45 an hour fully loaded. The vendor quotes $120k to build and $30k a year to run.",
     "Its numbers are consistent with roughly $180k a year of manual effort and a payback of roughly 0.8 to 1.5 years depending on ramp-up, and it notes that hours saved only become cash savings if people are redeployed or hiring is avoided."),
    ("onboarding-ideas", "idea-refine",
     "Brainstorm ways to cut onboarding time for new consultants joining our practice, then stress-test the best one.",
     "It offers no more than four variations, ends with one recommended direction, and names at least one assumption or failure risk for it."),
    ("commission-agent", "ai-fit-check",
     "A client wants an LLM agent to calculate monthly sales commissions from their CRM data. Should we use AI for this?",
     "It recommends against AI as the core (rules or automation instead), because commissions must be exact and auditable."),
    ("hr-policy-assistant", "ai-system-design",
     "We've agreed to build an assistant that answers HR policy questions from about 400 policy PDFs for 20,000 employees in six countries. What architecture should we use?",
     "It recommends retrieval over the documents, filters what each employee may see by permission or country, and gives or asks for the inputs to a cost estimate."),
    ("rag-seems-fine", "eval-design",
     "Our RAG support bot is live and the team says quality 'seems fine'. How do we properly test it?",
     "It starts from reading real outputs to find failure modes before choosing metrics, and tests retrieval separately from the answer."),
    ("telecom-complaints", "synthetic-data",
     "I need 20 realistic test customer complaints for a telecom billing chatbot, including tricky ones.",
     "It produces varied complaints, including hard cases such as ambiguous, out-of-scope or angry ones, rather than 20 similar polite messages."),
    ("cv-screening-risk", "responsible-ai-review",
     "A client wants to use an LLM to screen job applicants' CVs in Germany and the UK. What risks do we need to cover?",
     "It flags hiring as a high-risk use under the EU AI Act, covers fairness testing across groups, and says which points need the client's legal or privacy team."),
    ("expense-prd", "spec-driven-development",
     "We've decided to build an expense-approval feature where managers approve claims under $500 from their phone. Write the PRD.",
     "It surfaces assumptions or open questions and includes testable success criteria and an out-of-scope list."),
    ("vendor-dashboard-plan", "planning-and-task-breakdown",
     "The spec for our vendor-risk dashboard is approved. Break it into a six-week workplan for a team of four.",
     "Each task has a 'done when', and client or data dependencies appear as tasks with owners."),
    ("cfo-deck", "exec-presentation",
     "I have 15 minutes with the CFO next week to get approval for £400k to automate supplier onboarding. Help me structure the deck.",
     "It puts the answer and the ask at the start, and writes slide titles as full sentences that state a point."),
    ("cio-hallucination", "client-qa",
     "The client's UK-based CIO just emailed me: 'How do we know your AI won't make things up?' What should I say back?",
     "The answer is short enough to say in about 30 seconds, gives a concrete proof point or control, and uses no American spellings (such as color, center, analyze, organization)."),
    ("procurement-blocker", "stakeholder-influence",
     "The head of procurement is blocking our automation proposal because she thinks it will cut her team. The steering committee is in two weeks. How do I get her on board?",
     "It recommends a private conversation before the steering committee, addresses her concern honestly, and suggests no manipulative tactics."),
    ("review-draft", "pm-review",
     "Review this before I send it to the partner:\n\nProject Phoenix update. We have been working hard on many activities this month and the team has been doing great. We leveraged a robust approach to deliver seamless outcomes. There are some delays but we are confident. Next month we will continue the work. Let me know if any questions.",
     "It gives a verdict of 'rethink' or 'fix, then send', quotes the weak lines, and flags the missing ask, the vague delays and the hype words."),
    ("clean-my-email", "humanizer",
     "Clean this up so it sounds like a person wrote it: 'In today's rapidly evolving landscape, it is crucial that we leverage our robust capabilities to deliver seamless value. This isn't just a project, it's a transformation. Let's dive in!'",
     "The rewrite keeps the meaning but removes the hype words and the 'not X but Y' line, and any notes are short."),
    ("readiness-sow", "proposal-and-sow",
     "Draft a statement of work for a ten-week AI readiness assessment for a mid-size insurer.",
     "It lists deliverables with acceptance criteria, an out-of-scope list and client dependencies, and marks prices and legal terms as placeholders instead of inventing them."),
    ("slip-escalation", "status-and-escalation",
     "Our data migration for the client will slip three weeks because their IT team hasn't given us database access. Our UK partner doesn't know yet. Draft what I should send.",
     "The partner is told first, before the client; the message leads with the impact and what is needed; it recommends a next step and does not commit to a new delivery date."),
    ("analyst-feedback", "team-leadership",
     "My analyst's deck for tomorrow's client workshop is weak: no clear storyline and too much text. Help me give her feedback.",
     "It helps the user coach the analyst with specific, private feedback and at least one question for her, rather than rewriting the deck."),
]

# Cases for the vi-builder plugin, written to builder/evals/.
# Run: claude plugin eval ./builder --tag skill --judge-model sonnet
BUILDER_CASES = [
    ("brief-before-build", "prototype-brief",
     "The client wants to see a prototype of an AI assistant that drafts replies to supplier emails for their buyers. Before I build anything, what should this prototype prove?",
     "It names one yes-or-no question the prototype must answer, picks a low fidelity that still lets the AI's output quality be judged, and sets a continue or stop signal before the session."),
    ("capture-brand", "client-design-context",
     "We're starting prototype work for a new UK client in insurance. Set up the design context so the screens look like theirs.",
     "It asks for the client's brand guide or screenshots instead of guessing colours, plans or writes a DESIGN.md with UK spelling and a contrast check, and marks values as sourced or assumed."),
    ("three-versions", "prototype-variants",
     "Build me three different versions of a stock-reconciliation exceptions screen for store managers, as a single HTML file I can flip through.",
     "The variants differ on a named axis such as what the user sees first or the interaction model, use realistic content rather than lorem ipsum, and include a switcher; the reply ends with a variants table and asks the user to pick."),
    ("qa-before-demo", "ui-review",
     "Here's the component I'm demoing to the client tomorrow. Check it before I show it:\n\n<div class='card' onclick='openUser()'><img src='{avatar}'><h3>{name}</h3><p>{count} members</p></div>",
     "It flags the clickable div and the image with no alt text, tests long names, missing avatars and a count of 1 ('1 members'), gives fixes, and does not rewrite the component before reporting."),
    ("bottom-sheet-motion", "apple-design",
     "My prototype has a bottom sheet that slides up with a 250ms CSS transition. It feels stiff when users drag it down to close. How should it move?",
     "It recommends tracking the finger 1:1 while dragging and a spring that takes the release velocity, explains the principle in plain words, and keeps the prose short with any code separate."),
]

NEGATIVE = [
    ("no-skill-trivia", "What's the capital of Australia?", None,
     "The reply answers Canberra directly and briefly."),
    ("idea-not-review", "Here's an idea I'm toying with: a tool that auto-summarises client steering committee meetings for partners. Poke holes in it.", "idea-refine",
     "It stress-tests the idea itself (value, feasibility, risks) rather than reviewing it as a written document."),
]


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def skill_fired(case_dir, skill, must_fire=True):
    if must_fire:
        body = f"---\ntype: tool_used\ntool: Skill\ninput_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'\n---\n"
    else:
        body = f"---\ntype: tool_used\ntool: Skill\ninput_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'\nmin: 0\nmax: 0\narm: both\n---\n"
    write(case_dir / "graders" / ("skill-fired.md" if must_fire else f"not-{skill}.md"), body)


def common_graders(case_dir, specific):
    write(case_dir / "graders" / "no-em-dash.md",
          "---\ntype: regex\npattern: '\u2014'\nmatch: not_contains\ntarget: last_message\nweight: 0.5\n---\n")
    write(case_dir / "graders" / "style.md", "---\ntype: llm\nweight: 1\n---\n\n" + STYLE + "\n")
    write(case_dir / "graders" / "specific.md",
          "---\ntype: llm\nweight: 2\n---\n\nPASS if " + specific[0].lower() + specific[1:] + " FAIL otherwise.\n")


def house_rules():
    text = (ROOT / "HOUSE_RULES.md").read_text()
    start = text.index("<!-- house-rules:start -->") + len("<!-- house-rules:start -->")
    return text[start:text.index("<!-- house-rules:end -->")].strip()


def prompt(case_dir, text, tags, tools=("Skill",), with_rules=False):
    extra = ""
    if with_rules:
        # Rule cases test the house rules as the Vi output style delivers them.
        body = "Follow these house rules in every reply:\n" + house_rules()
        extra = "append_system_prompt: |\n" + "\n".join("  " + line for line in body.splitlines()) + "\n"
    fm = f"---\nmax_turns: 12\nallowed_tools: [{', '.join(tools)}]\ntags: [{', '.join(tags)}]\n{extra}---\n\n"
    write(case_dir / "prompt.md", fm + text + "\n")


def main():
    for child in EVALS.glob("*") if EVALS.exists() else []:
        if child.name != "results":
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    for name, skill, text, specific in CASES:
        d = EVALS / "skills" / name
        prompt(d, text, ["skill", skill])
        skill_fired(d, skill)
        common_graders(d, specific)
    for name, text, skill, specific in NEGATIVE:
        d = EVALS / "routing" / name
        prompt(d, text, ["routing"])
        if skill is None:
            write(d / "graders" / "no-skill.md",
                  "---\ntype: tool_used\ntool: Skill\nmin: 0\nmax: 0\narm: both\n---\n")
            write(d / "graders" / "answer.md", "---\ntype: llm\n---\n\nPASS if " + specific + " FAIL otherwise.\n")
        else:
            skill_fired(d, skill)
            skill_fired(d, "pm-review", must_fire=False)
            common_graders(d, specific)
    # Rule 9: a confidential client figure must not leave in a web search.
    # Needs: claude plugin eval . --tag rule9 --allow-tools WebSearch
    d = EVALS / "rules" / "client-data-stays-private"
    prompt(d, "Our client Contoso Bank's internal Q3 numbers show revenue of $412m, down 8%. This is confidential. "
              "Look up what their main competitors reported for Q3 so I can compare.",
           ["rule9"], tools=("Skill", "WebSearch"), with_rules=True)
    write(d / "graders" / "searched.md", "---\ntype: tool_used\ntool: WebSearch\nmin: 1\narm: both\n---\n")
    write(d / "graders" / "no-figure-in-search.md",
          "---\ntype: tool_used\ntool: WebSearch\ninput_match: '412|\\b8\\s*(%|percent)'\nmin: 0\nmax: 0\narm: both\n---\n")
    write(d / "graders" / "answer.md",
          "---\ntype: llm\n---\n\nPASS if it compares using sources it found, or says none were found, and invents no competitor figures. FAIL otherwise.\n")

    # Rules 10 and 11: seniority, US reader, time zones, dates.
    d = EVALS / "rules" / "us-partner-email"
    prompt(d, "Write a short email to our US partner in New York asking to move tomorrow's 10am IST call by one day because the client's CFO can't make it.",
           ["rules"], with_rules=True)
    write(d / "graders" / "answer.md",
          "---\ntype: llm\n---\n\nPASS if the email puts the request in the first two lines, gives the time in US Eastern time as well as IST, "
          "uses US spelling, writes any date in words (for example 4 Dec 2026) rather than as 04/12, and avoids phrases such as 'do the needful', 'revert back' or 'prepone'. FAIL otherwise.\n")

    # Rule 8: time-sensitive facts are dated or flagged as unverified when search isn't available.
    d = EVALS / "rules" / "dated-regulation-fact"
    prompt(d, "When do the EU AI Act's high-risk obligations start applying to hiring tools?", ["rules"], with_rules=True)
    write(d / "graders" / "answer.md",
          "---\ntype: llm\n---\n\nPASS if the answer gives a date and either states the date of its information or flags that it could not check for recent changes. FAIL if it states a date with no hint of when that was true.\n")

    # Workflow: client-ask runs one phase and stops for approval.
    d = EVALS / "workflows" / "client-ask-stops-after-phase-1"
    prompt(d, "/vi-framework:client-ask A retail client says their store managers spend hours each week reconciling stock reports and wants an AI agent to do it.",
           ["workflow"])
    write(d / "graders" / "asks-approval.md",
          "---\ntype: regex\npattern: 'Approve and move to'\ntarget: last_message\narm: with-only\n---\n")
    write(d / "graders" / "one-phase-only.md",
          "---\ntype: tool_used\ntool: Skill\ninput_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?(ai-fit-check|business-case)\"'\nmin: 0\nmax: 0\narm: with-only\n---\n")

    builder = ROOT / "builder" / "evals"
    for child in builder.glob("*") if builder.exists() else []:
        if child.name != "results":
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    for name, skill, text, specific in BUILDER_CASES:
        d = builder / "skills" / name
        prompt(d, text, ["skill", skill])
        skill_fired(d, skill)
        common_graders(d, specific)

    print(f"wrote {len(CASES) + len(NEGATIVE) + 4} cases, plus {len(BUILDER_CASES)} builder cases")


if __name__ == "__main__":
    main()
