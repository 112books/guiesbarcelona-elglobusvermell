# Resposta tècnica a Xavi — 8 punts del 30/9/2026

Data: 2026-10-01
Font de les preguntes: `.ai/FEEDBACK-XAVI-2026-09-30.md`, secció "Tasques que Joan ha de respondre a Xavi".
Estat: esborrany de respostes tècniques. Cap canvi de disseny sense aprovació.

---

## F5 — Arquitectes clicables + any en un sol camp

**Pregunta:** es pot mostrar "Joan Arias, Lluís Pérez de la Vega, 1988", amb els arquitectes clicables i l'any no clicable, en un sol camp?

**Resposta:** sí. La fitxa ja mostra avui els arquitectes com a enllaços
(`layouts/elements/single.html`, bloc `fitxa-dades`). N'hi ha prou de posar
l'any al mateix `dd`, després dels enllaços i separat per una coma:

- Arquitectes: enllaços a la seva pàgina (ja funciona).
- Any: text pla dins el mateix camp.
- Si hi ha diverses intervencions, es poden llistar els anys de cada intervenció
  (el camp `intervencions` ja existeix a 324 fitxes i es pinta a part).

Pendent de decidir amb el client: si l'any ha de ser clicable i portar a un
llistat d'elements d'aquell any. Tècnicament és possible (una pàgina de filtre
per any), però és una funcionalitat nova.

---

## A1 — Ordenació dels arquitectes per cognom

**Pregunta:** quines implicacions té ordenar-los per cognom?

**Resposta:** es pot fer sense canviar cap URL. Actualment la pàgina
`/arquitectes/` agrupa per la primera lletra del títol (`layouts/arquitectes/terms.html`).
L'URL de cada arquitecte deriva del nom (`nombre | urlize`), no de l'ordre, així
que reordenar no trenca enllaços.

Per ordenar pel cognom cal una dada fiable: no es pot deduir el cognom de manera
automàtica en tots els casos (noms compostos, estudis). Opcions:

1. Afegir un camp opcional `cognom` a la fitxa d'arquitecte i ordenar per aquest
   camp; si no hi és, s'usa el títol.
2. Mantenir l'ordre actual per nom complet.

Recomanació: opció 1, editat des del CMS. És feina de contingut (197 fitxes),
no de programari.

---

## M3 — Pins multicolor

**Pregunta:** com s'implementa el pin meitat/meitat o pastís de 3 colors?

**Resposta:** ara els punts del mapa són cercles (`L.circleMarker`) amb el color
de la publicació. Per fer meitat/meitat o pastís cal canviar el marcador per un
`L.divIcon` amb un SVG de dos o tres sectors. La dada de colors per publicació ja
existeix (`data/publicacions.yml`), de manera que la implementació és directa.

Dependència: la paleta definitiva per plànol (GR1/GR2). Fins que arribi, es pot
programar amb els colors actuals i canviar-los després canviant només el fitxer
de dades.

Cal mantenir l'accessibilitat que ja té el marcador actual (focus, `role`,
`aria-label`, Enter/Espai).

---

## GR3 — Tipografia

**Pregunta:** quines opcions hi ha i és fàcil canviar-la?

**Resposta:** el web fa servir avui la pila de tipografies del sistema (sense
cap fitxer extern ni Google Fonts, coherent amb la privacitat del projecte).
Canviar-la és fàcil: es defineix a `--font-sans` (`main.css`) i s'aplica a tot.

Propostes de tipografies lliures (llicència SIL OFL), autoallotjades en WOFF2
(sense peticions externes ni galetes):

1. **Inter** — neutra, molt llegible en pantalla, àmplia cobertura de caràcters.
2. **Source Sans 3** — humanista, bona en text llarg, català ben cobert.
3. **Atkinson Hyperlegible** — dissenyada per a baixa visió, reforça accessibilitat.

Es pot preparar una pàgina de prova amb les tres perquè triïn.

---

## EP3 — Carrusel infinit

**Resposta:** ja implementat (tasca R4). El carrusel d'En paper és infinit, sense
barra de desplaçament a escriptori, s'arrossega amb el cursor i les portades són
més grans. Pendent de validació visual del client.

---

## GR1 / GR2 — Colors

**Resposta:** GR2 ja aplicat: l'accent vermell ha passat a gris fosc (#222) a
l'espera de la paleta definitiva. GR1 (colors de pins i etiquetes) queda
preparat: només cal que arribi la paleta per plànol amb els codis HEX.

---

## P7 — Splash mòbil

**Resposta:** ja implementat (tasca R6): el splash mostra el logo i dura una
mica més. Es pot ajustar la durada a demanda.

---

## C2 — Pàgina de Contacte al CMS

**Resposta:** era cert: la col·lecció `pagines` no incloïa Contacte. Ja està
corregit. Ara són editables des de l'editor: Presentació, En paper, Crèdits,
Contacte, Accessibilitat, Avís legal, Política de galetes i Política de
privacitat. També s'ha actualitzat la guia de l'editor.

---

## Resum

- Fets i confirmats: EP3, P7, C2, GR2.
- Viables amb feina petita: F5, M3.
- Viables però depenen de dades del client: A1 (camp cognom), GR1 (paleta).
- A decidir: anys clicables (F5), tipografia (GR3).
