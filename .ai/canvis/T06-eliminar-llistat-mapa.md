# T06 — Eliminar l'abecedari (horitzontal i vertical) sota el mapa

**Data:** 2026-09-30
**Estat:** Implementat (abast revisat per Joan) — pendent d'aprovació

## 1. Text literal de Xavi

Font: `.ai/FEEDBACK-XAVI-2026-09-30.md`, secció MAPA:

> `| M6 | Eliminar llistat d'elements sota el mapa i l'abecedari; mantenir només el cercador | Pendent |`

## 2. Abast acordat amb Joan (2026-09-30)

Joan concreta: **treure l'abecedari horitzontal i vertical, res més**.
- Abecedari horitzontal = barra d'índex de lletres (`.llistat-index`).
- Abecedari vertical = llistat agrupat per lletra (`.llistat-grups`).
- **No es toca res més:** es conserven el cercador (Cerca, Època, Arquitecte) i els
  filtres de Publicacions i Temes transversals.
- **No** s'ha connectat el cercador als marcadors del mapa (es va provar i s'ha
  revertit: era una interpretació que anava més enllà de la petició).

## 3. Estat de l'execució

Implementat el 2026-09-30. Build Hugo OK. Pendent d'aprovació abans de commit.

## 4. Fitxers modificats

### `themes/guiesbcn-elglobusvermell/layouts/mapa/list.html`

Eliminada la secció:

    <section class="llistat-alfabetic" id="llistat">
      <nav class="llistat-index" id="llistat-index" aria-label="Índex alfabètic"></nav>
      <div id="llistat-grups"></div>
    </section>

L'etiqueta del cercador passa de "Filtres del llistat" a "Cercador del mapa".

### `themes/guiesbcn-elglobusvermell/layouts/elements/list.html`

Mateixa eliminació. Aquesta plantilla no es renderitza (`build.render: never`;
/elements/ és un alias de /mapa/), però es manté coherent.

### `themes/guiesbcn-elglobusvermell/assets/js/mapa.js`

**Sense canvis nets** respecte T04 v2: la connexió cercador→mapa que s'havia
provat queda revertida. Els únics canvis pendents al fitxer són els de T08.

## 5. Resultat final

La pàgina /mapa/ mostra el mapa, els filtres de Publicacions/Temes i el cercador,
sense l'abecedari horitzontal ni el vertical.

## 6. Pregunta oberta per a Xavi

Confirmar si també vol treure el bloc **"Publicacions"** (l'activador/desactivador
d'elements del mapa). Assumpció: **mantenir-lo**.
Afegit a `.ai/QUESTIONS-CLIENT.md`.

## 7. Aprovació

Pendent de revisió Joan i validació Xavi.

---

**Observació UX:** el cercador queda a la pàgina però, sense el llistat, actualment
no filtra res. Es manté perquè és el que demana Xavi ("mantenir només el cercador")
i a l'espera de confirmar amb ell com ha de funcionar.
