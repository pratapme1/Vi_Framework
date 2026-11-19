# Vi_Framework

My skills for product work: understanding problems, shaping ideas, writing specs, planning, and writing clean. They work in Claude chat and in the terminal (Claude Code).

See [HOUSE_RULES.md](HOUSE_RULES.md) for the rules every skill follows. To change them, edit that file and run `python3 scripts/sync_house_rules.py`; add `--check` to confirm nothing has drifted.

## Skills

| Skill | Use it to |
|---|---|
| problem-framing | Find the real problem behind a request |
| outcome-definition | Define measurable outcomes, metrics and guardrails |
| idea-refine | Shape and pressure-test an idea |
| ai-fit-check | Decide whether a problem needs AI, and how much |
| ai-system-design | Choose the architecture, costs and risks of an AI system |
| eval-design | Design evals so you know an AI system works |
| synthetic-data | Create realistic test and demo data safely |
| spec-driven-development | Write a spec or PRD before building |
| planning-and-task-breakdown | Break work into small, ordered tasks |
| exec-presentation | Build an answer-first deck that gets a decision |
| client-qa | Prepare and rehearse tough client questions |
| stakeholder-influence | Win honest support for a decision |
| pm-review | Brutally review any PM document before it goes out |
| humanizer | Remove AI patterns from writing |

## Install in the terminal (Claude Code)

```
/plugin marketplace add pratapme1/Vi_Framework
/plugin install vi-framework@vi-framework
```

To get updates later: `/plugin marketplace update vi-framework`

## Use in Claude chat

Save each skill to your Claude account so chat and terminal use the same version.

## Credits

- idea-refine, spec-driven-development, planning-and-task-breakdown: adapted from [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (MIT)
- humanizer: adapted from [blader/humanizer](https://github.com/blader/humanizer) (MIT)
