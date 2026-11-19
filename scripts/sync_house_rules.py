"""Copy the house rules from HOUSE_RULES.md into every skill and output style.

Usage:
    python3 scripts/sync_house_rules.py          # update all files
    python3 scripts/sync_house_rules.py --check  # fail if any file has drifted
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"<!-- house-rules:start -->.*?<!-- house-rules:end -->", re.S)

canonical = BLOCK.search((ROOT / "HOUSE_RULES.md").read_text()).group(0)
check = "--check" in sys.argv
targets = (sorted((ROOT / "skills").glob("*/SKILL.md")) + sorted((ROOT / "builder" / "skills").glob("*/SKILL.md"))
           + sorted((ROOT / "output-styles").glob("*.md")))
bad = []

for path in targets:
    label = path.relative_to(ROOT)
    text = path.read_text()
    if not BLOCK.search(text):
        bad.append(f"{label}: no house-rules markers")
        continue
    new = BLOCK.sub(lambda _: canonical, text)
    if new != text:
        if check:
            bad.append(f"{label}: house rules differ from HOUSE_RULES.md")
        else:
            path.write_text(new)
            print(f"updated {label}")

if bad:
    print("\n".join(bad))
    sys.exit(1)
print(f"all {len(targets)} files in sync")
