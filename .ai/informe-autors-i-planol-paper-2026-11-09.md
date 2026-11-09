# Informe — Fotos del plànol en paper, autors enllaçats i autors editables

**Data:** 9/11/2026
**Estat:** les tres tasques fetes, verificades i en línia · CI verd
**Relacionat:** mail d'en Xavi del 6/11 (`docs/2026-11-06-mail-xavi-resposta-2.md`), registre de fitxes #18

---

## 1. Fotos del plànol en paper (punt 6 de la llista d'en Xavi)

**Què demanava:** «A l'apartat en paper de cada plànol-guia ens agradaria afegir un carrusel de fotos dels plànols en paper.»

**Què s'ha fet** (`2cd03be4`):
- Camp nou al CMS, dins de la col·lecció de plànols-guia: **«Fotos del plànol en paper»** (llista d'imatges amb peu opcional). Les imatges es desen a `static/img/publicacions/paper`.
- Carrusel horitzontal a la pàgina del plànol, després de les descàrregues, amb desplaçament natiu i imant (sense JavaScript).

**Com s'ha verificat:**
- Amb dades de prova (una foto amb peu i una sense): surten les dues figures, amb el text alternatiu correcte.
- Sense fotos: **la secció no apareix** i la pàgina queda igual. Comprovat en viu a «Mercats».
- L'editor carrega el camp nou (obert amb el token): surt «0 Fotos del plànol en paper» i el botó d'afegir. El YAML del CMS és vàlid (el 30/10 va caure per un comentari de plantilla Hugo dins `config.yml`; aquesta vegada s'ha validat amb el parser).

## 2. Els autors de «Projecte» enllacen a la seva fitxa

**Què demanava:** «Al camp projecte apareixen els mateixos noms però escrits diferents i sense enllaçar.»

**Què s'ha fet** (`c2fc28d5`):
- Els autors es tracten igual vinguin com a llista o com a text: se separen per « + », « – », coma i barra, s'eliminen duplicats i **cada nom enllaça a la pàgina del seu arquitecte si existeix**.
- S'ha afegit el parcial `arquitectes-permalinks.html` (mapa nom → enllaç): les pàgines d'arquitecte són termes de taxonomia amb **accents a la URL** (`/arquitectes/albert-de-pineda-álvarez/`) i el `urlize` antic no hi encertava, i per això no s'enllaçava res.

**Verificat:** Camp Nou (2 enllaços), Montbau (2 enllaços, sense duplicats) i Parc de Recerca (només el que té fitxa). En viu.

## 3. Els autors de les intervencions es poden editar a l'editor

**Per què no es podia:** el camp d'autors és una **relació múltiple** i 309 intervencions el tenien com un **text**; l'editor n'esperava una llista i la mostrava buida.

**Què s'ha fet** (`80564b3d`): normalitzades **297 fitxes / 309 valors** a llista amb `scripts/normalitza-autors.py` (té `--dry`).

**Precaucions:**
- Còpia prèvia: `/tmp/elements-backup-20261109-1334` (+ `.tgz`) i branca `backup/autors-abans-20261109-1334`.
- Separadors **amb espais**: mai el «+» enganxat («Peris+Toral», «Roldán+Berengué») ni el « i » dels cognoms («Josep Font i Gumà»). La primera passada els va trencar i ho va detectar el diff del build abans de pujar res.
- Duplicats fora i camps buits a llista buida.

**Verificacions (les quatre):**
1. **Semàntica:** per a cada fitxa, la resta de camps és idèntica a la de git i la llista resultant és exactament la separació del text antic. 297 fitxes, 309 valors, **0 problemes**.
2. **Build:** les **661 pàgines d'element surten byte a byte igual** abans i després. Les 4 pàgines d'arquitecte que difereixen són el bug no determinista de Hugo amb termes amb «&»: dues compilacions de la mateixa font també difereixen en aquelles.
3. **Editor:** obert el CMS amb la fitxa del Camp Nou, la intervenció mostra «Francesc Mitjans i Miró» i «Josep Maria Soteras i Mauri» seleccionats, amb la × per treure'ls.
4. **En línia:** CI verd (Deploy + pa11y) i pàgines 200.

Registrat com a **#18** al `REGISTRE-CANVIS-FITXES.md`.

## 4. Pendent

- **Validació d'en Xavi** de la llista dels 92 noms orfes (`/admin/revisio/arquitectes-orfes.html`), amb l'opció «Mixt» per als casos barrejats. Amb això es podran crear les fitxes que faltin (**Fase 3**) i, per tant, que aquests noms acabin d'enllaçar i apareguin al selector de l'editor.
- **Fotos** dels plànols en paper (les ha de fer arribar).
- **Paleta** definitiva i **textos** que vulguin que escrivim nosaltres.
