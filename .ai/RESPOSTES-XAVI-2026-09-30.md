# Resposta de Xavi a l'eina de revisió — 30 setembre 2026

**Font literal:** `.ai/fonts-xavi/2026-09-30-xavi-resposta-revisio.md`
**Eina revisada:** https://112books.github.io/guiesbarcelona-elglobusvermell/admin/revisio/
**Data del missatge:** 30/9/2026
**Derivat de:** `.ai/FEEDBACK-XAVI-2026-09-30.md` i `static/admin/revisio/tasques.json`

Xavi contesta l'eina de revisió. Respon 6 de les decisions obertes, verifica 3
canvis com a OK i comenta 9. Els blocs «Pendent de fer (nosaltres)» i
«Sobre les decisions nostres» li surten buits al resum: no hi afegeix res.

---

## 1. Decisions respostes

| Ref | Pregunta | Resposta | Conseqüència |
|-----|----------|----------|--------------|
| M6 · T06 | Treure el bloc «Publicacions» del mapa? | **Mantenir-lo** (recomanat) + volen valorar un filtre de temes (Èpoques, Arquitectura temàtica, Barris, Art) com a «En paper»; no n'estan segurs | Es manté. Nova tasca **R12** (valorar filtre de temes). Cal concretar-ho amb ells. |
| PR4 · T07 | «Suggerir un canvi»: només fora de Presentació o del tot? | **Només fora de Presentació** (es manté a Contacte) amb un únic formulari per a tot | Es manté a Contacte. Nova tasca **R11** (unificar en un sol formulari). |
| M3 | Pins multicolor per a elements de diversos plànols | **Sí**, meitat/meitat o pastís de 3 colors | Nova tasca **R3**. Depèn de la paleta (**R13**). |
| EP3 | Carrusel de portades: infinit o amb final? | **Infinit**. Al mòbil ja agrada; a escriptori volen amagar la barra de desplaçament, arrossegar amb el cursor i portades més grans | Nova tasca **R4**. |
| GR1 · GR2 | Colors dels pins i etiquetes, i el vermell del web | **Passaran la paleta definitiva per plànol**. Reporten que **el filtre del mapa no funciona** | Nova tasca **R13** (espera paleta). Nova tasca **R1** (bug del filtre, confirmat per nosaltres). |
| G1 | Amplada de la columna de text | **Prova amb 2-3 amplades i trien** | Nova tasca **R9**. |

## 2. Canvis fets — verificació

| Ref | Canvi | Estat Xavi | Comentari | Acció |
|-----|-------|------------|-----------|-------|
| M5 | Botó (i) als temes transversals | Amb comentaris | Volen **pàgina pròpia amb el seu mapa**, com els temes dels plànols-guia | Nova tasca **R2** |
| F6 | Fotos en blanc i negre | Amb comentaris | Sense consens a l'equip; ho deixen com està. Exploren **color parcial** (patrimoni industrial amb il·lustracions vermelles; resta B/N) | Nova tasca **R5** |
| P7 | Splash amb el logo al mòbil | Amb comentaris | Surt la pantalla negra un instant **sense el logo**; una mica més llarg, tampoc massa; un cop per sessió OK | Nova tasca **R6** |
| G1 | Alineació del logo i el menú amb el cos | Amb comentaris («Ens agrada!») | Aprovació implícita | Es pot donar per validat |
| ENQ-lectura | Lectura en veu alta a «En paper» i plànols | Amb comentaris | Alinear el botó **a la dreta** com a les fitxes; dubte sobre si la veu ha canviat | Nova tasca **R7** |
| PR1 | Xifres del projecte (portada i Presentació) | Amb comentaris | Revisar els anys; dubte **1400-2026 vs s. XIV-2026**. Vindrà d'arreglar les fitxes | Nova tasca **R8** |
| G2·G3·F7 | T01–T03 terminologia, ordre de menú, menú text | Amb comentaris | «Genial!» + **icones mòbil**: la icona de mapa passa a «En paper»; el mapa estrena **pin clàssic** | Nova tasca **R10** |
| M1 | T04 zoom inicial del mapa | **Verificat i OK** | — | Tancat |
| M4 | T05 sense difuminat en seleccionar plànol | Amb comentaris | «Ara no funciona el filtre»: seleccionar una guia no amaga ni difumina la resta. L'atenuació original no els convenç («queda brut»); la potència del conjunt es veu en obrir el mapa | **R1** (cal aclarir el comportament desitjat) |
| PR4 | T07 «Suggerir una correcció» fora de Presentació | Amb comentaris | A Contacte pensaran una frase que serveixi per a tot; oberts a diversos formularis si ho veiem millor | **R11** |
| A2 | T08 llistat de la pàgina d'arquitecte en pla | **Verificat i OK** | — | Tancat |
| FU1 | CMS: on i com crear fitxes noves | **Verificat i OK** | — | Tancat |

## 3. Preguntes obertes que queden SENSE resposta

Xavi no va respondre aquestes decisions de l'eina:

- **cercador-general** (NOU) — cercador general a tot el web o només el d'elements.
- **autoria-fotos** (ENQ-autoria) — web CC BY-SA i fotos CC BY-NC amb nota genèrica.
- **arquitectes-combinats** (PREG-arquitectes) — com els ho posem fàcil per separar-los.
- **portada-guies-distribucio** (P4 · G1) — 6·6·1 o 5·5·3.
- **m2-mapa-grisos** (M2) — base en grays o punts.
- **gr3-tipografia** (GR3) — proposta de 2-3 tipografies lliures.

Canvis que no va verificar: **cercador-mapa** (M6), **en-paper** (EP1-EP8),
**p6-navegacio-blocs** (P6), **t06** (abecedari) i **t09** (portada sense
destacats). Les tres **decisions nostres** no tenen cap comentari.

## 4. Bug confirmat: el filtre del mapa no fa res visualment

Xavi ho diu dues vegades. Causa directa:

`themes/guiesbcn-elglobusvermell/assets/js/mapa.js:328`

```js
// T05 — es va igualar l'atenuada a la ressaltada
var OPACITAT_ATENUADA = OPACITAT_RESSALTADA;
```

El codi sí que calcula bé la pertinença a cada guia, però com que l'opacitat
atenuada és idèntica a la ressaltada, **seleccionar una guia no produeix cap
efecte visual**. Quelcom similar passa a la base «b» (satèl·lit), on
`OPACITAT_RESSALTADA = { opacity: 0, fillOpacity: 0.92 }`.

Punt ambigu a aclarir amb Xavi: diu que el filtre «no funciona» però també que
l'atenuació original «queda brut». Cal triar entre atenuar, amagar, ressaltar
d'una altra manera o fer zoom/llistat en seleccionar una guia.

## 5. Tasques noves derivades (prefix R)

| ID | Tasca | Depèn de |
|----|-------|----------|
| R1 | Filtre del mapa: corregir la regressió de T05 i acordar el comportament en seleccionar una guia | Decisió de Xavi |
| R2 | M5: pàgina pròpia per als temes transversals amb el seu mapa (en lloc del botó (i)) | — |
| R3 | M3: pins multicolor meitat/meitat o pastís de 3 colors | R13 (paleta) |
| R4 | EP3: carrusel infinit, amagar scrollbar a escriptori, arrossegar amb cursor, portades més grans | — |
| R5 | F6: explorar color parcial a les fotos (patrimoni industrial) i consens d'equip | Equip |
| R6 | P7: splash mòbil amb el logo i una mica més de durada | — |
| R7 | ENQ-lectura: alinear el botó d'escoltar a la dreta com a les fitxes; revisar la veu | — |
| R8 | PR1: revisar els anys de les xifres (1400-2026 vs s. XIV-2026) | Fitxes |
| R9 | G1: prova de 2-3 amplades de columna de text perquè triïn | — |
| R10 | Icones mòbil: la icona de mapa passa a «En paper»; el mapa estrena pin clàssic | — |
| R11 | T07: valorar un únic formulari a Contacte per a tot (o mantenir-ne dos) | — |
| R12 | Valorar un filtre de temes (Èpoques, Arquitectura temàtica, Barris, Art) a «En paper» i potser al mapa | Xavi |
| R13 | Aplicar la paleta definitiva per plànol quan Xavi l'enviï | Xavi |

## 6. Proper pas

1. Confirmar amb Xavi el comportament del filtre del mapa (R1) i concretar el
   filtre de temes (R12), les dues coses que la seva resposta deixa obertes.
2. Reprintar-li les 6 decisions sense resposta (secció 3).
3. Implementar la resta de tasques R quan hi hagi vistiplau.

---

**Nota de governança:** `.ai/` viu al repositori públic
`112books/guiesbarcelona-elglobusvermell` (ja hi havia les fonts d'Xavi i
l'eina de revisió). Si es prefereix no publicar els correus sencers, caldria
moure les fonts a `docs/` (repo privat).
