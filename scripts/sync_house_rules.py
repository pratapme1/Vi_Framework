"""Copy the house rules from HOUSE_RULES.md into every skill.

Usage:
    python3 scripts/sync_house_rules.py          # update all skills
    python3 scripts/sync_house_rules.py --check  # fail if any skill has drifted
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"<!-- house-rules:start -->.*?<!-- house-rules:end -->", re.S)

canonical = BLOCK.search((ROOT / "HOUSE_RULES.md").read_text()).group(0)
check = "--check" in sys.argv
bad = []

for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = skill.read_text()
    if not BLOCK.search(text):
        bad.append(f"{skill.parent.name}: no house-rules markers")
        continue
    new = BLOCK.sub(lambda _: canonical, text)
    if new != text:
        if check:
            bad.append(f"{skill.parent.name}: house rules differ from HOUSE_RULES.md")
        else:
            skill.write_text(new)
            print(f"updated {skill.parent.name}")

if bad:
    print("\n".join(bad))
    sys.exit(1)
print("all skills in sync")
