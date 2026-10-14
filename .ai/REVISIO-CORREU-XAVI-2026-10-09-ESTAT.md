# Revisió punt a punt — correu de Xavi (9/10/2026)

**Font:** `.ai/fonts-xavi/2026-10-09-xavi-resposta-revisio.md`
**Objectiu:** repassar cada punt del correu, marcar si està fet i redactar-ne la resposta.

**Llegenda d'estat:**
- ✅ **Fet** (amb evidència: commit / fitxer / pàgina)
- 🟡 **Parcial** (una part feta, una altra pendent)
- ⏳ **Pendent** (factible, sense decisió pendent)
- ❓ **Cal decisió** (Joan o Xavi)
- ✔️ **Ja estava fet / verificat** (no requereix acció)

---

## A. Nous temes

| # | Punt de Xavi | Estat | Evidència | Resposta proposada |
|---|--------------|-------|-----------|--------------------|
| A1 | Sense **faixa de color** a les fitxes ni color al **títol** | ✅ Fet | `2b6bbd8`; `themes/.../elements/single.html` i `main.css` | «Fet: fora la faixa de color i el títol en color neutre.» |
| A2 | **CMS**: clicar «Publicacions» deixava la **pantalla negra** | ✅ Fet (per validar) | `755e2ae`; `dropdown_threshold: 20` + cache. Verificat amb Chrome headless | «Corregit: el desplegable s'ha canviat per caselles de selecció. Torna-ho a provar, si us plau.» |
| A3 | «En paper»: cada plànol en **dues columnes** (portada+índex esq., plànol+textos dreta), textos desplegats | ⏳ Pendent | És **S3**; disseny gran, no fet | «Ho tenim pendent; proposem dissenyar-ho i ensenyar-te una prova abans d'implementar-ho.» |

## B. Errors de traspàs

| # | Punt de Xavi | Estat | Evidència | Resposta proposada |
|---|--------------|-------|-----------|--------------------|
| B1 | Biblioteques: surt la **foto de la portada del plànol** | ✅ Comprovat (13/10) | Hash MD5 de les 50 biblioteques: **0 amb foto igual a la portada** (les 33 es van treure el 18/8). 6 sense cap `foto` → no mostren imatge | «Comprovat: cap biblioteca mostra la portada del plànol. Queden 6 sense foto (Bon Pastor, Canyelles, Ateneu Barcelonès, Les Roquetes, Vallcarca i Fort Pienc); cal una foto real.» |
| B2 | Informació **encallada dins «projecte»**; manual o automàtic? | ❓ Decisió | Diagnosi: 31 `projecte_text`, 19 `edifici_original`, 12 `intervencions.any` no numèrics | «Et proposem: neteja automàtica del que és clar + revisió manual de la resta. Ho decidim?» |
| B3 | Camp **adreça atrapat en altres llocs** | 🟡 Informe llest (13/10) | `806f5e7`: **25 adreces** amb ` | ` final netejades; **informe de 85 candidats: 36 duplicats clars + 49 a mà** a `.ai/informe-adreces-descripcio-2026-10-13.md` | «Hem preparat la llista d'adreces dins del text; la netegem quan ens ho digueu.» |
| B4 | Algunes fitxes **sense camp projecte** | ⏳ Pendent | Diagnosi feta; omplir dades requereix decisió B2 | «És part del mateix lot de dades que decidim a B2.» |

## C. Decisions respostes

| # | Punt de Xavi | Estat | Evidència | Resposta proposada |
|---|--------------|-------|-----------|--------------------|
| C1 | [NOU] Cercador general? **No** | ✔️ Resolt | — | «Anotat: no fem cercador general.» |
| C2 | [M6] Mantenir bloc «Publicacions» + **filtre de temes** | ⏳ Decisió | **S10**; avui no hi és | «El mantenim. Sobre el filtre de temes: ens dius on situar-lo i el valorem.» |
| C3 | [PR4] Suggerir canvi només fora de Presentació, **un sol formulari** | ✔️ Verificat | A Contacte; R11 verificat | «Fet, tal com demanaves.» |
| C4 | [ENQ-autoria] verificat | ✔️ | — | «Perfecte.» |
| C5 | [P4·G1] 5·5·3 (replantejat per P6) | ⏳ Decisió | Es resol amb el redisseny de portada **S9** | «Ho integrem al nou disseny de portada.» |
| C6 | [M2] Mapa en grays: el que ja hi ha | ✔️ Resolt | — | «Ho deixem com està.» |
| C7 | [M3] Pins multicolor **sí** | ⏳ Pendent | **S22**, depèn de la paleta (**S23**) | «Ho fem tan bon punt tinguem la paleta.» |
| C8 | [EP3] Carrusel **infinit** + amagar scrollbar / arrossegar / portades grans | 🟡 Fet tècnicament (13/10) | Infinit, arrossegament i scrollbar amagat ja hi eren; **afegides fletxes, portades més grans i mides responsives** (`?ample`, proves) — pendent vist-i-plau visual | «L'infinit, l'arrossegament i les fletxes ja funcionen; mira com queden les portades.» |
| C9 | [GR1·GR2] Paleta definitiva + **el filtre del mapa no funciona** | 🟡 | Paleta **S23** espera Xavi; **filtre**: arreglat **S25** (`2b6bbd8`) | «El filtre ja està corregit; esperem la paleta per aplicar colors.» |
| C10 | [GR3] **Tipografia**: 2-3 opcions lliures | 🟡 Propostes fetes (13/10) | `.ai/informe-tipografia-2026-10-13.md`: 3 opcions OFL (Instrument Sans, Public Sans, Space Grotesk) | «Aquí tens 3 propostes d'ús lliure: mira-les i tria'n una; l'apliquem de seguida.» |
| C11 | [G1] Amplada de columna de text | ⏳ **Pendent (tria Xavi)** | Prova `?ample=1\|2\|3` (13/10), **ara a tot el web i cada opció amb el contingut alineat amb header i peu**: **a) com estava** = 52 rem · **b) més ample** = 64 rem · **c) la més ampla** = `min(110rem, 96vw)` i contenidor a 96vw (quasi sense marges). Fora la variant estreta. Defecte: 64 rem | «Tres opcions: actual, més ample i la més ampla amb pocs marges. Tria quina deixem per defecte.» |
| C12 | [MIG-1] Navas: redirigir genèrica a la 240 | ✅ Fet | `5ac617a`: eliminades genèrica i 238, redirigides | «Fet: queda només la 240 (Casa Nativitat Vedruna).» |
| C13 | [MIG-2] Plaça Mons | ✅ Fet | `5ac617a`: eliminada «Casa unifamiliar» (Duran i Reynals) | «Fet: queda Casa Lluís Barangé.» |
| C14 | [MIG-3] Pavelló de la República: fusionar | ✅ Fet | `5ac617a`: fusionades en una sola fitxa | «Fet: una sola fitxa.» |
| C15 | [A1] Camp **cognom** i ordenar | ✅ Fet | `598c117`, `a712805`, `5410706`; CMS + ordenació + resposta al dubte | «Camp afegit i llistat ordenat per cognom. Dubte resolt: si només ompliu «cognom», no es trenca cap vincle.» |

## D. Canvis fets (comentaris)

| # | Punt de Xavi | Estat | Evidència | Resposta proposada |
|---|--------------|-------|-----------|--------------------|
| D1 | [M6] Cercador del mapa; els punts amagats **segueixen clicables** | ✅ Fet | `2b6bbd8`: punts filtrats no clicables ni enfocables | «Corregit: els punts amagats ja no es poden clicar.» |
| D2 | [EP1–EP8] Carrusel més fluid; títols; «Usos»; portada gran; sense any; menys espai | 🟡 Fet tècnicament (13/10) | `2b6bbd8`: **títols, «Usos», anys i portada gran fets**. **Fletxes i mides afegides** (13/10); fluiditat millorada amb desplaçament suau — pendent vist-i-plau visual | «Hem afegit fletxes visibles i portades més grans; mira si ara és prou fluid.» |
| D3 | [M5] La «i» dels temes sense color | ✅ Fet | `2b6bbd8`: la «i» usa gris neutre | «Fet: la «i» ara és grisa.» |
| D4 | [F6] Fotos B/N: explorar color parcial | ⏳ Equip | **S14** | «Ho deixem en blanc i negre i seguim explorant el color al patrimoni industrial.» |
| D5 | [P7] Splash mòbil | ✔️ OK | — | «Perfecte, gràcies.» |
| D6 | [P6] Portada per blocs (mapa a sang, capçalera fora, peu unificat) | 🟡 Proposta en proves (revertida 13/10) | **Fora la barra «Inici/Guies/Mapa» i salt de scroll: sí, en producció.** El redisseny complet (hero, mapa a sang, carrusel, capçalera fora, peu unificat) està fet però **revertit temporalment** per polir-lo abans de publicar (branca `portada-s9-revisio`) | «Tenim la portada nova muntada i funcionant; la revisem i arreglem abans de deixar-la, i us la ensenyem.» |
| D7 | [G1] **Menys espai blanc a cada banda** | 🟡 Parcial | Amplada de text feta (C11); contenidor central pendent | «Hem ampliat la columna de text; revisem també l'amplada central.» |
| D8 | [ENQ-lectura] Botó d'escoltar a la dreta | ✔️ OK | Ja fet (R7) | «Fet.» |
| D9 | [ENQ-lectura] dubte sobre **la veu** | ⏳ Informatiu | No és codi | «La veu la genera el navegador; en parlem i mirem alternatives.» |
| D10 | [PR1] Anys de les xifres (1400-2026 vs s. XIV-2026) | 🟡 Analitzat (13/10) | **El més antic és s. XI (any 1000)**, no 1400: `.ai/informe-anys-xifres-2026-10-13.md` amb 5 opcions | «Les dades diuen s. XI; quina opció vols que posem?» |
| D11 | [G2·G3·F7] T01–T03 + icones mòbil | ✔️ OK | R10 verificat | «Fet.» |
| D12 | [M1] T04 zoom | ✔️ OK | — | «Fet.» |
| D13 | [M4] T05 punts amagats clicables | ✅ Fet | `2b6bbd8` (mateix que D1) | «Corregit.» |
| D14 | [M6] T06 abecedari eliminat | ✔️ OK | — | «Fet.» |
| D15 | [PR4] T07 suggerir correcció | ✔️ OK | — | «Fet.» |
| D16 | [A2] T08 llistat arquitecte | ✔️ OK | — | «Fet.» |
| D17 | [P5] T09 portada sense destacats | ⏳ Decisió | Es resol amb **S9** (sense índex «Inici/Guies/Mapa» i amb salt de scroll) | «Ho integrem al nou disseny de portada.» |
| D18 | [FU1] CMS crear fitxes | ✅ Fet (amb A2) | `755e2ae` | «Ja pots tornar a provar de crear la fitxa de la Vall d'Hebron.» |
| D19 | [R1] Filtre del mapa | ✅ Fet | `2b6bbd8` | «Corregit.» |
| D20 | [EP3·R4] Carrusel infinit/arrossegament; infinit a portada i finit a «En paper»? | ✅ Fet (13/10) | **Infinit a la portada i finit a «En paper»**; fletxes i portades grans a tots dos | «Fet: infinit a la portada i finit a En paper, tal com demanaves.» |
| D21 | [P7·R6] Splash | ✔️ OK | — | «Genial.» |
| D22 | [ENQ-lectura·R7] Botó escoltar a la dreta | ✔️ OK | — | «Fet.» |
| D23 | [G2·G3·F7·R10] Icones mòbil | ✔️ OK | — | «Fet.» |
| D24 | [GR2] Vermell → gris fosc | ✔️ OK | — | «Fet.» |
| D25 | [M5·R2] Temes transversals: pàgina pròpia + mapa | ✔️ OK | — | «Fet.» |
| D26 | [T07·R11] Un sol formulari a Contacte | ✔️ OK | — | «Fet.» |
| D27 | [ENQ-autoria] CC BY-NC 4.0 | ✔️ OK | — | «Fet.» |
| D28 | [G1·R9] Amplada de text | ⏳ **Pendent (tria Xavi)** | `baseof`: 1 actual (52) · 2 més ample (64) · 3 la més ampla (pocs marges) | «Mira les tres opcions i ens dius quina deixem per defecte.» |
| D29 | [ENQ-autoria] Nom d'arxiu de les fotos descarregades | ✅ Fet | `2b6bbd8`: nom = nom de la fitxa, sense «elglobusvermell» | «Fet.» |
| D30 | [C2] Contacte editable al CMS | ✔️ OK | — | «Fet.» |
| D31 | [F5] Arquitectes clicables i any en un sol camp | 🟡 Parcial | `598c117`/`a712805`: tipus «Projecte» per defecte i **autors clicables**; falta **retirar el camp «arquitectes» duplicat** (migració de dades, B2) | «Els arquitectes de les intervencions ja són clicables i «projecte» surt per defecte. El camp repetit l'eliminem quan netegem les dades.»

---

## Punts recuperats (correus anteriors, no tancats)

| # | Punt de Xavi | Estat | Evidència | Resposta proposada |
|---|--------------|-------|-----------|--------------------|
| P8 | (30/9) «No ens convencen les pastilles negres. Preferim prescindir de pastilles» | ✅ Fet (13/10, aprovat per Joan) | Blocs «hero» i «mapa» de la portada sense fons negre: fons del web, text fosc, separats amb línia | «Fet: hem tret les pastilles negres de la portada.» |

## Notes verbals (no són al correu)

- **Portada (13/10, dit de viva veu):** Xavi diu que **no calen les opcions «Inici / Guies / Mapa»** i que el que vol és un **efecte de salt en fer scroll** — concretament **scroll snapping amb `proximity`** (magnètic però flexible), no `mandatory`. S'integra a **S9** (files **D6** i **D17**).

---

## Proves fetes (13/10, tarda)

- ✅ **Portada-test**: creada la pàgina **`/portada-test/`** amb la proposta S9 (hero + mapa a sang + carrusel + xifres) i **salt de scroll `proximity`**. El mapa s'ha provat amb Chrome headless: **656 pins i tiles carregats**, sense errors de JS.
- ✅ **P4·G1 5·5·3**: aplicat a la **portada actual** (graella de guies a 5 columnes; 4/3/2 als breakpoints petits), perquè no quedi cap guia despenjada.
- ✅ **Tauler de revisió**: nova decisió **`fitxa-arquitectes-projecte`** sobre la **duplicitat «Arquitectes» / «Projecte»** (212 de 658 fitxes) perquè en Xavi decideixi.
- ✅ **Mapa a tot l'ample** a `/portada-test/`: s'ha tret el `max-width` i el padding del `<main>` en aquesta pàgina.
- ✅ **Logo sencer a la portada actual**: la primera secció ja no és objectiu de `scroll-snap`, així que en carregar no es desplaça i el header no surt reduït.
- ✅ **Tauler**: afegida la tasca **`enllacos-proves-tauler`** perquè les proves (amplades, tipografia i portades) siguin accessibles des del document de revisió.
- 📄 **Mail preparat per a Xavi**: `docs/2026-10-14-mail-xavi-portades.md` (explica les propostes de portada i els enllaços).

---

## Enviat a Xavi (13/10) — NO repetir

**Correu enviat** (text literal a `docs/2026-10-13-mail-xavi-enviat-revisio-9oct.md`). Ja explicat:
- **Amplada de text** (`?ample=1|2|3`).
- **Carrusel d'«En paper»**: fletxes, portades més grans, infinit a la portada i finit a «En paper».
- **Fora les pastilles negres** de la portada (P8).
- **Biblioteques**: 50 fitxes comprovades, 6 sense foto.
- **Arquitectes coautors del GATCPAC** enllaçats.
- **Bibliografies**: 8 títols amb enllaç.
- **Portada nova en tres blocs** (en preparació, no publicada).
- **Pendent de decisió**: amplada, tipografia, anys de les xifres, paleta i «En paper» a dues columnes.

El **mail de canvis** (`docs/2026-10-14-mail-xavi-canvis.md`) s'ha retallat perquè no repeteixi res d'això.

---

## Resum

- ✅ **Fets en aquest lot:** A1, A2, C3, C12–C15, D1, D2 (part títols), D3, D13, D18, D19, D20 (base), D29, D31 (part).
- ⏳ **Pendent de triar (Xavi):** C11 i D28 (amplada: actual / més ample / la més ampla) i **D6/D17** (portada: fora «Inici/Guies/Mapa» + efecte de salt en scroll).
- ❓ **Pendents de decisió:** A3, B2, C2, C5, D6 (nota verbal: fora índex + salt de scroll), D17, D31 (resta).
- 🟡 **Parcials a acabar:** B1, B3, C8, C9, D2, D7, D20.
- ⏳ **Pendents de fer:** B4, C7, C10, D4, D9, D10.
- ✔️ **Ja estaven fets/verificats:** C1, C4, C6, D5, D8, D11, D12, D14, D15, D16, D21–D27, D30.

**Proper pas proposat:** repassar aquest document secció a secció (A → D) i, per cada ⏳/❓, decidir si ho fem ara o ho deixem anotat; amb això muntem el correu de resposta.

---

## Tauler actualitzat (14/10)

- `static/admin/revisio/tasques.json` posat al dia amb la ronda del 9/10: respostes de Xavi a 9 decisions (cercador, 5·5·3, mapa grisos, tipografia, Navas, Mons, Pavelló, cognom, Publicacions), 8 canvis nous del 10/10 (CMS, faixa, punts filtrats, «i» grisa, En paper, duplicats, intervencions, cognom), ítems desfasats corregits (nom d'arxiu, amplades a/b/c, portada de prova) i 3 tasques noves (A3 dues columnes, B2/B4 dades «projecte», F6 color parcial).
- Tasca `enllacos-proves-tauler` feta: totes les proves enllaçades des del tauler.
- **Biblioteca Vall d'Hebron:** Xavi la va crear el 9/10 (`115e869`) però va quedar sense `publicacions` ni adreça (just on es bloquejava el CMS). Al mail: «completeu-la», no «creeu-la».

## Loop de tasques (14/10, migdia) — aprovat per Joan

| # | Tasca | Resultat | Commit |
|---|---|---|---|
| 1 | Duplicitat «Arquitectes» / «Projecte» (S26, D31) | Origen: demanat per Xavi el 31/8, revisat el 9/10. 212 fitxes amb la fila repetida; 10 amb noms escrits diferent. Prova `?projecte=1` (amaga la fila, no toca dades). Decisió al tauler sense l'opció d'esborrar dades. Informe: `.ai/informe-arquitectes-projecte-2026-10-14.md` | `a3e6d49`, `bf5546c` |
| 2 | Informació encallada a «projecte» (B2/B4) | `scripts/proposa-neteja-projecte.py` (només lectura): 154 fitxes, 194 casos → 103 AUTO, 45 REVISA, 46 MANUAL. Informe: `.ai/informe-neteja-projecte-2026-10-14.md`. **No aplicat.** | `…` (docs traspàs) |
| 3 | Coordenades 10b | Ja correctes des del 29/7 (`5dc20ca`); verificades amb OSM. `casa-unifamiliar` resolta el 10/10. Cap canvi | — (full de ruta) |
| 4 | Pins multicolor (M3/R3) | Prova `/mapa/?pins=multicolor`: 27 punts, 18 combinacions, pin partit en meitats o pastís (patrons SVG) | `b1420a5` |
| 5 | «En paper» dues columnes (A3/S3) | Prova `?columnes=1` a cada plànol: portada + índex fix (h2) a l'esquerra; mapa + textos desplegats a la dreta | `b28523a` |

Pendent de decisió de Xavi per a tot el lot (enllaços al tauler). El punt 6 (verificació contra el WP abans del tall) queda aparcat per decisió de Joan.
