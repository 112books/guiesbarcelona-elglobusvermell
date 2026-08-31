# Registre de canvis de fitxes i punts dels mapes

**Regla de governança (aprovada per Joan, 31 ago 2026):** cap creació, esborrat o modificació
de fitxes o punts dels mapes sense **aprovació expressa de Joan** i entrada a aquest registre.
El web actual (Hugo) és la **font de veritat** de les dades; el WordPress antic i els plànols
en paper són referència històrica i mai no "corregeixen" el web sense aprovació.

Cada entrada del registre porta: data, canvi exacte (fitxa i camp), font de dades i
referència de l'aprovació. Davant dubte: **es pregunta primer, no es fa**.

---

## Base de seguretat — recompte (31 ago 2026, abans dels canvis d'avui)

- **Total fitxes:** 658 (657 elements + `_index`)
- **Fitxes amb foto:** 326
- **Recompte per publicació (plànol):**

| Publicació | Fitxes |
|---|---|
| 09-25 | 59 |
| 50-75 | 86 |
| 76-08 | 73 |
| barceloneta | 62 |
| biblioteques | 50 |
| gatcpac | 44 |
| interiors-illa | 79 |
| marina | 20 |
| masies | 88 |
| mercats | 42 |
| poblenou | 77 |
| new-babylon / tapies | 0 (cap fitxa els té com a publicació) |

**Fitxes amb `publicacions` buit (invisibles a tots els plànols):**
`casa-unifamiliar`, `edifici-dhabitatges-carrer-navas`, `jardins-ada-byron`,
`pavello-de-la-republica-de-1937-replica`, `placa-dolors-piera-isabel-vila`.

---

## Registre de canvis

| # | Data | Canvi | Font de dades | Aprovació |
|---|---|---|---|---|
| 1 | 2026-08-31 | Creada `content/ca/elements/casa-roca-barallat.md` — Casa Roca Barallat, Via Augusta 12, Carles Martínez Sánchez, 1935; coords 41.3967221 / 2.1551607 (Nominatim, validat: Via Augusta 61 OSM coincideix amb fitxa Rodriguez Arias a ~3 m); `publicacions: [gatcpac]` (ítem #39 reedició 2026) | PDF reedició 2026 *Arquitectura d'avantguarda* + Nominatim OSM | Joan, 31 ago: "Arregla doncs les fitxes que comenta en XAVI" (Xavi la cita com a pendent de crear) |
| 2 | 2026-08-31 | Afegida `- gatcpac` a `publicacions` de `fundacio-joan-miro.md` (ítem #43 avantguarda, present a les edicions 2016 #46 i 2026 #43) | PDF edicions 2016 i 2026 | Joan, mateixa instrucció |
| 3 | 2026-08-31 | Afegida `- gatcpac` a `publicacions` de `les-escales-park.md` (ítem #42 avantguarda, present a les edicions 2016 #47 i 2026 #42) | PDF edicions 2016 i 2026 | Joan, mateixa instrucció |

**Estat després dels canvis 1-3:** total 659 fitxes; gatcpac 47 elements.

---

## Pendents d'aprovació (NO executar sense confirmació expressa de Joan)

| Fitxa / canvi proposat | Motiu | Estat |
|---|---|---|
| Crear `casa-lluis-jara-urbano.md` — Balmes 371, Josep Soteras Mauri, 1935; coords 41.4045422 / 2.1403092 (Nominatim, validat: Balmes 166 OSM coincideix amb fitxa a ~12 m) | Ítem #38 avantguarda a les dues edicions en paper; mai ha tingut fitxa al web (descobert a la investigació del 31 ago, no citat per Xavi) | 🔴 esperant aprovació de Joan |
| 5 fitxes amb `publicacions` buit (llista amunt) | Invisibles als plànols; 3 són duplicats de migració WordPress | 🔴 esperant decisió (implica Xavi) |
| Duplicats visibles: `edifici-dhabitatges-carrer-navas-238` + `-240` (el paper 2026 les fusiona en #7 Casa Nativitat Vedruna) i `casa-unifamiliar-placa-mons` vs `casa-unifamiliar` (#11 Casa Lluís Barangé) | Artefactes de migració | 🔴 esperant decisió |
| `pavello-de-la-republica-biblioteca-crai-ub.md` (visible, frontmatter malmès) vs `pavello-de-la-republica-de-1937-replica.md` (correcta però sense publicacions) | Duplicat de migració; el mapa mostra la malmesa | 🔴 esperant decisió |
| 4 fitxes d'ítems retirats del paper 2026 (`botiga-cottet`, `reforma-dun-atic`, `reforma-de-laula-de-quimica-a-la-ub`, `adaptacio-dun-convent-per-a-escola-del-cenu`) | Ja no són al plànol en paper però el web les manté (obra GATCPAC real) | 🔴 esperant criteri de Xavi (proposta: mantenir-les) |
