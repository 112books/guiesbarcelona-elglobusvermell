# Informe — anys de les xifres del projecte (D10 / PR1 · R8) — 2026-10-13

**Origen:** Xavi (9/10): «Hem de revisar els anys... veure si podem posar 1400-2026 o s. XIV - 2026.»

## Què es mostra ara
- La portada i Presentació mostren **«anys d'arquitectura: 1928–2026»**.
- El valor surt de `.ai`/parcial `xifres-projecte.html`: **anyMin = 1928 està fixat a mà** («valor editorial»), no es calcula de les dades. `anyMax = any en curs`.

## Què diuen les dades
Analitzades les 657 fitxes (`any`, `edicio` i `intervencions[].any`), l'element més antic de la col·lecció és del **segle XI**:

| Any | Segle | Fitxa |
|-----|-------|------|
| 1000 | s. XI | `masia-can-cortada` |
| 1000 | s. XI | `torre-rodona` |
| 1200 | s. XIII | `masia-can-fargues`, `masia-i-masoveria-de-can-safont` |
| 1300 | s. XIV | `masia-ca-nartes`, `masia-torre-del-rellotge` |
| 1400 | s. XV | `masia-can-figuerola`, `masia-mas-enric`, `masia-mas-guinardo`, `masia-torre-del-fang`, `masia-torre-llobeta` |
| … | … | … |
| 2026 | — | `parc-de-les-glories` (el més modern) |

- Rang real de les dades: **any 1000 – 2026**.
- La proposta «1400-2026» deixaria fora les masies dels segles XI–XIV; «s. XIV-2026» encara deixaria fora les del s. XI–XIII.

## Opcions
- **a) s. XI–2026** — fidel a les dades de la col·lecció (recomanada si l'etiqueta vol dir «tot el que documentem»).
- **b) s. XIV–2026** — com vas proposar; arrodoneix a partir de la baixa edat mitjana, però omet masies més antigues.
- **c) 1400–2026** — descarta tota l'alta edat mitjana.
- **d) Mantenir 1928–2026** — només té sentit si l'etiqueta vol dir «arquitectura contemporània», no la col·lecció sencera.
- **e) Reformular l'etiqueta** — canviar «anys d'arquitectura» per un altre text si es vol parlar només de l'arquitectura moderna.

## Nota
Si es tria una opció basada en segles, caldrà decidir el format exacte del text («s. XI–2026» vs «1000–2026»). El canvi és d'una línia al parcial `xifres-projecte.html`.

*Font canònica en Markdown (LinuxBCN).*
