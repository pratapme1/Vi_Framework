# Vi_Framework

My skills for product work: understanding problems, shaping ideas, writing specs, planning, and writing clean. They work in Claude chat and in the terminal (Claude Code).

See [HOUSE_RULES.md](HOUSE_RULES.md) for the rules every skill follows. To change them, edit that file and run `python3 scripts/sync_house_rules.py`; add `--check` to confirm nothing has drifted.

## Skills

| Skill | Use it to |
|---|---|
| discovery | Plan, run and synthesise interviews and workshops |
| problem-framing | Find the real problem behind a request |
| outcome-definition | Define measurable outcomes, metrics and guardrails |
| business-case | Size value, cost, payback and risk |
| idea-refine | Shape and pressure-test an idea |
| ai-fit-check | Decide whether a problem needs AI, and how much |
| ai-system-design | Choose the architecture, costs and risks of an AI system |
| eval-design | Design evals so you know an AI system works |
| synthetic-data | Create realistic test and demo data safely |
| responsible-ai-review | Check regulatory, data, fairness and oversight risks |
| spec-driven-development | Write a spec or PRD before building |
| planning-and-task-breakdown | Break work into small, ordered tasks |
| exec-presentation | Build an answer-first deck that gets a decision |
| client-qa | Prepare and rehearse tough client questions |
| stakeholder-influence | Win honest support for a decision |
| proposal-and-sow | Write a client proposal or statement of work |
| pm-review | Brutally review any PM document before it goes out |
| humanizer | Remove AI patterns from writing |

## Workflows

Type these to run several skills in order. Each pauses for your approval after every phase, and in the terminal saves each phase to `vi-work/<project>/`.

| Command | Runs |
|---|---|
| `/vi-framework:client-ask` | Problem framing, AI fit check, business case, then a summary for your engagement lead |
| `/vi-framework:ai-solution` | AI system design, eval design, responsible AI review, then a short spec |
| `/vi-framework:meeting-prep` | Stakeholder map, storyline, Q&A rehearsal, then a 30-second version |

## Install in the terminal (Claude Code)

```
/plugin marketplace add pratapme1/Vi_Framework
/plugin install vi-framework@vi-framework
```

To get updates later: `/plugin marketplace update vi-framework`

## Turn on the house rules for every answer (terminal)

The plugin ships an output style called **Vi** that applies the house rules to every reply, not only when a skill runs. Turn it on once:

```
/output-style Vi
```

To make it your default in every project, add `"outputStyle": "Vi"` to `~/.claude/settings.json`. Restart Claude Code after installing or updating the plugin so it picks up the style.

## Recommended companions (terminal)

These do specialist jobs better than this kit, so use them alongside it rather than rebuilding them:

- [hamelsmu/evals-skills](https://github.com/hamelsmu/evals-skills): hands-on eval work (error analysis, judge prompts, judge validation). `/plugin marketplace add hamelsmu/evals-skills`
- [obra/superpowers](https://github.com/obra/superpowers): coding discipline (test-driven development, debugging, code review). Enable it only in coding projects, because its brainstorming skill competes with problem-framing and idea-refine.

## Test the kit

`evals/` holds test cases for `claude plugin eval` (Claude Code 2.1.269 or later). Each case checks that the right skill fires and that the house rules hold, and compares against Claude without the plugin. Runs use your own Claude usage.

```
claude plugin eval .                 # all cases, 3 runs each with and without the plugin
claude plugin eval . --runs 1        # quicker, cheaper first pass
claude plugin eval . --allow-tools WebSearch   # needed for the client-data rule case
```

## Use in Claude chat

Save each skill to your Claude account so chat and terminal use the same version.

## Credits

- idea-refine, spec-driven-development, planning-and-task-breakdown: adapted from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT)
- humanizer: adapted from [blader/humanizer](https://github.com/blader/humanizer) (MIT)
