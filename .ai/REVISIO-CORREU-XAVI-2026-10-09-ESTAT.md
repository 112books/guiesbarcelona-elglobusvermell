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
| B1 | Biblioteques: surt la **foto de la portada del plànol** | 🟡 Diagnosi | `.ai/DIAGNOSI-TRASPAS-2026-10.md`: 6 de 50 biblioteques sense `foto` | «Hem detectat 6 fitxes sense foto; cal revisar-les una a una per veure d'on surt la imatge.» |
| B2 | Informació **encallada dins «projecte»**; manual o automàtic? | ❓ Decisió | Diagnosi: 31 `projecte_text`, 19 `edifici_original`, 12 `intervencions.any` no numèrics | «Et proposem: neteja automàtica del que és clar + revisió manual de la resta. Ho decidim?» |
| B3 | Camp **adreça atrapat en altres llocs** | 🟡 Parcial | `806f5e7`: **25 adreces** amb ` | ` final netejades; extreure adreces de `descripcio` (31) pendent | «Hem netejat 25 adreces; la resta (adreces dins del text) les podem extreure automàticament i revisar.» |
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
| C10 | [GR3] **Tipografia**: 2-3 opcions lliures | ⏳ Pendent | **S24** | «T'enviem 2-3 propostes d'ús lliure per triar.» |
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
| D6 | [P6] Portada per blocs (mapa a sang, capçalera fora, peu unificat) | 🟡 Parcial | **Fet (13/10, `9167af7`):** fora la barra «Inici/Guies/Mapa» i salt de scroll (scroll-snap) entre els tres blocs a pantalla completa. Resta de S9 (mapa a sang, peu unificat) pendent. **Nota verbal (13/10):** no calen les opcions «Inici / Guies / Mapa»; vol un **efecte de salt en fer scroll** (que se sentin tres apartats) | «Ho tenim: fora l'índex i amb efecte de salt entre els tres blocs. T'ensenyem una prova.» |
| D7 | [G1] **Menys espai blanc a cada banda** | 🟡 Parcial | Amplada de text feta (C11); contenidor central pendent | «Hem ampliat la columna de text; revisem també l'amplada central.» |
| D8 | [ENQ-lectura] Botó d'escoltar a la dreta | ✔️ OK | Ja fet (R7) | «Fet.» |
| D9 | [ENQ-lectura] dubte sobre **la veu** | ⏳ Informatiu | No és codi | «La veu la genera el navegador; en parlem i mirem alternatives.» |
| D10 | [PR1] Anys de les xifres (1400-2026 vs s. XIV-2026) | ⏳ Pendent | **S17**, lligat a les fitxes | «Ho revisem quan normalitzem les dades.» |
| D11 | [G2·G3·F7] T01–T03 + icones mòbil | ✔️ OK | R10 verificat | «Fet.» |
| D12 | [M1] T04 zoom | ✔️ OK | — | «Fet.» |
| D13 | [M4] T05 punts amagats clicables | ✅ Fet | `2b6bbd8` (mateix que D1) | «Corregit.» |
| D14 | [M6] T06 abecedari eliminat | ✔️ OK | — | «Fet.» |
| D15 | [PR4] T07 suggerir correcció | ✔️ OK | — | «Fet.» |
| D16 | [A2] T08 llistat arquitecte | ✔️ OK | — | «Fet.» |
| D17 | [P5] T09 portada sense destacats | ⏳ Decisió | Es resol amb **S9** (sense índex «Inici/Guies/Mapa» i amb salt de scroll) | «Ho integrem al nou disseny de portada.» |
| D18 | [FU1] CMS crear fitxes | ✅ Fet (amb A2) | `755e2ae` | «Ja pots tornar a provar de crear la fitxa de la Vall d'Hebron.» |
| D19 | [R1] Filtre del mapa | ✅ Fet | `2b6bbd8` | «Corregit.» |
| D20 | [EP3·R4] Carrusel infinit/arrossegament; infinit a portada i finit a «En paper»? | 🟡 Parcial | Ja existeix; matís pendent | «Ho deixem infinit a la portada i finit a «En paper», com suggereixes.» |
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

- **Portada (13/10, dit de viva veu):** Xavi diu que **no calen les opcions «Inici / Guies / Mapa»** i que el que vol és un **efecte de salt en fer scroll** (que els tres blocs se sentin com tres apartats). S'integra a **S9** (files **D6** i **D17**).

---

## Resum

- ✅ **Fets en aquest lot:** A1, A2, C3, C12–C15, D1, D2 (part títols), D3, D13, D18, D19, D20 (base), D29, D31 (part).
- ⏳ **Pendent de triar (Xavi):** C11 i D28 (amplada: actual / més ample / la més ampla) i **D6/D17** (portada: fora «Inici/Guies/Mapa» + efecte de salt en scroll).
- ❓ **Pendents de decisió:** A3, B2, C2, C5, D6 (nota verbal: fora índex + salt de scroll), D17, D31 (resta).
- 🟡 **Parcials a acabar:** B1, B3, C8, C9, D2, D7, D20.
- ⏳ **Pendents de fer:** B4, C7, C10, D4, D9, D10.
- ✔️ **Ja estaven fets/verificats:** C1, C4, C6, D5, D8, D11, D12, D14, D15, D16, D21–D27, D30.

**Proper pas proposat:** repassar aquest document secció a secció (A → D) i, per cada ⏳/❓, decidir si ho fem ara o ho deixem anotat; amb això muntem el correu de resposta.
