#!/usr/bin/env python3
"""Aplica els 96 reanomenaments automàtics d'arquitectes orfes."""

import json
import re
from pathlib import Path

REPO = Path(__file__).parent.parent
JSON = REPO / ".ai/pla-arquitectes-orfes-2026-11-05.json"
ELEMENTS = REPO / "content/ca/elements"

def apply_rename_in_frontmatter(text: str, old_nom: str, fragments: list) -> tuple:
    """Substitueix old_nom per fragments dins el bloc arquitectes: del frontmatter."""
    targets = [f[0] for f in fragments]

    # Split frontmatter from content
    if not text.startswith("---"):
        return text, False

    parts = text.split("---", 2)
    if len(parts) < 3:
        return text, False

    frontmatter = parts[1]
    content = parts[2]

    # Find arquitectes section
    arch_pattern = re.compile(r'^arquitectes:\n((?:  - .*\n)*)', re.MULTILINE)
    match = arch_pattern.search(frontmatter)
    if not match:
        return text, False

    # Get the arquitectes list
    arch_section = match.group(0)
    arch_lines = match.group(1)

    # Check if the old_nom exists in this list
    if f"- {old_nom}" not in arch_lines:
        return text, False

    # Replace exactly one occurrence
    old_entry = f"  - {old_nom}\n"
    if old_entry not in arch_lines:
        return text, False

    new_entries = "\n".join(f"  - {t}" for t in targets) + "\n"
    new_arch_lines = arch_lines.replace(old_entry, new_entries, 1)
    new_arch_section = f"arquitectes:\n{new_arch_lines}"

    new_frontmatter = frontmatter.replace(arch_section, new_arch_section, 1)
    new_text = f"---{new_frontmatter}---{content}"

    return new_text, True

def main():
    data = json.loads(JSON.read_text())
    resolts = data['resolts']
    changed = 0
    skipped = 0

    for entry in resolts:
        nom = entry['nom']
        fragments = entry['fragments']
        for slug in entry['fitxes']:
            path = ELEMENTS / f"{slug}.md"
            if not path.exists():
                skipped += 1
                continue

            original = path.read_text()
            updated, found = apply_rename_in_frontmatter(original, nom, fragments)

            if found:
                path.write_text(updated)
                targets = [f[0] for f in fragments]
                print(f"  OK: {slug} | '{nom}' → {targets}")
                changed += 1
            else:
                skipped += 1

    print(f"\nTotal: {changed} canvis, {skipped} omissions")

if __name__ == '__main__':
    main()
