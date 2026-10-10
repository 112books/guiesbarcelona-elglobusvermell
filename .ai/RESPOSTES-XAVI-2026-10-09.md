# Resposta de Xavi a la revisió de canvis — 9 octubre 2026

**Font literal:** `.ai/fonts-xavi/2026-10-09-xavi-resposta-revisio.md`
**Eina revisada:** https://112books.github.io/guiesbarcelona-elglobusvermell/admin/revisio/
**Data del missatge:** 9/10/2026
**Derivat de:** `.ai/RESPOSTES-XAVI-2026-09-30.md` i `static/admin/revisio/tasques.json`

Aquest correu arriba **després** del del 30/9. Primer posa temes que no són a
l'eina de revisió (temes nous i errors de traspàs) i després la resposta a les
preguntes. Serveix per **separar què dona per OK** (es pot tancar) de **què
genera tasca nova**.

**Titular:** el bloc que més corre: **el CMS es trencava en clicar «Publicacions»**
(pantalla negra). És la prioritat. Ja hi ha una correcció verificada (secció 7).

---

## 1. Què dona per OK (es pot tancar)

Referències que Xavi marca com a **«Verificat i OK»**, amb o sense comentari:

| Ref | Què | Comentari |
|-----|-----|-----------|
| C2 | Pàgina de Contacte editable al CMS | OK |
| ENQ-autoria | Autoria de les fotografies i llicència del peu | verificat |
| ENQ-autoria | Autoria de les fotografies: CC BY-NC 4.0 | OK |
| #972 (P7) | Splash amb el logo al mòbil | «Ara va estupendo!» |
| #973 (P7 · R6) | Splash mòbil: es veu el logo | «Genial!» |
| #976 (M1) | T04 — Zoom inicial del mapa | OK |
| #977 (M6) | T06 — Abecedari i llistat del mapa eliminats | «…genial!» |
| #978 (PR4) | T07 — «Suggerir una correcció» fora de Presentació | OK |
| #979 (A2) | T08 — Llistat de la pàgina d'arquitecte en mode pla | OK |
| #981 (FU1) | CMS — On i com crear fitxes noves | OK (tot i que després hi troba el bug) |
| #984 (ENQ-lectura · R7) | Botó d'escoltar alineat a la dreta | OK |
| #985 (G2·G3·F7 · R10) | Icones mòbil: mapa → En paper; pin clàssic al mapa | OK |
| #986 (GR2) | El vermell del web passa a gris fosc | OK |
| #987 (M5 · R2) | Temes transversals: pàgina pròpia amb el seu mapa | OK |
| #988 (T07 · R11) | Un sol formulari a Contacte per a tot | OK |
| #989 (ENQ-autoria) | Autoria de les fotografies: CC BY-NC 4.0 | OK |
| #990 (C2) | Pàgina de Contacte editable al CMS | OK |

> Matís important: **FU1 (crear fitxes) el dona per OK però tot seguit reporta
> que no pot crear-ne cap** perquè «Publicacions» fa la pantalla negra. La
> funcionalitat de crear està bé; el que falla és el camp. Vegeu la secció 7.

---

## 2. Decisions que respon

| Ref | Pregunta | Resposta de Xavi | Conseqüència |
|-----|----------|------------------|--------------|
| NOU | Cercador general a tot el web? | **No**, amb el d'elements n'hi ha prou | **Tancat.** No es fa cercador global. |
| M6 · T06 | Treure el bloc «Publicacions» del mapa? | **Mantenir-lo.** Proposa valorar un **filtre de temes** com a «En paper» (Èpoques, Arquitectura temàtica, Barris, Art); no ho veu clar | Es manté. Nova tasca **S10**. Cal decidir on s'expliquen aquests grans temes. |
| PR4 · T07 | «Suggerir un canvi»: només fora de Presentació o del tot? | **Només fora de Presentació** (a Contacte) **amb un únic formulari** | Confirmat (ja verificat a #988). |
| P4 · G1 | Distribució de les guies a la portada | **5 · 5 · 3**, però «ho volem plantejar diferent»: tot el bloc de portada es redissenya (P6) | **Substituïda** pel redisseny de portada. Nova tasca **S9**. |
| M2 | Mapa en escala de grisos | **El que ja hi ha** (base discreta + punts amb color) | **Tancat.** |
| M3 | Pins multicolor per a elements de diversos plànols | **Sí**, meitat/meitat o pastís de 3 colors | Nova tasca **S22** (depèn de la paleta). |
| EP3 | Carrusel de portades: infinit o amb final? | **Infinit.** A l'ordinador: amagar la barra, arrossegar amb el cursor, portades més grans | Nova tasca **S11**. Matís a #983: infinit a la portada, **finit a «En paper»** (on hi ha filtres). |
| GR1 · GR2 | Colors dels pins/etiquetes i vermell del web | **Passarà la paleta definitiva per plànol** (pendent seu). Torna a dir que **el filtre del mapa no funciona** | Nova tasca **S23** (paleta) i **S25** (bug del filtre). |
| GR3 | Tipografia del web | **Proposeu 2-3 opcions d'ús lliure** | Nova tasca **S24**. |
| G1 | Amplada de la columna de text | **La més ampla i encara una mica més**; la imatge de l'edifici, a l'esquerra del títol, ~1/3 de l'ample (#992) | Nova tasca **S15**. |
| MIG-1 | Navas 238 / 240: fitxa genèrica | **Redirigir la genèrica a la 240**; les altres dues, **eliminar** | Nova tasca **S18**. |
| MIG-2 | Casa unifamiliar de plaça Mons | **És l'edifici de Churruca i Rodríguez Arias**; fitxa ara «Lluís Barangé», ubicació corregida. L'altra (Duran i Reynals) **és un error** | Nova tasca **S19**. |
| MIG-3 | Pavelló de la República | **Sí, fusionar** en una sola fitxa | Nova tasca **S20**. |
| A1 | Ordenació d'arquitectes per cognom | **Afegir camp «cognom»** i ordenar-hi. **Dubte:** si editen noms/cognoms al CMS, es trenca el vincle amb els edificis? | Nova tasca **S21** (cal respondre el dubte). |

---

## 3. Canvis comentats que NO tanquen

| Ref | Què | Comentari de Xavi | Acció |
|-----|-----|-------------------|-------|
| M6 | Cercador del mapa: filtra pins i mostra resultats | «Ara és xulíssim!», però **els punts amagats segueixen sent clicables** i es cliquen per error | **S25** (bug UX) |
| EP1–EP8 | Redisseny «En paper» | Carrusel més fluid a l'ordinador, arrossegar, fletxes/mitja portada, canvis de títols («Plànols-guia publicats», «Filtra per agrupacions temàtiques», «Usos», «Tots els plànols-guia en detall»), portada gran, menys espai, sense any | **S11**, **S12** |
| M5 | Botó (i) als temes transversals | «Perfecte!», però la **«i» no ha de tenir color**; hover tot en gris | **S13** |
| F6 | Fotos en blanc i negre | Sense consens; deixar com està. Exploren **color parcial** (patrimoni industrial amb vermell) | **S14** (equip) |
| P6 | Navegació per blocs a la portada | Replanteja la portada: **3 blocs imantats**, sense capçalera, 1) logo+frase+botó, 2) mapa a sang sense filtres+botó «Veure filtres i cercar», 3) carrusel+botó «Veure tots els plànols-guia»+peu; **peu en un sol bloc** | **S9** (portada) |
| G1 | Alineació logo/menú amb el cos | Vol **més amplada central**, menys blanc als costats | **S9** |
| ENQ-lectura | Lectura en veu alta | Alinear a la dreta; dubte sobre la veu | **S16** |
| PR1 | Xifres del projecte | Revisar anys (1400-2026 vs s. XIV-2026); depèn de les fitxes | **S17** |
| G2·G3·F7 | T01–T03 terminologia/ordre/menú | «Genial!» + **icones mòbil** (la de mapa → En paper; pin clàssic al mapa) | **S13** / R10 ja fet |
| M4 | T05 sense difuminat en seleccionar plànol | Els punts no visibles **segueixen clicables** | **S25** (mateix bug) |
| P5 | T09 portada sense destacats ni recursos | «En un altre lloc ja he fet comentaris» (P6) | **S9** |
| R1 | Filtre del mapa: només elements del plànol triat | «Segueixen presents en la invisibilitat: tot i que no els veiem, són clicables» | **S25** |
| EP3 · R4 | Carrusel infinit i amb arrossegament | Dubte: infinit a la portada, finit a «En paper» | **S11** |
| G1 · R9 | Prova d'amplades de columna | La més ampla; imatge a l'esquerra ~1/3 | **S15** |
| ENQ-autoria | Nom d'arxiu de les imatges | Posar **el nom de la fitxa**, però **no «elglobusvermell»** | **S27** |
| F5 | Arquitectes clicables i any en un sol camp | Treure el camp «arquitectes» repetit; a «intervencions», tipus per defecte «projecte» i arquitecte clicable allà | **S26** |

---

## 4. Temes nous (no eren a l'eina)

### S2 — Fitxes d'elements sense color
- **No** volem faixa de color a les fitxes dels elements.
- **El títol (nom de l'element) tampoc** ha de tenir color.

### S1 — CMS: «Publicacions» deixa la pantalla en negra (CRÍTIC)
- En crear una fitxa nova (**Biblioteca Vall d'Hebron**), en clicar **Publicacions
  → «Selecciona una opció…»** la pantalla es torna negra i no pot seguir editant.
- Passa **exactament igual en fitxes ja creades**.
- **Prioritat màxima.** Vegeu la secció 7 (ja resolt i verificat).

### S3 — «En paper»: cada plànol en dues columnes
- **Portada del plànol en paper + índex de continguts a l'esquerra**.
- **Plànol i textos a la dreta.**
- Els textos **sempre desplegats** (ara hi ha massa clics).
- L'índex esquerre serveix per **navegar pels temes del plànol**.

---

## 5. Errors de traspàs (migració WordPress → Hugo)

Xavi avisa que només ha trobat «els ràpids» i creu que n'hi pot haver més.

| ID | Problema | Detall |
|----|----------|--------|
| S5 | **Foto de la portada del plànol** a moltes biblioteques | En comptes de la foto de l'edifici |
| S6 | Informació **encallada dins l'etiqueta «projecte»** | Passa a biblioteques i, sembla, en altres plànols. Pregunta: **ho fem manualment fitxa per fitxa?** (diu que entén que la IA no ho sap fer) |
| S7 | Camp **adreça atrapat en altres llocs** | En altres fitxes |
| S8 | **No s'ha generat el camp «projecte»** | En algunes fitxes |

Cal fer una **diagnosi de conjunt** abans de decidir manual vs automàtic: quantes
fitxes estan afectades per cada patró. Decisió de fons a **S6**.

---

## 6. Tasques noves derivades (prefix S)

| ID | Tasca | Prioritat | Depèn de |
|----|-------|-----------|----------|
| **S1** | **CMS: corregir «Publicacions» (pantalla negra)** | 🔴 màxima | — (resolta, pendent validar) |
| S2 | Treure faixa de color de les fitxes i el color del títol | 🟠 | — |
| S3 | «En paper»: cada plànol en dues columnes, textos desplegats, índex navegable | 🟠 | — |
| S4 | (reservat) | — | — |
| S5 | Biblioteques: substituir foto de portada del plànol per la de l'edifici | 🟠 | diagnosi |
| S6 | «Projecte»: destriar informació encallada; decidir manual vs automàtic | 🔴 decisió | Xavi |
| S7 | Adreça atrapada en altres camps | 🟡 | diagnosi |
| S8 | Fitxes sense camp «projecte» | 🟡 | diagnosi |
| S9 | Portada: redisseny P6 (3 blocs, mapa a sang, peu unificat, més amplada) | 🟠 | contingut Xavi |
| S10 | Filtre de temes al mapa (Èpoques/Usos/Barris/Art) | 🟡 | Xavi |
| S11 | Carrusel: fluid a l'ordinador, arrossegar, scrollbar, portades grans, infinit/finit | 🟠 | — |
| S12 | «En paper»: canvis de títols i estil de text | 🟠 | — |
| S13 | Temes transversals: la «i» sense color; hover gris | 🟡 | — |
| S14 | Fotos B/N: explorar color parcial al patrimoni industrial | 🟡 | equip |
| S15 | Amplada de columna de text + imatge de l'edifici a l'esquerra | 🟠 | — |
| S16 | Lectura en veu alta: botó a la dreta; revisar la veu | 🟡 | — |
| S17 | Anys de les xifres: 1400-2026 vs s. XIV-2026 | 🟡 | fitxes |
| S18 | MIG-1: eliminar genèrica/errònies de Navas i redirigir a la 240 | 🟡 | — |
| S19 | MIG-2: eliminar fitxa errònia de Duran i Reynals | 🟡 | — |
| S20 | MIG-3: fusionar les dues fitxes del Pavelló de la República | 🟡 | — |
| S21 | A1: camp «cognom» + ordenació; respondre el dubte del vincle | 🟡 | — |
| S22 | M3: pins multicolor (meitat/pastís) | 🟡 | S23 |
| S23 | Paleta definitiva per plànol | 🟡 | Xavi |
| S24 | Tipografia: 2-3 opcions lliures | 🟡 | — |
| S25 | Filtre del mapa: els punts amagats no han de ser clicables | 🔴 bug UX | — |
| S26 | Intervencions: tipus «projecte» per defecte + arquitecte clicable | 🟠 | — |
| S27 | Nom d'arxiu de les imatges: nom de la fitxa, sense «elglobusvermell» | 🟢 | — |

---

## 7. Prioritat: el CMS (S1)

### Símptoma
En crear una fitxa nova, **clicar el camp «Publicacions» obre un desplegable
modal i la pantalla queda negra**, sense poder continuar editant. Passa en
fitxes noves i existents.

### Causa
El camp «Publicacions» és un `select` amb `multiple: true` i **13 opcions**.
Sveltia, quan hi ha més opcions que `dropdown_threshold` (**per defecte 5**),
canvia les caselles de selecció per **una UI de tags amb desplegable
(`<dialog>` modal a pantalla completa**, amb `backdrop-filter`). En alguns
navegadors aquest desplegable es pintava negre i bloquejava l'edició.

Reproduït en local amb Chrome headless i l'API de Test de Sveltia: el camp
obria un `<dialog class="sui modal popup … open active">` de 1440×900.

### Solució aplicada
A `static/admin/cms/config.yml`, camp `publicacions`:

```yaml
dropdown_threshold: 20
```

Així es mostren **caselles de selecció** (la mateixa UI que ja funciona a
«Temes transversals») en comptes del desplegable. També s'ha pujat
`CMS_CACHE_VERSION` a `static/admin/cms/index.html` perquè els editors no
arrosseguin la configuració antiga.

### Verificació
Provat amb Chrome headless contra la **configuració real** (backend canviat a
`test-repo`): el camp «Publicacions» mostra **13 caselles + 4 de Temes
transversals**, **0 combobox i 0 diàlegs**. Es pot crear la fitxa i seleccionar
plànols sense pantalla negra.

**Pendent:** que Joan/Xavi ho validin al navegador real (sobretot si Xavi feia
servir Safari) i, si cal, publicar a staging.

---

## 7b. Resposta al dubte A1 (S21) — el vincle dels arquitectes es trenca?

**Si només s'omple el camp nou «cognom»: NO.** El `title` i l'slug de la pàgina
de l'arquitecte no canvien, i els enllaços de les fitxes (que es calculen a partir
del nom) continuen apuntant al mateix lloc.

**Si es canvia el `title` (nom) de l'arquitecte: SÍ.** L'URL de la seva pàgina
canvia i les fitxes que el citen guarden el nom antic al camp `arquitectes`, de
manera que quedarien enllaços trencats. Per renombrar sense perdre enllaços cal:
1. afegir l'URL antic com a `aliases` de la pàgina de l'arquitecte, i
2. actualitzar el nom a totes les fitxes que el citen (o fer-ho amb un script).

**Recomanació:** no renombrar; fer servir `cognom` només per ordenar. Ja s'ha
afegit el camp al CMS i el llistat d'arquitectes ja ordena per `cognom` quan hi
és (i, si no, pel nom complet).

---

## 8. Proper pas

1. **Publicar la correcció del CMS (S1)** i demanar a Xavi que torni a provar
   de crear la fitxa de la Biblioteca Vall d'Hebron.
2. **Respondre els dubtes** que planteja:
   - A1/S21: els canvis de nom/cognom al CMS trenquen el vincle amb els edificis?
   - S6: manual o automàtic per a les dades encallades a «projecte».
3. **Diagnosi dels errors de traspàs** (S5–S8): comptar fitxes afectades per
   patró abans de tocar-ne cap.
4. **Reenviar les preguntes que encara no ha respost** (vegeu
   `.ai/QUESTIONS-CLIENT.md`).
5. La resta de tasques S, quan hi hagi vistiplau.

---

**Nota de governança:** `.ai/` viu al repositori públic
`112books/guiesbarcelona-elglobusvermell`. Si es prefereix no publicar els
correus sencers, caldria moure `.ai/fonts-xavi/` a `docs/` (repo privat).
