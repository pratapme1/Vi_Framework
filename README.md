# Vi_Framework

My skills for consulting product work on AI: understanding the real problem, sizing value, deciding whether AI fits, designing and testing AI systems, writing proposals, communicating with partners and clients, and leading a team. They work in Claude chat and in the terminal (Claude Code).

Every skill follows the same [house rules](HOUSE_RULES.md): coach rather than replace, one recommendation, short and plain writing, honest and labelled claims, client data protected, and written for the reader's seniority and location.

## Skills

| Skill | Use it to |
|---|---|
| discovery | Plan, run and synthesise interviews and workshops |
| problem-framing | Find the real problem behind a request, with an issue tree when it's big |
| outcome-definition | Define measurable outcomes, metrics and guardrails |
| business-case | Size value, cost, payback and risk |
| idea-refine | Generate and pressure-test options for a known problem |
| ai-fit-check | Decide whether a problem needs AI, and how much |
| ai-system-design | Choose the architecture, cost and risks of an AI system |
| eval-design | Plan evals and a ship bar for an AI system |
| synthetic-data | Create realistic test and demo data safely |
| responsible-ai-review | Check regulatory, data, fairness and oversight risks (EU, UK, US, India) |
| spec-driven-development | Write a spec or PRD once a direction is chosen |
| planning-and-task-breakdown | Break work into tasks or a week-by-week workplan |
| proposal-and-sow | Write a proposal, statement of work or change request |
| exec-presentation | Build an answer-first deck or decision memo |
| client-qa | Answer or rehearse tough client questions |
| stakeholder-influence | Win honest support for a decision |
| status-and-escalation | Write status updates, steering one-pagers and escalations |
| team-leadership | Delegation briefs, feedback, 1:1s and coaching your team's work |
| pm-review | Brutally review any document before it goes out |
| humanizer | Remove AI patterns from text you've written |

## Workflows

Run several skills in order. Each pauses for your approval after every phase. In the terminal, they ask before saving each phase to `~/vi-work/<project>/`, outside your client repositories.

| Command (terminal) | Runs |
|---|---|
| `/vi-framework:client-ask` | Problem framing (with discovery questions if facts are thin), AI fit check, business case, then a summary for your engagement lead |
| `/vi-framework:ai-solution` | AI system design, eval design, responsible AI review, then a short spec |
| `/vi-framework:meeting-prep` | Stakeholder map, storyline, Q&A rehearsal, then a 30-second version |

In chat, ask for them by name, for example "run the client-ask workflow on this".

## Install in the terminal (Claude Code)

```
/plugin marketplace add pratapme1/Vi_Framework
/plugin install vi-framework@vi-framework
```

To get updates: `/plugin marketplace update vi-framework`, then restart Claude Code.

## Turn on the house rules for every answer (terminal)

The plugin ships an output style that applies the house rules to every reply, not only when a skill runs. Plugin styles are named `<plugin>:<style>`, so in each project run:

```
/output-style vi-framework:Vi
```

That command saves the choice for the current project only. To make it the default everywhere, add this to `~/.claude/settings.json` (the name is case-sensitive):

```json
{ "outputStyle": "vi-framework:Vi" }
```

## Use in Claude chat

1. Run `python3 scripts/export_for_chat.py`. It writes chat-ready copies to `dist/chat/`, removing terminal-only settings that chat uploads reject.
2. Zip each skill folder and upload it in Claude's skill settings, or ask Claude in chat to save the skill for you.
3. Paste the short form of the house rules into your Claude personal preferences, so plain chats follow them too.

Use these skills with client data only in a workspace your firm has approved for client work.

## Recommended companions (terminal)

These do specialist jobs better than this kit, so use them alongside it rather than rebuilding them:

- [hamelsmu/evals-skills](https://github.com/hamelsmu/evals-skills): hands-on eval work (error analysis, judge prompts, judge validation). `/plugin marketplace add hamelsmu/evals-skills`
- [obra/superpowers](https://github.com/obra/superpowers): coding discipline (test-driven development, debugging, code review). Enable it only in coding projects, because its brainstorming skill competes with problem-framing and idea-refine.

## Test the kit

`evals/` holds test cases for `claude plugin eval` (Claude Code 2.1.269 or later). Skill cases check what each skill adds against Claude without the plugin; whether the right skill fired is shown as an indicator in the report. Rule cases check the house rules as the output style delivers them. Every run uses your own Claude usage.

```
# skill cases, compared with no plugin (start here)
claude plugin eval . --tag skill --runs 1 --judge-model sonnet --threshold 0.8

# routing, workflow and rule cases, where the plugin firing is the point
claude plugin eval . --tag routing --tag workflow --tag rules --ablation none --judge-model sonnet

# the client-data case, which needs web search granted (run it on its own)
claude plugin eval . --tag rule9 --allow-tools WebSearch --ablation none --judge-model sonnet
```

## Maintaining the kit

- House rules live in `HOUSE_RULES.md` only. After editing, run `python3 scripts/sync_house_rules.py`, and `--check` to confirm every skill and the output style match.
- Test cases are generated from `scripts/build_evals.py`. Edit the table there and rerun it.
- Bump `version` in `.claude-plugin/plugin.json` on every change, or `/plugin marketplace update` won't pick it up.

## Credits

- idea-refine, spec-driven-development, planning-and-task-breakdown: adapted from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT)
- humanizer: adapted from [blader/humanizer](https://github.com/blader/humanizer) (MIT)
