import smtplib
from datetime import datetime
from unittest import mock

import pytest

import renom
from conftest import canvia_titol, commit_sveltia, git

ARA = datetime(2026, 11, 17, 14, 3)


def resultat(repo, camí, nou, tipus_commit, slug=None):
    base = git(repo, "rev-parse", "HEAD")
    canvia_titol(repo, camí, nou)
    commit_sveltia(repo, tipus_commit, slug or camí.split("/")[-1])
    ev = renom.detecta_renoms(repo, base, "HEAD")[0]
    return renom.aplica_esdeveniment(repo, ev)


def registre(repo):
    return (repo / ".ai/REGISTRE-CANVIS-FITXES.md").read_text(encoding="utf-8")


def test_registre_afegeix_al_final_sense_tocar_el_previ(repo_prova):
    previ = registre(repo_prova)
    r = resultat(repo_prova, "content/ca/arquitectes/pere-lópez/_index.md", "Pere López Núñez", "Arquitecte")
    assert renom.afegeix_registre(repo_prova, renom.entrada_registre(r), ara=ARA) is True
    nou = registre(repo_prova)
    assert nou.startswith(previ)
    bloc = nou[len(previ):]
    assert "### 2026-11-17 14:03 — renom de arquitecte «Pere López» → «Pere López Núñez»" in bloc
    assert "- **Autor del desament:** xaviglobus (commit `" in bloc
    assert "`/arquitectes/pere-lópez/` → `/arquitectes/pere-lópez-núñez/`" in bloc
    assert "- **Fitxes actualitzades:** 3 (" in bloc
    assert "https://112books.github.io/guiesbarcelona-elglobusvermell/elements/casa-bloc/" in bloc
    assert "- **Resultat:** aplicat" in bloc
    assert "- **Aprovació:** automàtic — regla aprovada per Joan 17/11/2026" in bloc


def test_registre_idempotent_per_sha(repo_prova):
    r = resultat(repo_prova, "content/ca/arquitectes/pere-lópez/_index.md", "Pere López Núñez", "Arquitecte")
    e = renom.entrada_registre(r)
    assert renom.afegeix_registre(repo_prova, e, ara=ARA)
    una = registre(repo_prova)
    assert renom.afegeix_registre(repo_prova, e, ara=ARA) is False
    assert registre(repo_prova) == una


def test_registre_refus_amb_motiu(repo_prova):
    r = resultat(repo_prova, "content/ca/arquitectes/rebecca-horn/_index.md", "Pere López", "Arquitecte")
    assert r.estat == "refusat"
    renom.afegeix_registre(repo_prova, renom.entrada_registre(r), ara=ARA)
    t = registre(repo_prova)
    assert "refús de renom de arquitecte «Rebecca Horn» → «Pere López»" in t
    assert "- **Resultat:** refusat (ja existeix un arquitecte amb el nom «Pere López»" in t
    assert "s'ha revertit el títol a «Rebecca Horn»" in t


def test_registre_escapa_markdown(repo_prova):
    r = resultat(repo_prova, "content/ca/arquitectes/pere-lópez/_index.md", "Pere | López *Núñez*", "Arquitecte")
    renom.afegeix_registre(repo_prova, renom.entrada_registre(r), ara=ARA)
    assert "«Pere \\| López \\*Núñez\\*»" in registre(repo_prova)


def test_registre_conflicte_idempotent(repo_prova):
    e = {"tipus": "conflicte", "clau": "abcdef1", "detall": ["L'adreça /elements/x/ és alhora …"]}
    assert renom.afegeix_registre(repo_prova, e, ara=ARA)
    assert not renom.afegeix_registre(repo_prova, e, ara=ARA)
    assert "conflicte detectat" in registre(repo_prova)


# ---------------- correu ----------------

ENV = {"SMTP_HOST": "smtp.exemple.org", "SMTP_PORT": "587", "SMTP_USER": "usuari",
       "SMTP_PASSWORD": "contrasenya-falsa-123", "AVIS_DESTINATARIS": "a@exemple.org, b@exemple.org"}


def test_avis_cos_amb_urls_sencers_i_frase_de_recarrega(repo_prova):
    r = resultat(repo_prova, "content/ca/arquitectes/pere-lópez/_index.md", "Pere López Núñez", "Arquitecte")
    assumpte, cos = renom.compon_avis(r)
    assert assumpte == "Canvi de nom aplicat: arquitecte «Pere López» → «Pere López Núñez»"
    assert "https://112books.github.io/guiesbarcelona-elglobusvermell/arquitectes/pere-l%C3%B3pez-n%C3%BA%C3%B1ez/" in cos
    assert "https://112books.github.io/guiesbarcelona-elglobusvermell/arquitectes/pere-l%C3%B3pez/" in cos
    assert "https://112books.github.io/guiesbarcelona-elglobusvermell/elements/casa-bloc/" in cos
    assert "Recarrega l'editor abans de continuar editant." in cos
    # Signatura: banderola ASCII amb el remitent i l'avís d'automatisme.
    assert "LinuxBCN · sistemes i web · webmaster@linuxbcn.com" in cos
    assert "[ avís automàtic ] guiesbarcelona.elglobusvermell.org" in cos
    assert cos.rstrip().endswith("----------------------------------------------------------")


def test_avis_refus_explica_que_fer(repo_prova):
    # el refús que queda és el d'arquitecte (els títols repetits ja no es refusen)
    r = resultat(repo_prova, "content/ca/arquitectes/rebecca-horn/_index.md", "Pere López", "Arquitecte")
    assumpte, cos = renom.compon_avis(r)
    assert assumpte.startswith("No s'ha pogut canviar el nom")
    assert "tria un altre nom" in cos and "desfés el canvi" in cos


def test_avis_alies_eliminat_surt_al_correu(repo_prova):
    p0 = "content/ca/elements/torre-llevant.md"
    r = resultat(repo_prova, p0, "Torre del Llevant", "Edifici")
    r.pla.alies_eliminats.append("/elements/x/")
    assert "s'ha tret la redirecció /elements/x/" in renom.compon_avis(r)[1]


def test_envia_avis_amb_smtp_simulat():
    smtp = mock.MagicMock()
    classe = mock.MagicMock(return_value=smtp)
    assert renom.envia_avis("Assumpte", "Cos", env=ENV, smtp_classe=classe) == 0
    classe.assert_called_once_with("smtp.exemple.org", 587, timeout=30)
    smtp.starttls.assert_called_once()
    smtp.login.assert_called_once_with("usuari", "contrasenya-falsa-123")
    msg = smtp.send_message.call_args.args[0]
    assert msg["From"] == "webmaster@linuxbcn.com"
    assert msg["To"] == "a@exemple.org, b@exemple.org" and msg["Subject"] == "Assumpte"
    assert smtp.send_message.call_args.kwargs["to_addrs"] == ["a@exemple.org", "b@exemple.org"]
    assert "contrasenya-falsa-123" not in msg.as_string()


def test_envia_avis_ssl_port_465():
    smtp = mock.MagicMock()
    ssl = mock.MagicMock(return_value=smtp)
    renom.envia_avis("A", "B", env={**ENV, "SMTP_PORT": "465"}, smtp_ssl_classe=ssl)
    ssl.assert_called_once()
    smtp.starttls.assert_not_called()


def test_envia_avis_error_smtp_torna_zero_i_va_a_stderr(capsys):
    classe = mock.MagicMock(side_effect=smtplib.SMTPException("ha fallat amb contrasenya-falsa-123"))
    assert renom.envia_avis("A", "B", env=ENV, smtp_classe=classe) == 0
    err = capsys.readouterr().err
    assert "no enviat" in err and "SMTPException" in err
    assert "contrasenya-falsa-123" not in err      # mai la contrasenya als logs


def test_envia_avis_sense_secrets_s_omet(capsys):
    assert renom.envia_avis("A", "B", env={}) == 0
    assert "omès" in capsys.readouterr().err


def test_cos_no_conte_la_contrasenya(repo_prova):
    r = resultat(repo_prova, "content/ca/elements/casa-bloc.md", "Casa Bloc Nova", "Edifici")
    assert ENV["SMTP_PASSWORD"] not in "".join(renom.compon_avis(r))
