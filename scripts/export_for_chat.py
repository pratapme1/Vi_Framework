"""Make chat-ready copies of every skill in dist/chat/<skill>/SKILL.md.

Claude chat accepts fewer frontmatter fields than Claude Code, so this drops
terminal-only fields such as disable-model-invocation. Workflow skills keep
their "Use only when the user asks to run..." description so they don't fire
on their own.

Run: python3 scripts/export_for_chat.py
"""
import pathlib
import re
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "chat"
CHAT_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}

shutil.rmtree(OUT, ignore_errors=True)
for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = skill.read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    kept = [line for line in match.group(1).splitlines()
            if line.split(":", 1)[0].strip() in CHAT_FIELDS or line.startswith((" ", "\t"))]
    out = OUT / skill.parent.name / "SKILL.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("---\n" + "\n".join(kept) + "\n---\n" + text[match.end():])
    print(f"exported {skill.parent.name}")
