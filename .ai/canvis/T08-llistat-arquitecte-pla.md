# T08 — Llistat de la pàgina d'arquitecte: sense etiqueta d'any ni clics

**Data:** 2026-09-30
**Estat:** Implementat — pendent d'aprovació

## 1. Tasca demanada

> "Llistat elements de l'arquitecte: eliminar etiqueta any + eliminar clics extra."

Font: feedback Xavi 30/9/2026, secció ARQUITECTES (A2). Handoff T08.

## 2. Solució prevista

Afegir un mode de llistat plana a mapa.js: una llista única ordenada alfabèticament, sense agrupacions per any (ni les seves etiquetes) i sense acordions, per tant sense cap clic addicional. La pàgina d'arquitecte passa a fer servir aquest mode.

## 3. Estat de l'execució

Implementat el 2026-09-30. Build Hugo OK. Pendent d'aprovació abans de commit.

## 4. Fitxers modificats

### themes/guiesbcn-elglobusvermell/layouts/arquitectes/term.html

- window.LLISTAT_GRUP = 'plana'; (abans 'any').
- Tret aria-hidden="true" de la secció #llistat: ara la llista és visible i accessible.

### themes/guiesbcn-elglobusvermell/assets/js/mapa.js

- Nova branca grupPer === 'plana' dins construeixLlistat(): construeix una única ul.llistat-grup-elements.llistat-incrustat amb tots els elements ordenats per títol, i retorna.
- Les insígnies d'any i de publicacions se suprimeixen també en mode plana (com ja passava amb any).

## 5. Resultat final

La pàgina de cada arquitecte mostra un únic llistat alfabètic de tots els seus elements, sempre desplegat, sense l'etiqueta d'any ni cap clic per obrir-lo.

## 6. Aprovació

Pendent de revisió Joan i validació Xavi.
