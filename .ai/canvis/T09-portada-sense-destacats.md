# T09 — Portada: treure guia destacada, arquitecte destacat i recursos educatius

**Data:** 2026-09-30
**Estat:** Aprovat per Joan — pendent de validació Xavi

## 1. Tasca demanada

> "Eliminar: guia destacada, arquitecte destacat, recursos educatius."

Font: feedback Xavi 30/9/2026, secció PÀGINA PRINCIPAL (P5). Handoff T09.

## 2. Solució prevista

Treure les tres seccions de la portada index.html i tot el JavaScript associat (selecció aleatòria de guia/arquitecte i dades PA_GUIES / PA_ARQUITECTES). Es conserven l'hero, "Totes les guies" i el bloc de CTA al mapa.

## 3. Estat de l'execució

Implementat el 2026-09-30. Build Hugo OK. Pendent d'aprovació abans de commit.

## 4. Fitxers modificats

### themes/guiesbcn-elglobusvermell/layouts/index.html

- Eliminada la secció "2. Guia destacada" (amb l'element aleatori i l'enllaç a la guia).
- Eliminada la secció "4. Arquitecte o estudi destacat".
- Eliminada la secció "5. Recursos educatius".
- Eliminada la slice $arquitectes (només servia al bloc destacat).
- Eliminat el bloc script amb window.PA_GUIES/window.PA_ARQUITECTES i la selecció aleatòria.
- Seccions renumerades (Totes les guies = 2, Tornada al mapa = 3).

El càlcul de $elementsPub i $guies es manté perquè alimenta el recompte de "Totes les guies" (xifres idèntiques a abans).

## 5. Resultat final

La portada queda: hero + xifres + "Totes les guies" + CTA al mapa. Sense blocs de contingut destacat ni recursos educatius.

## 6. Aprovació

Pendent de revisió Joan i validació Xavi.

---

**Nota de criteri:** les regles CSS de les seccions eliminades (.pa-guia-dest*, .pa-arq*, .pa-recursos*) queden al full d'estil sense ús. Neteja opcional.
