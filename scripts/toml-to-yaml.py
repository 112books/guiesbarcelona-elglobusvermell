#!/usr/bin/env python3
"""
Migra fitxers Markdown amb frontmatter TOML (+++) a frontmatter YAML (---).
Gestiona [[intervencions]] i altres llistes de diccionaris.

Ús: python3 scripts/toml-to-yaml.py [--dry-run] [--limit N]
"""

import sys
import re
import tomllib
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pip install pyyaml")
    sys.exit(1)

# Camps numèrics guardats com a string al TOML que cal convertir a float/int
TO_FLOAT = {"lat", "long"}
TO_INT   = {"superficie"}


def coerce(data: dict) -> dict:
    for k in TO_FLOAT:
        if k in data and isinstance(data[k], str):
            try:
                data[k] = float(data[k])
            except ValueError:
                pass
    for k in TO_INT:
        if k in data and isinstance(data[k], str):
            try:
                data[k] = int(data[k])
            except ValueError:
                pass
    return data


def to_yaml_block(data: dict) -> str:
    return yaml.dump(data, allow_unicode=True, default_flow_style=False,
                     sort_keys=False).rstrip()


def convert_file(path: Path, dry_run: bool = False) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("+++"):
        return False

    end = text.find("+++", 3)
    if end == -1:
        print(f"  AVÍS: {path.name} — no es troba el tancament +++, saltat")
        return False

    toml_str = text[3:end].strip()
    body = text[end + 3:].lstrip("\n")

    # Elimina comentaris TOML (línies que comencen per #) per facilitar parsing
    toml_clean = re.sub(r"^\s*#.*$", "", toml_str, flags=re.MULTILINE)

    try:
        data = tomllib.loads(toml_clean)
    except tomllib.TOMLDecodeError as e:
        print(f"  ERROR TOML a {path.name}: {e}")
        return False

    data = coerce(data)
    yaml_block = to_yaml_block(data)

    new_text = f"---\n{yaml_block}\n---\n"
    if body:
        new_text += f"\n{body}\n"

    if new_text == text:
        return False

    if dry_run:
        print(f"\n── {path.name} {'─'*40}")
        print(new_text[:500])
    else:
        path.write_text(new_text, encoding="utf-8")

    return True


def main():
    dry_run = "--dry-run" in sys.argv
    limit = 0
    if "--limit" in sys.argv:
        idx = sys.argv.index("--limit")
        limit = int(sys.argv[idx + 1])

    repo_root = Path(__file__).parent.parent
    elements_dir = repo_root / "content" / "ca" / "elements"

    if not elements_dir.exists():
        print(f"ERROR: No es troba {elements_dir}")
        sys.exit(1)

    files = sorted(elements_dir.glob("*.md"))
    toml_files = [f for f in files if f.read_text(encoding="utf-8").startswith("+++")]

    mode = "DRY RUN — " if dry_run else ""
    print(f"\n{mode}Migrant frontmatter TOML → YAML")
    print(f"Fitxers TOML: {len(toml_files)}")
    if limit:
        toml_files = toml_files[:limit]
        print(f"Limitant a:   {limit}")
    print()

    converted = errors = 0
    for f in toml_files:
        try:
            if convert_file(f, dry_run=dry_run):
                converted += 1
                if not dry_run:
                    print(f"  ✓ {f.name}")
        except Exception as e:
            errors += 1
            print(f"  ✗ {f.name}: {e}")

    print(f"\nResultat: {converted} convertits, {errors} errors")
    if dry_run:
        print("Executa sense --dry-run per aplicar els canvis.")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
