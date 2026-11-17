"""Tests de scripts/estampa_tauler.py: data i hora de la darrera actualització del tauler."""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

ARREL_REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ARREL_REPO / "scripts"))

import estampa_tauler as et  # noqa: E402

TAULER = """{
  "actualitzat": "2026-11-17",
  "intro": "text amb el mot actualitzat a dins: 2026-11-17",
  "decisions": [
    {"id": "a", "titol": "«actualitzat» entre cometes"}
  ]
}
"""


def escriu_tauler(carpeta, text=TAULER):
    p = Path(carpeta) / "static" / "admin" / "revisio" / "tasques.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p


# --- conversió de dates ------------------------------------------------------

@pytest.mark.parametrize("entrada,esperat", [
    ("2026-11-17T15:27:00Z", "2026-11-17T16:27"),          # UTC → Madrid (hivern, +1)
    ("2026-11-17T15:27:00+01:00", "2026-11-17T15:27"),     # ja és hora de Madrid
    ("2026-07-01T10:00:00Z", "2026-07-01T12:00"),          # estiu, +2
    ("2026-11-17T15:27", "2026-11-17T15:27"),              # sense zona: es pren com a local
    (" 2026-11-17T15:27:00 +0100 ", "2026-11-17T15:27"),
])
def test_data_iso_local(entrada, esperat):
    assert et.data_iso_local(entrada) == esperat


@pytest.mark.parametrize("brossa", ["", "ahir", "17/11/2026", None])
def test_data_iso_local_rebutja_el_que_no_es_una_data(brossa):
    assert et.data_iso_local(brossa) is None


# --- estampat del fitxer -----------------------------------------------------

def test_estampa_escriu_la_data_i_no_toca_res_mes(tmp_path):
    p = escriu_tauler(tmp_path)
    assert et.estampa(p, "2026-11-17T18:20") is True
    text = p.read_text(encoding="utf-8")
    dades = json.loads(text)
    assert dades["actualitzat"] == "2026-11-17T18:20"
    # el mot «actualitzat» dins dels textos i l'entrada de decisions no es toquen
    assert dades["intro"] == "text amb el mot actualitzat a dins: 2026-11-17"
    assert dades["decisions"] == [{"id": "a", "titol": "«actualitzat» entre cometes"}]
    # només canvia una línia: la resta del fitxer queda byte a byte igual
    assert text == TAULER.replace('"actualitzat": "2026-11-17"', '"actualitzat": "2026-11-17T18:20"')


def test_estampa_sense_camp_actualitzat_no_escriu(tmp_path):
    p = escriu_tauler(tmp_path, '{"intro": "sense camp"}\n')
    assert et.estampa(p, "2026-11-17T18:20") is False
    assert p.read_text(encoding="utf-8") == '{"intro": "sense camp"}\n'


def test_estampa_no_deixa_el_fitxer_en_un_estat_invalid(tmp_path):
    p = escriu_tauler(tmp_path, '{\n  "actualitzat": "2026-11-17",\n')
    with pytest.raises(json.JSONDecodeError):
        et.estampa(p, "2026-11-17T18:20")
    assert p.read_text(encoding="utf-8").startswith('{\n  "actualitzat": "2026-11-17"')


# --- lectura del commit ------------------------------------------------------

def git(repo, *args, env=None):
    entorn = dict(os.environ)
    entorn.update({"GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_SYSTEM": "/dev/null"})
    if env:
        entorn.update(env)
    r = subprocess.run(["git", "-C", str(repo), *args],
                       capture_output=True, text=True, encoding="utf-8", env=entorn, check=False)
    assert r.returncode == 0, r.stderr
    return r.stdout.strip()


@pytest.fixture
def repo_git(tmp_path):
    repo = tmp_path / "repo"
    repo.mkdir()
    git(repo, "init", "-q", "-b", "main")
    git(repo, "config", "user.name", "Joan")
    git(repo, "config", "user.email", "joan@example.org")
    return repo


def test_data_del_commit_agafa_el_darrer_que_va_tocar_el_tauler(repo_git):
    p = escriu_tauler(repo_git)
    git(repo_git, "add", "-A")
    git(repo_git, "commit", "-q", "-m", "primer", env={
        "GIT_AUTHOR_DATE": "2026-11-17T09:00:00+01:00",
        "GIT_COMMITTER_DATE": "2026-11-17T09:00:00+01:00",
    })
    # un commit posterior que NO toca el tauler no ha de comptar
    (repo_git / "altre.txt").write_text("x", encoding="utf-8")
    git(repo_git, "add", "-A")
    git(repo_git, "commit", "-q", "-m", "altre", env={
        "GIT_AUTHOR_DATE": "2026-11-17T20:00:00+01:00",
        "GIT_COMMITTER_DATE": "2026-11-17T20:00:00+01:00",
    })
    assert et.data_del_commit(p, repo_git) == "2026-11-17T09:00"


def test_data_del_commit_sense_commits_retorna_none(repo_git):
    p = escriu_tauler(repo_git)
    assert et.data_del_commit(p, repo_git) is None


def test_data_del_commit_fora_de_git_retorna_none(tmp_path):
    p = escriu_tauler(tmp_path)
    assert et.data_del_commit(p, tmp_path) is None


def test_main_estampa_i_no_falla_mai(tmp_path, capsys):
    repo = tmp_path / "repo"
    repo.mkdir()
    assert et.main(["--repo", str(repo), "--fitxer", str(tmp_path / "no-existeix.json")]) == 0
    assert "deixa com és" in capsys.readouterr().out
