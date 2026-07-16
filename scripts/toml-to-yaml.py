#!/usr/bin/env python3
"""
Migra fitxers Markdown amb frontmatter TOML (+++) a frontmatter YAML (---).
Sveltia CMS té un bug conegut amb la generació de fitxers TOML nous.

Ús: python3 scripts/toml-to-yaml.py [--dry-run]
"""

import sys
import re
import tomllib
from pathlib import Path

# Camps que han de ser strings fins i tot si semblen números (any, lat, long)
FORCE_STRING = {"any", "lat", "long", "superficie"}

# Camps que Hugo espera com a llistes
FORCE_LIST = {"publicacions", "arquitectes", "anys_reforma", "usos_reforma",
              "premis", "temes_transversals"}


def toml_value_to_yaml(key: str, value) -> str:
    """Converteix un valor Python (vingut de TOML) a línia/línies YAML."""
    if isinstance(value, bool):
        return "true" if value else "false"

    if isinstance(value, list):
        if not value:
            return "[]"
        items = "\n".join(f"  - {yaml_quote(str(v))}" for v in value)
        return "\n" + items

    if isinstance(value, (int, float)) and key not in FORCE_STRING:
        return str(value)

    # Strings (i numèrics forçats a string)
    s = str(value)
    return yaml_quote(s)


def yaml_quote(s: str) -> str:
    """Retorna el valor entre cometes si conté caràcters especials YAML."""
    # Necessita cometes si: buit, conté : # & * ? | > ! % @ ` , { } [ ]
    # o comença amb caràcter especial, o és un literal booleà/null
    dangerous = re.compile(r'[:{}\[\],#&*?|>\'\"%@`!]')
    yaml_reserved = {"true", "false", "yes", "no", "null", "~"}
    if not s:
        return '""'
    if s.lower() in yaml_reserved or dangerous.search(s) or s[0] in "-?":
        # Escapa les cometes dobles interiors
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return f'"{escaped}"'
    return s


def convert_file(path: Path, dry_run: bool = False) -> bool:
    """Converteix un fitxer de TOML a YAML. Retorna True si ha canviat."""
    text = path.read_text(encoding="utf-8")

    # Detecta frontmatter TOML
    if not text.startswith("+++"):
        return False  # Ja és YAML o no té frontmatter

    # Separa frontmatter i cos
    end = text.find("+++", 3)
    if end == -1:
        print(f"  AVÍS: {path.name} — no es troba el tancament +++, saltat")
        return False

    toml_str = text[3:end].strip()
    body = text[end + 3:].lstrip("\n")

    # Parseja TOML
    try:
        data = tomllib.loads(toml_str)
    except tomllib.TOMLDecodeError as e:
        print(f"  ERROR TOML a {path.name}: {e}")
        return False

    # Construeix el frontmatter YAML
    lines = ["---"]
    for key, value in data.items():
        yaml_val = toml_value_to_yaml(key, value)
        if yaml_val.startswith("\n"):
            # Llista multilinea
            lines.append(f"{key}:{yaml_val}")
        else:
            lines.append(f"{key}: {yaml_val}")
    lines.append("---")

    yaml_front = "\n".join(lines)
    new_text = yaml_front + "\n"
    if body:
        new_text += body

    if new_text == text:
        return False  # Sense canvis

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return True


def main():
    dry_run = "--dry-run" in sys.argv

    repo_root = Path(__file__).parent.parent
    elements_dir = repo_root / "content" / "ca" / "elements"

    if not elements_dir.exists():
        print(f"ERROR: No es troba {elements_dir}")
        sys.exit(1)

    files = sorted(elements_dir.glob("*.md"))
    converted = 0
    skipped = 0
    errors = 0

    mode = "DRY RUN — " if dry_run else ""
    print(f"\n{mode}Migrant frontmatter TOML → YAML")
    print(f"Directori: {elements_dir}")
    print(f"Fitxers:   {len(files)}\n")

    for f in files:
        try:
            changed = convert_file(f, dry_run=dry_run)
            if changed:
                converted += 1
                tag = "(simulat) " if dry_run else ""
                print(f"  ✓ {tag}{f.name}")
            else:
                skipped += 1
        except Exception as e:
            errors += 1
            print(f"  ✗ {f.name}: {e}")

    print(f"\nResultat: {converted} convertits, {skipped} saltats (ja YAML o sense frontmatter), {errors} errors")

    if dry_run:
        print("\nExecuta sense --dry-run per aplicar els canvis.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
