# Informe — jornada del 17/11/2026

**Data:** 17/11/2026
**Autoria:** Joan (LinuxBCN) amb assistència d'IA
**Context:** dues sessions. Matí (11:59–13:45): disseny, pla i implementació del renom automàtic de fitxes i arquitectes, i publicació a `main`. Tarda (13:50–17:15): arreglo del bug de «&», prova real del renom, decisió de Xavi sobre els tipus d'intervenció, signatura dels avisos i tancament.
**Commits (repo públic):** `cd861a1d`, `85d462b9` (renom), `1920fc77` (bug de «&»), `274649ce` (tauler), `badcfb30` («Nom i ús actual»), `4ef8af40` (informe del «&»), `ea94908b` → `ac07a27f` (prova real), `dbadf69a` → `67caefa2` (reversió), `b57717a3` (neteja de l'àlies de prova), `bee07409` (tauler), `b4fe05d7` (signatura i `clean_accents`).

---

## 1. Què s'ha fet

### 1.1 Renom automàtic de fitxes i arquitectes (matí)

Quan es canvia el `title` d'una fitxa o d'un arquitecte des de l'editor, un pas nou del workflow de desplegament (`scripts/renom.py`, abans de Hugo) ho deixa coherent: mou l'arxiu o la carpeta, afegeix l'adreça antiga a `aliases`, propaga el nom nou de l'arquitecte a totes les fitxes (`arquitectes:` i `intervencions[].autors`) i a `data/arquitectes-bio-extra.yaml`, ho apunta a `.ai/REGISTRE-CANVIS-FITXES.md` i envia un avís per correu. 116 tests. Detall complet al full de ruta i al log de tasques del dia.

### 1.2 Bug de «&» a les pàgines d'arquitecte (`1920fc77`)

Detall a `.ai/informe-bug-ampersand-2026-11-17.md`. En resum: Hugo creava dos nodes per a la mateixa adreça (el terme de la taxonomia i un node derivat de la carpeta) i, segons l'ordre intern, publicava el de la carpeta, de manera que ~50% de les compilacions deixaven la pàgina sense edificis ni mapa (es veia en producció a Arriola & Fiol i a SV60). Arreglat a la plantilla, verificar amb sis compilacions seguides.

### 1.3 Prova real del renom, amb còpia prèvia

Còpia prèvia: tag `backup/abans-prova-renom-20261117` i el fitxer a `docs/.taques/prova-renom-2026-11-17/`. Assaig local en una branca temporal amb `--no-push` i després prova real a `main` amb la fitxa «Jardins de Sofia Barat» → «Jardins de Sofia Barat (prova)». Resultats: correu enviat, robot amb commit i push (`ac07a27f`), adreça nova 200, adreça antiga i l'àlies del plànol en paper redirigint a la nova. Reversió (`dbadf69a` → `67caefa2`) i neteja de l'àlies de prova (`b57717a3`): la fitxa queda **idèntica byte a byte** a la còpia prèvia i l'adreça de prova torna 404. Al tauler hi ha una fitxa que explica els dos correus que rep en Xavi.

### 1.4 Tipus d'intervenció: «Nom i ús actual» (`badcfb30`)

Decisió d'en Xavi: els dos tipus «Ús actual» i «Nom actual» passen a ser un de sol, «Nom i ús actual», i la llista ha de ser **tancada i ampliable, no lliure** (si en falta un, ens ho diu i l'afegim). Canviats el desplegable de l'editor (amb l'ajuda corresponent) i la condició de la plantilla que amaga la fila «Arquitectes». Cap fitxa en feia servir cap, el web no canvia. Resposta enregistrada al tauler.

### 1.5 Signatura dels avisos i noms d'arxiu sense accents (`b4fe05d7`)

- Els avisos per correu acaben amb una banderola ASCII d'estil administració de sistemes: `LinuxBCN · sistemes i web · webmaster@linuxbcn.com`, `[ avís automàtic ] guiesbarcelona.elglobusvermell.org` i el nom de l'script. Sense l'adreça `hola@linuxbcn.com`.
- Editor: bloc global `slug: { clean_accents: true }` perquè les fitxes noves neixin amb nom d'arxiu ASCII, com les 658 que ja hi ha. No renombra res d'existent.
- Es va provar d'alinear `slug_fitxa` amb Sveltia caràcter a caràcter i es va descartar: obligava a acceptar 135 noms antics com a excepcions i hauria fet noms d'arxiu amb «» i · al mig. Diferència que queda, documentada al codi: amb un apòstrof, Sveltia fa un guió (`ca-l-alier`) i aquí s'elimina (`ca-lalier`); és cosmètica.

### 1.6 Tauler de revisió al dia

Tres «fets» nous (bug de «&», renom provat de punta a punta, «Nom i ús actual») i una decisió nova per a Xavi («Clotet, Paricio & Associats» surt sense edificis perquè a la fitxa de l'edifici el nom és «Clotet-Paricio»). La decisió dels tipus d'intervenció queda amb la resposta rebuda.

## 2. Verificacions

| Què | Resultat |
|---|---|
| Deploy → GitHub Pages i Accessibilitat (pa11y-ci) | en verd en tots els commits publicats avui |
| Pàgines d'arquitecte amb «&» | 6 compilacions seguides estables (Arriola 2, Prince Smith 1, SV60 1, A&EB 1) |
| Prova real del renom | correu, adreça nova, redirecció i reversió comprovats en viu |
| Tests del renom | 116 en verd |
| Totals de compilació | 1315 pàgines i 768 àlies, sense canvis |

## 3. Pendent

- **Esperant Xavi**: «Clotet, Paricio & Associats» (és el mateix estudi que «Clotet-Paricio»?) i la resta de dubtes del tauler.
- **Neteja opcional**: les branques locals `feat/renom-automatic` i `feat/renom-revisio` ja són a `main` i es poden esborrar. La branca `prova-correu` i el worktree orfe de la sessió del matí ja s'han tret.
- **Signatura dels avisos**: si en Joan la vol més curta o amb un altre to, es canvia en un sol lloc (`compon_avis`, `peu`).
- Recordatori: el desplegament de producció del domini encara és el WordPress; el web nou es valida a `https://112books.github.io/guiesbarcelona-elglobusvermell/` fins al tall.

## 4. Hores

| Bloc | Hores | Tasques |
|---|---|---|
| Matí (11:59–13:45) | 1h 46 | 8 |
| Tarda (13:50–17:15, amb pauses) | 2h 56 | 7 |
| **Total** | **4h 42** | **15** |

Detall tasca a tasca a `docs/.taques/guia-globus-vermell/2026-11-17.md` (repo privat).
