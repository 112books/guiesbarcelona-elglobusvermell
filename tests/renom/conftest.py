"""Fixtures per als tests de scripts/renom.py: repo git de prova dins de tmp_path."""
import os
import subprocess
import sys
from pathlib import Path

import pytest

ARREL_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARREL_REPO / "scripts"))

SVELTIA_NOM = "xaviglobus"
SVELTIA_EMAIL = "xavirg@elglobusvermell.org"

REGISTRE_CAPCALERA = """# Registre de canvis de fitxes i punts dels mapes

**Regla de governança (aprovada per Joan, 31 ago 2026):** cap creació, esborrat o modificació
de fitxes o punts dels mapes sense **aprovació expressa de Joan** i entrada a aquest registre.

---

## Registre de canvis

| Canvi | Motiu | Estat |
|---|---|---|
| exemple | exemple | ok |
"""

FITXES = {
    # indentació 0, aliases inline, 'Pere López' també citat
    "casa-bloc": '''---
aliases: ["/avantguarda-1928-1938/casa-bloc/"]
adreca: Passeig de Torras i Bages
descripcio: |-
  Autoria: Josep Lluís Sert. Pere López Íñigo hi va col·laborar.
arquitectes:
- Josep Lluís Sert
- Pere López
draft: false
foto: /img/elements/casa-bloc.jpg
title: Casa Bloc
---
''',
    # indentació 2, cometes dobles, aliases en bloc
    "torre-llevant": '''---
aliases:
  - /barris/torre-llevant/
  - /torre-llevant-antic/
arquitectes:
  - "Arriola & Fiol Arquitectes"
  - "Josep Lluís Sert"
title: Torre Llevant
---
''',
    # sense aliases, intervencions[].autors amb cometes simples, indentació 4
    "lestel-ferit": '''---
adreca: Platja de la Barceloneta
descripcio: |-
  Autoria: Rebecca Horn. 1992
arquitectes:
- Rebecca Horn
- Sense Carpeta Uno
intervencions:
- any: '1992'
  autors:
    - 'Rebecca Horn'
    - 'Pere López'
  tipus: Autoria
foto: /img/elements/lestel-ferit.jpg
title: «L’estel ferit»
---
''',
    # excepció preexistent: nom d'arxiu ≠ slug del títol
    "biblioteca-vall-d-hebron": '''---
aliases: ["/biblioteques/vall-d-hebron/"]
arquitectes:
- Pere López Íñigo
title: Biblioteca Vall d'Hebron
---
''',
    "mixta": '''---
arquitectes:
- Pere López Íñigo
- Pere López
- Arriola & Fiol Arquitectes
title: Mixta
---
''',
}

ARQUITECTES = {
    "josep-lluís-sert": ("Josep Lluís Sert", ""),
    "pere-lópez-i-íñigo": ("Pere López Íñigo", "aliases:\n  - /vell/pere-lopez-inigo/\n"),
    "pere-lópez": ("Pere López", ""),
    "arriola--fiol-arquitectes": (
        "Arriola & Fiol Arquitectes",
        "aliases:\n  - /arquitectes/arriola-fiol-arquitectes/\n",
    ),
    "rebecca-horn": ("Rebecca Horn", ""),
}

BIO_EXTRA = """# Bio/enllaços per a termes d'arquitecte.
# terme: ha de coincidir EXACTAMENT amb el nom canònic.

- terme: "Arriola & Fiol Arquitectes"
  tipus: estudi
  link_web: "https://arriolafiol.com/"
"""

MAPA = """---
title: "Mapa"
aliases: ["/elements/", "/mapa-grisos/"]
---
Vegeu [Casa Bloc](/elements/casa-bloc/) al mapa.
"""


def git(repo, *args, env=None, check=True):
    e = dict(os.environ)
    e.update({"GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_SYSTEM": "/dev/null"})
    if env:
        e.update(env)
    r = subprocess.run(["git", "-C", str(repo), "-c", "core.quotepath=false", *args],
                       capture_output=True, text=True, encoding="utf-8", env=e)
    if check and r.returncode != 0:
        raise RuntimeError(f"git {args} ha fallat: {r.stderr}")
    return r.stdout.strip()


def escriu(repo, camí, text):
    p = Path(repo) / camí
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def commit(repo, missatge, autor=("Joan Mz Linux", "joan@example.org")):
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", missatge,
        env={"GIT_AUTHOR_NAME": autor[0], "GIT_AUTHOR_EMAIL": autor[1],
             "GIT_COMMITTER_NAME": autor[0], "GIT_COMMITTER_EMAIL": autor[1]})
    return git(repo, "rev-parse", "HEAD")


def commit_sveltia(repo, tipus, slug, extra=""):
    """Commit tal com el fa Sveltia: `Update Edifici “slug”`, autor xaviglobus."""
    return commit(repo, f"Update {tipus} “{slug}”{extra}", autor=(SVELTIA_NOM, SVELTIA_EMAIL))


def canvia_titol(repo, camí, nou, escrit=None):
    """Canvia només la línia `title:` d'una fitxa."""
    p = Path(repo) / camí
    llistes = p.read_text(encoding="utf-8").split("\n")
    for i, l in enumerate(llistes):
        if l.startswith("title:"):
            llistes[i] = f"title: {nou}"
            break
    p.write_text("\n".join(llistes), encoding="utf-8")


@pytest.fixture
def repo_prova(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.name", "Joan Mz Linux")
    git(repo, "config", "user.email", "joan@example.org")
    for stem, text in FITXES.items():
        escriu(repo, f"content/ca/elements/{stem}.md", text)
    escriu(repo, "content/ca/elements/_index.md", '---\ntitle: "Elements"\n---\n')
    for carpeta, (titol, extra) in ARQUITECTES.items():
        escriu(repo, f"content/ca/arquitectes/{carpeta}/_index.md",
               f"---\n{extra}title: {titol}\ntipus: persona\n---\n")
    escriu(repo, "content/ca/arquitectes/_index.md", '---\ntitle: "Arquitectes"\n---\n')
    escriu(repo, "content/ca/mapa/_index.md", MAPA)
    escriu(repo, "data/arquitectes-bio-extra.yaml", BIO_EXTRA)
    escriu(repo, ".ai/REGISTRE-CANVIS-FITXES.md", REGISTRE_CAPCALERA)
    commit(repo, "chore: estat inicial de prova")
    return repo


@pytest.fixture
def remot_bare(tmp_path, repo_prova):
    """Remot bare amb l'estat actual del repo de prova, configurat com a `origin`."""
    remot = tmp_path / "remot.git"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(remot)], check=True)
    git(repo_prova, "remote", "add", "origin", str(remot))
    git(repo_prova, "push", "-q", "origin", "main")
    return remot
