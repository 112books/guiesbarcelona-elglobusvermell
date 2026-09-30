# T07 — Eliminar el bloc "Suggerir una correcció" de la Presentació

**Data:** 2026-09-30
**Estat:** Aprovat per Joan — pendent de validació Xavi

## 1. Tasca demanada

> "Eliminar bloc 'Suggerir un canvi'."

Font: feedback Xavi 30/9/2026, secció PRESENTACIÓ (PR4). Handoff T07.

## 2. Solució prevista

Treure la inclusió del partial formulari-correccio.html de la pàgina Presentació. El client el descriu com "Suggerir un canvi"; el partial porta el títol "Suggerir una correcció".

## 3. Estat de l'execució

Implementat el 2026-09-30. Build Hugo OK. Pendent d'aprovació abans de commit.

## 4. Fitxers modificats

### themes/guiesbcn-elglobusvermell/layouts/presentacio/list.html

Eliminada la línia:

    {{ partial "formulari-correccio.html" . }}

## 5. Resultat final

La pàgina Presentació ja no mostra el formulari de suggeriment de correcció. Es manté a /contacte/, que és el lloc natural per a correccions (PR4 és específic de la Presentació).

## 6. Aprovació

Pendent de revisió Joan i validació Xavi.

---

**Nota de criteri:** si el client vol eliminar també el formulari de /contacte/, caldrà fer-ho conjuntament amb la reescriptura del formulari únic (C1).
