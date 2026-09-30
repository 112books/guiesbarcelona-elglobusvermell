# Feedback Xavi — El Globus Vermell · 30 setembre 2026

Font: correu directe Xavi → Joan. Primer lot de feedback consolidat de l'equip.

**Resposta a l'eina de revisió (30/9/2026):** `.ai/RESPOSTES-XAVI-2026-09-30.md` (font literal a `.ai/fonts-xavi/2026-09-30-xavi-resposta-revisio.md`).

---

## Meta — reflexió sobre el flux de treball

Xavi demana que Joan revisi personalment les peticions abans de delegar a IA. Alguns fils han quedat encallats per interpretació automàtica. Valor de la mirada humana per avaluar si val la pena automatitzar o és millor editar manualment.

---

## GENERAL — Estructura i navegació

| ID | Descripció | Estat |
|----|-----------|-------|
| G1 | Layout dues modalitats: (a) sang de banda a banda (portada, mapa, presentació), (b) dues columnes (fitxes, en paper) | Pendent decisió mides columnes |
| G2 | Menú sempre en text, mai icones en fer scroll (només icones al mòbil) | Pendent implementació |
| G3 | Ordre menú: Presentació · Mapa · En paper · Arquitectes · Contacte | Pendent implementació |
| G4 | Alineació vertical menú (logo+nav) amb les dues columnes de contingut | Lligat a G1 |

---

## PÀGINA PRINCIPAL

| ID | Descripció | Estat |
|----|-----------|-------|
| P1 | Bloc hero: logo "Arquitectura i urbanisme de Barcelona" centrat + xifres (elements documentats, guies, arquitectes) | Pendent |
| P2 | Tagline "Tota l'arquitectura i l'urbanisme de Barcelona, guia a guia." — a confirmar, però editable per ells | Pendent consens intern |
| P3 | Bloc mapa navegable a portada + botó "veure filtres" → pàgina mapa completa | Pendent |
| P4 | Bloc totes les guies (ja existeix) — manté si layout va a sang elimina el problema 6+6+1 | Revisar quan G1 resolt |
| P5 | Eliminar: guia destacada, arquitecte destacat, recursos educatius | Pendent |
| P6 | Valorar: navegació per blocs amb scroll com arquitecturacatalana.cat | Decisió Joan+Xavi |
| P7 | Mòbil: splash logo breu abans d'entrar al mapa (sense click) | Pendent prototip |
| P8 | Eliminar pastilles negres; si n'hi ha, prefereixen a sang als cantons | Lligat a G1 |

---

## MAPA

| ID | Descripció | Estat |
|----|-----------|-------|
| M1 | Augmentar zoom inicial del mapa | Pendent (fàcil) |
| M2 | Mapa en escala de grisos — opcional, "no molesta excessivament" | Valorar (Stadia Maps té estil grayscale) |
| M3 | Pins multicolor: meitat/meitat (o pastís 3 colors) per elements que pertanyen a dos o més plànols | Pendent — cal decidir implementació SVG/Canvas |
| M4 | Quan es selecciona un plànol, NO difuminar la resta d'elements | Pendent |
| M5 | Temes transversals: afegir botó (i) amb informació pròpia (contingut de la web antiga, Xavi ho passa) | Pendent contingut |
| M6 | Eliminar llistat d'elements sota el mapa i l'abecedari; mantenir només el cercador | Pendent |
| M7 | Camp arquitecte al cercador: dropdown + typeahead (el llistat es redueix mentre s'escriu) | Pendent |

---

## FITXES EDIFICIS

| ID | Descripció | Estat |
|----|-----------|-------|
| F1 | Layout dues columnes: foto (sticky en scroll) a l'esquerra, informació a la dreta | Pendent |
| F2 | Ordre informació: nom edifici → xips plànol (color del plànol) + xips transversals (gris neutre) → taula → text → ubicació | Pendent |
| F3 | Nom edifici amb interlineat estret quan ocupa dues línies | Pendent |
| F4 | Mapa ubicació: no a sang (no ocupa tota l'amplada) | Pendent |
| F5 | Taula projecte: arquitectes clicables + any no clicable en un sol camp (ex: "Joan Arias, Lluís Pérez de la Vega, 1988") — confirmar tècnicament | Cal avaluar abans d'implementar |
| F6 | Fotos en blanc i negre — NO implementar ara; preguntar confirmació primer; és reversible? | En espera confirmació |
| F7 | Canviar "edificis" → "elements" a tot el lloc | Pendent (cerca/substitució global) |

---

## PRESENTACIÓ

| ID | Descripció | Estat |
|----|-----------|-------|
| PR1 | Xifres portada i pàgina Presentació han de ser idèntiques | Pendent (ja era tasca oberta) |
| PR2 | Afegir secció presentació d'El Globus Vermell (contingut pendent d'ells) | Pendent contingut |
| PR3 | Pàgines buides a l'editor (no editables) — diagnosticar problema CMS | Bug a investigar |
| PR4 | Eliminar bloc "Suggerir un canvi" | Pendent |

---

## EN PAPER

| ID | Descripció | Estat |
|----|-----------|-------|
| EP1 | Redisseny: 4 blocs: (a) text presentació, (b) carrusel horitzontal portades, (c) xips temàtics, (d) llistat dues columnes | Disseny pendent |
| EP2 | Carrusel: clic a portada fa scroll fins al plànol corresponent | Pendent |
| EP3 | Carrusel infinit (loop) — pendent decisió | Pendent |
| EP4 | 4 xips: Èpoques · Usos · Barris · Art + xip "Tots" | Pendent contingut (descripcions TBD, lorem ipsum provisional) |
| EP5 | Xips filtren tant el carrusel com el llistat | Pendent |
| EP6 | Plànols en dues columnes: portada a l'esquerra, títol+text a la dreta | Pendent |
| EP7 | Afegir al final: Punts de venda + enllaç "vols vendre els plànols guia al teu espai?" → contacte | Pendent |
| EP8 | Reordenar temes — pendent decisió interna equip | Pendent |

---

## EN PAPER — PER CADA PLÀNOL

| ID | Descripció | Estat |
|----|-----------|-------|
| EPI1 | Layout dues columnes: portada+índex (sticky) a l'esquerra, plànol+textos a la dreta | Pendent |
| EPI2 | Textos sempre desplegats (eliminar accordions / clics extra) | Pendent |
| EPI3 | Índex esquerra per navegar pels temes del plànol | Pendent |

---

## ARQUITECTES

| ID | Descripció | Estat |
|----|-----------|-------|
| A1 | Ordenació per cognom — evaluar implicacions (dades, slugs, etc.) | Cal avaluació prèvia |
| A2 | Llistat elements de l'arquitecte: eliminar etiqueta any + eliminar clics extra | Pendent |

---

## CONTACTE

| ID | Descripció | Estat |
|----|-----------|-------|
| C1 | Actualitzar text formulari (un sol formulari: floretes, vendre plànols, finançar nous plànols) — contingut pendent d'ells | Pendent contingut |
| C2 | No troba on editar la pàgina de contacte al CMS — diagnosticar/documentar | Bug o buit en guia editors |

---

## GRAFISME

| ID | Descripció | Estat |
|----|-----------|-------|
| GR1 | Colors pins mapa i etiquetes fitxes = color específic de cada plànol, editable per ells | Pendent |
| GR2 | Vermell actual → negre o gris fosc (el vermell és identitat del Globus, no d'aquesta web) | Pendent (canvi disseny — aprovar explícitament) |
| GR3 | Tipografia: explorar opcions. Qualsevol? D'un catàleg? Fàcil el canvi? | Pendent avaluació + decisió |

---

## RESPOSTES A PREGUNTES OBERTES (de correus anteriors)

| Pregunta | Resposta Xavi |
|---------|--------------|
| Data tall domini Dinahosting | "Quan tinguem la web enllestida" (no data concreta) |
| Noms usuari GitHub (Laia, etc.) | Pendent que Joan demani (o ja té?) |
| 73 arquitectes combinats | Es faran manualment |
| PDFs pendents | Barceloneta castellà: ja existeix. Francesos (8) + Marina EN/ES: no existeixen |
| Llicència peu de pàgina | Creative Commons BY-SA |
| Autoria fotos | Nota genèrica CC BY-NC a peu de pàgina + nom arxiu/meta amb "elglobusvermell" |
| Botó mapa exterior | Google Maps (un sol botó, per familiaritat) |
| Lectura en veu alta | Versió actual, però IMPORTANT: afegir a "en paper" i a cada plànol |
| Estadístiques | Privades, ok |

---

## FUTUR

| ID | Descripció |
|----|-----------|
| FU1 | CMS: documentar com crear nous plànols i noves fitxes (molt important per a ells) |

---

## ERRORS

Xavi no ha pogut recopilar els errors de migració WP. Decidit: es faran manualment quan calgui, sense automatitzar.

---

## Fil 2 — Arquitectes: normalització i separats (resposta Xavi ~30/9)

### Resum del fil

Joan havia enviat a Xavi:
- **Punts desubicats (5 fitxes):** coordenades ja eren correctes. Pendent aplicar: "Casa xalet passatge Roserar" → "Casa Mercè Escolano"
- **Diccionari normalització arquitectes:** aplicades les correccions. Dos casos tractats diferent:
  - MBM: corregit per normalitzar "MBM (Martorell, Bohigas, Mackay)" → "MBM Arquitectes"
  - Lluís Cantallops: tret del diccionari (persona ≠ estudi, no fusionar)
  - Antoni de Moragas i Francesc Riba: mantingut a ARQUITECTES-A-SEPARAR.md (no és variant ortogràfica, és dos arquitectes)
- **Format per separar arquitectes combinats:** Joan havia proposat format simple: `Nom combinat actual → Nom 1, Nom 2`

### Resposta Xavi

"Bon dia! Això ho fem directament a la web de l'editor, ja que ens cal una bona repassada general a tots els arquitectes, i sospito que haurà de ser manual. Gràcies!"

### Decisions

- Normalització diccionari: posposada — ho faran manualment des del CMS
- Separació arquitectes combinats: ídem, manual des del CMS
- Pendent: canvi de nom "Casa xalet passatge Roserar" → "Casa Mercè Escolano" — confirmar si també ho fan ells o ho apliquem nosaltres

---

## Fil 4 — Arquitectes: tres dubtes de nom (resposta Xavi ~30/9)

Joan havia plantejat 3 casos concrets per resoldre:
1. **Helio Piñón vs Heliodoro Piñón Pallarés** — la fitxa diu "Helio Piñón" però les 4 fitxes d'edificis usen el nom complet
2. **E. i J. Rey Fàbregas** — dos germans separables o nom d'estudi conjunt (Industrias Deslite, 1957)
3. **Mariano Romano Rius (?)** — ortografia marcada amb incertesa en una revisió anterior

Joan havia ofert dues opcions: que Xavi ho edités ell mateix al CMS (instruccions pas a pas incloses) o que respongués les decisions i nosaltres ho apliquéssim.

Resposta Xavi: "De moment ho deixarem com està. En tot cas, ja ho revisarem manualment, si cal. Gràcies!"

**Decisió:** els tres casos queden sense canvi per ara. Revisió manual futura si convé.

---

## Fil 3 — MAPATGE-URLS.md no adjuntat

Joan va enviar a Xavi una explicació detallada del document MAPATGE-URLS.md (666 URLs WP, 660 redirects, 3 idèntiques, 2 eliminades, 221 noves) però va oblidar adjuntar el fitxer.

Xavi va respondre: "Aquí deies que adjuntaves un document, però no hi havia document adjunt... Gràcies,"

**Pendent:** reenviar el correu amb el fitxer MAPATGE-URLS.md adjunt (o com a link al repositori).

---

## Tasques que Joan ha de respondre a Xavi

1. **F5** — arquitectes clicables + any al mateix camp: confirmar si és possible tècnicament
2. **A1** — ordenació arquitectes per cognom: quines implicacions té (canvi de slugs, etc.)?
3. **M3** — pins multicolor: com s'implementa? Necessita dades de quin color té cada plànol
4. **GR3** — tipografia: quines opcions hi ha? Cal decidir junts
5. **EP3** — carrusel infinit: recomanació tècnica
6. **GR1/GR2** — colors: cal que ells passin la paleta definitiva per plànol
7. **P7** — splash logo mòbil: demostrar/protipar per confirmar expectativa
8. **C2** — pàgina contacte al CMS: verificar per quin motiu no apareix editable
