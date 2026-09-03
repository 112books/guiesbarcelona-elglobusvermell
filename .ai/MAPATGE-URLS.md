# Mapatge URLs: Producció (WordPress) → Nou projecte (Hugo)

Data: 2026-09-02
Font WP: sitemap.xml viu (post-sitemap.xml, page-sitemap.xml, sitemap-misc.xml)
Font Hugo: content/ca/ (branch main)

**Llegenda:** ✅ URL idèntica · ⚠️ URL canviada (cal redirect) · ❌ Eliminada · 🆕 Nova (sense origen WP)

---

## Resum

| | Total |
|---|---|
| URLs producció WP (fitxes) | 649 |
| URLs producció WP (textos-guia) | 11 |
| URLs producció WP (pàgines estàtiques) | 6 |
| **Total URLs WP** | **666** |
| Elements Hugo (amb alias WP) | 649 |
| Elements Hugo (nous, sense alias) | 11 |
| Publicacions Hugo (amb alias WP) | 11 |
| Publicacions Hugo (noves) | 2 |
| Arquitectes Hugo (col·lecció nova) | 197 |
| Pàgines estàtiques Hugo | ~11 |
| ✅ Idèntiques | 3 (`/`, `/en-paper/`, `/credits/`) |
| ⚠️ Canviades (cobertes per `aliases:` Hugo) | 660 |
| ❌ Eliminades | 2 |
| 🆕 Noves a Hugo sense origen WP | ~221 |

---

## 1. Pàgines estàtiques

| URL WordPress | URL Hugo | Estat | Notes |
|---|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/ | https://guiesbarcelona.elglobusvermell.org/ | ✅ | |
| https://guiesbarcelona.elglobusvermell.org/en-paper/ | https://guiesbarcelona.elglobusvermell.org/en-paper/ | ✅ | |
| https://guiesbarcelona.elglobusvermell.org/credits/ | https://guiesbarcelona.elglobusvermell.org/credits/ | ✅ | |
| https://guiesbarcelona.elglobusvermell.org/politica-de-privadesa/ | https://guiesbarcelona.elglobusvermell.org/legal/privacitat/ | ⚠️ | Sense alias explícit — cal redirect manual |
| https://guiesbarcelona.elglobusvermell.org/arquitectura-i-urbanisme/ | https://guiesbarcelona.elglobusvermell.org/elements/ | ⚠️ | Sense alias explícit — candidat: /elements/ o /mapa/ |
| https://guiesbarcelona.elglobusvermell.org/wp-statistics-honey-pot-page-2021-09-02-105732/ | — | ❌ | Artefacte del plugin WP-Statistics, no migrar |

---

## 2. Textos-guia → Publicacions

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/text/barceloneta/ | https://guiesbarcelona.elglobusvermell.org/publicacions/barceloneta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/biblioteques/ | https://guiesbarcelona.elglobusvermell.org/publicacions/biblioteques/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/gatcpac/ | https://guiesbarcelona.elglobusvermell.org/publicacions/gatcpac/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/interiors-illa/ | https://guiesbarcelona.elglobusvermell.org/publicacions/interiors-illa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/la-marina-del-port-i-del-prat-vermell-passat-i-present/ | https://guiesbarcelona.elglobusvermell.org/publicacions/marina/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/masies/ | https://guiesbarcelona.elglobusvermell.org/publicacions/masies/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/mercats/ | https://guiesbarcelona.elglobusvermell.org/publicacions/mercats/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/poblenou/ | https://guiesbarcelona.elglobusvermell.org/publicacions/poblenou/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/arquitectura-a-barcelona-1975-2008-de-lesperanca-a-la-crisi/ | https://guiesbarcelona.elglobusvermell.org/publicacions/76-08/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/arquitectura-moderna-a-barcelona-1950-1975/ | https://guiesbarcelona.elglobusvermell.org/publicacions/50-75/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/text/arquitectura-a-barcelona-2010-2025-la-revolucio-tranquilla/ | https://guiesbarcelona.elglobusvermell.org/publicacions/09-25/ | ⚠️ |


---

## 3. Fitxes d'edificis / elements

Organitzades per categoria WordPress original.

### 3.1 barceloneta (58 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/barceloneta/antic-montepio-de-sant-pere/ | https://guiesbarcelona.elglobusvermell.org/elements/antic-montepio-de-sant-pere/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/arc-de-la-maquinista-terrestre-i-maritima/ | https://guiesbarcelona.elglobusvermell.org/elements/arc-de-la-maquinista-terrestre-i-maritima/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/bestial/ | https://guiesbarcelona.elglobusvermell.org/elements/bestial/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-de-la-barceloneta-1761/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-de-la-barceloneta-1761/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-esteve-cortada/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-esteve-cortada/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-jaume-cardus/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-jaume-cardus/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-joan-magi/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-joan-magi/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-josep-magret/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-josep-magret/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-josep-torras/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-josep-torras/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-lesseps/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-lesseps/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-lluis-cairo/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-lluis-cairo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-marti-ventosa/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-marti-ventosa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-miquel/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-miquel/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/casa-valenti-puigbo/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-valenti-puigbo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/centre-civic-barceloneta/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-civic-barceloneta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/club-natacio-atletic-barceloneta/ | https://guiesbarcelona.elglobusvermell.org/elements/club-natacio-atletic-barceloneta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/club-natacio-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/club-natacio-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/cooperativa-popular-obrera-el-siglo-xx/ | https://guiesbarcelona.elglobusvermell.org/elements/cooperativa-popular-obrera-el-siglo-xx/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/crescendo-appare/ | https://guiesbarcelona.elglobusvermell.org/elements/crescendo-appare/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/david-i-goliat/ | https://guiesbarcelona.elglobusvermell.org/elements/david-i-goliat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/edifici-dhabitatges/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/edifici-dhabitatges-joan-de-borbo-38/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-joan-de-borbo-38/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/edifici-dhabitatges-joan-de-borbo-50/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-joan-de-borbo-50/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/edifici-dhabitatges-maquinista/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-maquinista/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/edifici-dhabitatges-salamanca/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-salamanca/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/edifici-dhabitatges-sant-carles/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-sant-carles/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/el-negre-de-la-riba/ | https://guiesbarcelona.elglobusvermell.org/elements/el-negre-de-la-riba/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/sant-miquel-del-port/ | https://guiesbarcelona.elglobusvermell.org/elements/esglesia-de-sant-miquel-del-port/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/espina-del-mar/ | https://guiesbarcelona.elglobusvermell.org/elements/espina-del-mar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/evocacio-marinera/ | https://guiesbarcelona.elglobusvermell.org/elements/evocacio-marinera/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/fabrica-del-sol/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-del-sol/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/facultat-de-nautica/ | https://guiesbarcelona.elglobusvermell.org/elements/facultat-de-nautica/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/ferroestructura-numero-5-o-sideroploide-als-homes-de-la-mar/ | https://guiesbarcelona.elglobusvermell.org/elements/ferroestructura-numero-5-o-sideroploide-als-homes-de-la-mar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/font-de-carmen-amaya/ | https://guiesbarcelona.elglobusvermell.org/elements/font-de-carmen-amaya/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/gasometre/ | https://guiesbarcelona.elglobusvermell.org/elements/gasometre/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/homenatge-a-la-natacio/ | https://guiesbarcelona.elglobusvermell.org/elements/homenatge-a-la-natacio/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/hospital-del-mar/ | https://guiesbarcelona.elglobusvermell.org/elements/hospital-del-mar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/hotel-w-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/hotel-w-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/les-quatre-barres-de-la-senyera-catalana/ | https://guiesbarcelona.elglobusvermell.org/elements/les-quatre-barres-de-la-senyera-catalana/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/lestel-ferit/ | https://guiesbarcelona.elglobusvermell.org/elements/lestel-ferit/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/mitgera-dels-objectes/ | https://guiesbarcelona.elglobusvermell.org/elements/mitgera-dels-objectes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/monument-a-josep-moragues/ | https://guiesbarcelona.elglobusvermell.org/elements/monument-a-josep-moragues/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/nereida/ | https://guiesbarcelona.elglobusvermell.org/elements/nereida/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/palau-de-mar-magatzems-generals-de-comerc/ | https://guiesbarcelona.elglobusvermell.org/elements/palau-de-mar-magatzems-generals-de-comerc/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/parc-de-recerca-biomedica-de-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-de-recerca-biomedica-de-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/passeig-maritim-de-la-barceloneta/ | https://guiesbarcelona.elglobusvermell.org/elements/passeig-maritim-de-la-barceloneta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/peix-blau/ | https://guiesbarcelona.elglobusvermell.org/elements/peix-blau/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/peix-daurat/ | https://guiesbarcelona.elglobusvermell.org/elements/peix-daurat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/pla-de-palau-i-passeig-joan-de-borbo/ | https://guiesbarcelona.elglobusvermell.org/elements/pla-de-palau-i-passeig-joan-de-borbo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/rosa-dels-vents/ | https://guiesbarcelona.elglobusvermell.org/elements/rosa-dels-vents/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/sense-titol-balanca-romana/ | https://guiesbarcelona.elglobusvermell.org/elements/sense-titol-balanca-romana/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/simon-bolivar/ | https://guiesbarcelona.elglobusvermell.org/elements/simon-bolivar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/tallers-nuevo-vulcano/ | https://guiesbarcelona.elglobusvermell.org/elements/tallers-nuevo-vulcano/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/torre-daigues-de-la-catalana-de-gas/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-daigues-de-la-catalana-de-gas/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/torre-de-sant-sebastia/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-de-sant-sebastia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/torre-del-rellotge/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-del-rellotge/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/torre-mare-nostrum/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-mare-nostrum/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/barceloneta/una-habitacio-on-sempre-plou/ | https://guiesbarcelona.elglobusvermell.org/elements/una-habitacio-on-sempre-plou/ | ⚠️ |

### 3.2 poblenou-industrial (76 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/acabados-tintes-y-estampados/ | https://guiesbarcelona.elglobusvermell.org/elements/acabados-tintes-y-estampados/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/antic-escorxador/ | https://guiesbarcelona.elglobusvermell.org/elements/antic-escorxador/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/ca-lalier/ | https://guiesbarcelona.elglobusvermell.org/elements/ca-lalier/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/ca-laranyo/ | https://guiesbarcelona.elglobusvermell.org/elements/ca-laranyo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/ca-lilla/ | https://guiesbarcelona.elglobusvermell.org/elements/ca-lilla/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/caldereria-de-joan-feiner/ | https://guiesbarcelona.elglobusvermell.org/elements/caldereria-de-joan-feiner/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-culleres/ | https://guiesbarcelona.elglobusvermell.org/elements/can-culleres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-felipa/ | https://guiesbarcelona.elglobusvermell.org/elements/can-felipa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-framis-fundacio-vila-casas/ | https://guiesbarcelona.elglobusvermell.org/elements/can-framis-fundacio-vila-casas/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-gili-nou/ | https://guiesbarcelona.elglobusvermell.org/elements/can-gili-nou/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-gili-vell/ | https://guiesbarcelona.elglobusvermell.org/elements/can-gili-vell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-jaumandreu-vapor-de-la-llana/ | https://guiesbarcelona.elglobusvermell.org/elements/can-jaumandreu-vapor-de-la-llana/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-pico-biciclot/ | https://guiesbarcelona.elglobusvermell.org/elements/can-pico-biciclot/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-ricart/ | https://guiesbarcelona.elglobusvermell.org/elements/can-ricart/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-saladrigas/ | https://guiesbarcelona.elglobusvermell.org/elements/can-saladrigas/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-tiana-il3-ub/ | https://guiesbarcelona.elglobusvermell.org/elements/can-tiana-il3-ub/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/casino-familiar/ | https://guiesbarcelona.elglobusvermell.org/elements/casino-familiar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/casino-lalianca-del-poblenou/ | https://guiesbarcelona.elglobusvermell.org/elements/casino-lalianca-del-poblenou/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/centre-moral-del-poblenou/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-moral-del-poblenou/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/colores-hispania/ | https://guiesbarcelona.elglobusvermell.org/elements/colores-hispania/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/cooperativa-la-flor-de-maig/ | https://guiesbarcelona.elglobusvermell.org/elements/cooperativa-la-flor-de-maig/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/cooperativa-la-flor-de-maig-sucursal/ | https://guiesbarcelona.elglobusvermell.org/elements/cooperativa-la-flor-de-maig-sucursal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/cooperativa-pau-i-justicia-sala-beckett/ | https://guiesbarcelona.elglobusvermell.org/elements/cooperativa-pau-i-justicia-sala-beckett/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/cotxeres-de-tmb/ | https://guiesbarcelona.elglobusvermell.org/elements/cotxeres-de-tmb/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/cunill-orfebres/ | https://guiesbarcelona.elglobusvermell.org/elements/cunill-orfebres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/edifici-del-rellotge/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-del-rellotge/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/edifici-ricard-ametlla-montana/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-ricard-ametlla-montana/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/el-sucre/ | https://guiesbarcelona.elglobusvermell.org/elements/el-sucre/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/fabrica-dalbert-musteros/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-dalbert-musteros/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/fabrica-de-gel-la-siberia/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-de-gel-la-siberia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/fabrica-de-gel-sant-antoni/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-de-gel-sant-antoni/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/fabrica-de-joan-guell/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-de-joan-guell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/fabrica-de-llorenc-pons-i-clerch/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-de-llorenc-pons-i-clerch/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/letona/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-letona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/fabrica-valls-teixidor-i-jordana/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-valls-teixidor-i-jordana/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/farinera-la-asuncion/ | https://guiesbarcelona.elglobusvermell.org/elements/farinera-la-asuncion/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/farinera-sant-jaume-la-farinera-del-clot/ | https://guiesbarcelona.elglobusvermell.org/elements/farinera-sant-jaume-la-farinera-del-clot/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/frigo-farga/ | https://guiesbarcelona.elglobusvermell.org/elements/frigo-farga/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/galetes-i-xocolata-solsona-i-rius/ | https://guiesbarcelona.elglobusvermell.org/elements/galetes-i-xocolata-solsona-i-rius/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/galetes-vinas-la-galeta/ | https://guiesbarcelona.elglobusvermell.org/elements/galetes-vinas-la-galeta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/habitatges-de-can-culleres/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-de-can-culleres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/hispano-olivetti/ | https://guiesbarcelona.elglobusvermell.org/elements/hispano-olivetti/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/huracan-motors-razzmatazz/ | https://guiesbarcelona.elglobusvermell.org/elements/huracan-motors-razzmatazz/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/industrias-deslite/ | https://guiesbarcelona.elglobusvermell.org/elements/industrias-deslite/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/industrias-metalicas-de-lluis-sabala-paloma-iaac/ | https://guiesbarcelona.elglobusvermell.org/elements/industrias-metalicas-de-lluis-sabala-paloma-iaac/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/industrias-metalicas-sa/ | https://guiesbarcelona.elglobusvermell.org/elements/industrias-metalicas-sa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/industrias-waldes/ | https://guiesbarcelona.elglobusvermell.org/elements/industrias-waldes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/la-ciutat-groga/ | https://guiesbarcelona.elglobusvermell.org/elements/la-ciutat-groga/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/la-escocesa/ | https://guiesbarcelona.elglobusvermell.org/elements/la-escocesa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/la-favorita/ | https://guiesbarcelona.elglobusvermell.org/elements/la-favorita/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/magatzem/ | https://guiesbarcelona.elglobusvermell.org/elements/magatzem/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/magatzem-de-draps-de-francisco-munne-bau/ | https://guiesbarcelona.elglobusvermell.org/elements/magatzem-de-draps-de-francisco-munne-bau/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/magatzem-del-banco-hispano-americano/ | https://guiesbarcelona.elglobusvermell.org/elements/magatzem-del-banco-hispano-americano/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/nau-industrial-modernista/ | https://guiesbarcelona.elglobusvermell.org/elements/nau-industrial-modernista/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/naus-de-la-familia-ametller/ | https://guiesbarcelona.elglobusvermell.org/elements/naus-de-la-familia-ametller/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/naus-industrials-adossades/ | https://guiesbarcelona.elglobusvermell.org/elements/naus-industrials-adossades/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/netol/ | https://guiesbarcelona.elglobusvermell.org/elements/netol/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/olis-pallares/ | https://guiesbarcelona.elglobusvermell.org/elements/olis-pallares/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/palo-alto/ | https://guiesbarcelona.elglobusvermell.org/elements/palo-alto/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/pastes-magin-quer/ | https://guiesbarcelona.elglobusvermell.org/elements/pastes-magin-quer/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/tallers-oliva-artes/ | https://guiesbarcelona.elglobusvermell.org/elements/tallers-oliva-artes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/torre-de-les-aigues-del-besos/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-de-les-aigues-del-besos/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/tules-y-encajes/ | https://guiesbarcelona.elglobusvermell.org/elements/tules-y-encajes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/union-metalurgica/ | https://guiesbarcelona.elglobusvermell.org/elements/la-union-metalurgica/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/vapor-llull/ | https://guiesbarcelona.elglobusvermell.org/elements/vapor-llull/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-folch/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia-de-can-folch/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/xemeneia/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/xemeneia-de-buigas-i-samso/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia-de-buigas-i-samso/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/xemeneia-de-can-girona-macosa/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia-de-can-girona-macosa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/xemeneia-de-la-foneria-giralt/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia-de-la-foneria-giralt/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/xemeneia-de-la-nubiola/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia-de-la-nubiola/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/xemeneia-de-la-ram/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia-de-la-ram/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/xemeneia-de-lelectrolisis/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia-de-lelectrolisis/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/xemeneia-de-tallada-i-lora/ | https://guiesbarcelona.elglobusvermell.org/elements/xemeneia-de-tallada-i-lora/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/yorka-abans-apresto-de-sederias/ | https://guiesbarcelona.elglobusvermell.org/elements/yorka-abans-apresto-de-sederias/ | ⚠️ |

### 3.3 mercats (42 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/mercats/boqueria/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-boqueria/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/biblioteca-fort-pienc/ | https://guiesbarcelona.elglobusvermell.org/elements/illa-dequipaments-fort-pienc/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/born/ | https://guiesbarcelona.elglobusvermell.org/elements/el-born-muhba-mercat-del-born/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-canyelles/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-canyelles/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-ciutat-meridiana/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-ciutat-meridiana/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-felip-ii/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-felip-ii/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-galvany/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-galvany/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-barceloneta-2/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-barceloneta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-concepcio/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-concepcio/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-guineueta/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-guineueta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-llibertat/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-llibertat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-marina/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-marina/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-merce/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-merce/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-montserrat/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-montserrat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-sagrada-familia/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-sagrada-familia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-trinitat/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-trinitat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-la-vall-dhebron-teixonera/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-la-vall-dhebron-teixonera/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-les-corts/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-les-corts/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-les-tres-torres/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-les-tres-torres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-lesseps/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-lesseps/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-lestrella/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-lestrella/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-nuria/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-nuria/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-provencals/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-provencals/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-sant-andreu/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-sant-andreu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-sant-antoni/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-sant-antoni/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-sant-gervasi/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-sant-gervasi/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-sant-marti/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-sant-marti/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-sants/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-sants/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-de-sarria/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-sarria/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-del-besos/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-del-besos/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-del-bon-pastor/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-del-bon-pastor/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-del-carmel/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-del-carmel/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-del-clot/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-del-clot/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-del-guinardo/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-del-guinardo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-del-ninot/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-del-ninot/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-del-poblenou/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-del-poblenou/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-delabaceria/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-delabaceria/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-dels-encants-fira-de-bellcaire/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-dels-encants-fira-de-bellcaire/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-dhorta/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-dhorta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/mercat-dhostafrancs/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-dhostafrancs/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/placa-i-mercat-de-la-marina/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-i-mercat-de-la-marina/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/mercats/santa-caterina/ | https://guiesbarcelona.elglobusvermell.org/elements/mercat-de-santa-caterina-i-habitatges-per-ancians/ | ⚠️ |

### 3.4 biblioteques (47 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-bon-pastor/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-bon-pastor-josefina-castellvi/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-camp-de-larpa-caterina-albert/ | https://guiesbarcelona.elglobusvermell.org/elements/illa-dequipaments-alchemika/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-canyelles/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-canyelles-maria-angels-rivas/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-clara/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-clara/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-collserola-josep-miracle/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-collserola-josep-miracle/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-crai-de-la-ciutadella-diposit-de-les-aigues-universitat-pompeu-fabra/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-crai-de-la-ciutadella-diposit-de-les-aigues-universitat-pompeu-fabra/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-de-catalunya/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-de-catalunya/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-de-lateneu-barcelones/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-de-lateneu-barcelones/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-el-carmel-juan-marse/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-el-carmel-juan-marse/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-el-clot-josep-benet/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-el-clot-josep-benet/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-esquerra-de-leixample-agusti-centelles/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-collage-centre-cultural-teresa-pamies/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-francesc-candel/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-francesc-candel/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-francesca-bonnemaison/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-francesca-bonnemaison/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-gotic-andreu-nin/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-gotic-andreu-nin/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-guinardo-merce-rodoreda/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-guinardo-merce-rodoreda/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-horta-can-mariner/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-horta-can-mariner/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-ignasi-iglesias-can-fabra/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-ignasi-iglesias-can-fabra/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-jaume-fuster/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-jaume-fuster/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-joan-miro/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-joan-miro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-la-fraternitat/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-la-fraternitat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-la-marina-del-prat-vermell/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-la-marina-del-prat-vermell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-la-sagrera-marina-clotet/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-la-sagrera-marina-clotet/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-les-corts-miquel-llongueras/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-les-corts-miquel-llongueras/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-les-roquetes/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-les-roquetes-rafa-juncadella/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-montbau-albert-perez-baro/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-montbau-albert-perez-baro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-montserrat-abello/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-montserrat-abello/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-nou-barris/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-nou-barris-aurora-diaz-plaja/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-poble-sec-francesc-boix/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-poble-sec-francesc-boix/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-poblenou-manuel-arranz/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-poblenou-manuel-arranz/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-prosperitat-ideal-plastica-flor/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-prosperitat-ideal-plastica-flor/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-publica-arus/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-publica-arus/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-publica-de-lestat-a-barcelona-biblioteca-central-de-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-publica-de-lestat-a-barcelona-biblioteca-central-de-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-ramon-dalos-moner/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-ramon-dalos-moner/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-sagrada-familia-josep-maria-ainaud-de-lasarte/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-sagrada-familia-josep-maria-ainaud-de-lasarte/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-sant-gervasi-joan-maragall/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-sant-gervasi-joan-maragall/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-sant-gervasi-sud/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-sant-gervasi-sud/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-sant-marti-de-provencals/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-gabriel-garcia-marquez/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-sant-pau-santa-creu/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-sant-pau-santa-creu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-sarria-j-v-foix/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-sarria-j-v-foix/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-sofia-barat/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-sofia-barat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-trinitat-vella-j-barbero/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-trinitat-vella-jose-barbero/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-vallcarca-i-els-penitents-m-antonieta-cot/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-vallcarca-i-els-penitents-maria-antonieta-cot/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-vapor-vell/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-vapor-vell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-vila-de-gracia/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-vila-de-gracia-rosa-maria-arquimbau/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-vilapicina-i-la-torre-llobeta/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-vilapicina-i-la-torre-llobeta-carmen-laforet/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-xavier-benguerel/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-xavier-benguerel/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-zona-nord/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-zona-nord-maria-sanchez/ | ⚠️ |

### 3.5 masies (86 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-la-figuera/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-la-figuera/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-la-marquesa/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-la-marquesa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-la-xica/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-la-xica/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-lagusti/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-lagusti/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-larno/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-larno/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-lestruch/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-lestruch/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-nandalet/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-nandalet/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-narmera/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-narmera/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-nartes/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-nartes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-ca-nensenya/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-ca-nensenya/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-cal-cervera/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-cal-cervera/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-baliarda/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-baliarda/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-baro/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-baro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-baste/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-baste/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-bruixa/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-bruixa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-cadena/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-cadena/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-canals/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-canals/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-canet-de-la-riera/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-canet-de-la-riera/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-carabassa/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-carabassa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-carreras/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-carreras/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-castello/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-castello/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-cortada/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-cortada/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-cros/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-cros/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-fargues/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-fargues/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-figuerola/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-figuerola/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-garcini/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-garcini/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-gardenyes/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-gardenyes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-gras/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-gras/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-joanet-del-borni/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-joanet-del-borni/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-laietos/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-laietos/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-llupia/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-llupia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-manen/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-manen/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-marcet/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-marcet/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-mascaro/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-mascaro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-masdeu/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-masdeu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-melic/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-melic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-mestres-2/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-mestres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-miralletes/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-miralletes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-mora/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-mora/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-muntaner/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-muntaner/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-papanaps/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-papanaps/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-piteu/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-piteu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-planes/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-planes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-planes-la-masia/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-planes-la-masia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-pomaret/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-pomaret/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-ponsic/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-ponsic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-prats/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-prats/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-querol/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-querol/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-raspall/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-raspall/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-raventos/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-raventos/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-riera/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-riera/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-ros/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-ros/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-ros-de-mayol/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-ros-de-mayol/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-roses/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-roses/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-santgenis/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-santgenis/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-senillosa/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-senillosa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-sert/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-sert/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-sitjar-gran/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-sitjar-gran/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-soler/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-soler/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-travi-nou/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-travi-nou/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-travi-vell/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-travi-vell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-trilla/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-trilla/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-tusquets/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-tusquets/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-valent/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-valent/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-verdaguer/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-verdaguer/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-can-xipreret/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-xipreret/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-granja-montserrat/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-granja-montserrat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-masoveria-de-can-safont/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-i-masoveria-de-can-safont/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-la-granja-vella/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-la-granja-vella/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-la-petita-maria/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-la-petita-maria/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-les-carasses/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-les-carasses/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-mas-enric/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-mas-enric/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-mas-guinardo/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-mas-guinardo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-mas-teixidor/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-mas-teixidor/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-masoveria-de-la-virreina/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-masoveria-de-la-virreina/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-rectoria-de-sant-genis-dels-agudells/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-rectoria-de-sant-genis-dels-agudells/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-rectoria-de-sant-marti/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-rectoria-de-sant-marti/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-torre-del-fang/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-torre-del-fang/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-torre-del-rellotge/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-torre-del-rellotge/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-torre-llobeta/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-torre-llobeta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-villa-florida/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-villa-florida/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-villa-joana/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-villa-joana/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-torre-de-sant-joan/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-de-sant-joan/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-torre-de-santa-caterina/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-de-santa-caterina/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-torre-rodona/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-rodona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/masies/masia-torre-velez/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-velez/ | ⚠️ |

### 3.6 eixample-jardins-interiors (79 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-candida-perez/ | https://guiesbarcelona.elglobusvermell.org/elements/biblioteca-sant-antoni-joan-oliver-casal-davis-i-jardins-de-candida-perez/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardi-de-cristina-fernandez/ | https://guiesbarcelona.elglobusvermell.org/elements/jardi-de-cristina-fernandez-pereira/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardi-de-ferran-soldevila-jardins-de-la-universitat-de-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/jardi-de-ferran-soldevila-jardins-de-la-universitat-de-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-dada-byron/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-dada-byron/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardi-de-roger-de-flor/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-dagusti-centelles/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-dalicia-de-larrocha/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-dalicia-de-larrocha/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-danais-napoleon/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-danais-napoleon/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-dantoni-puigvert/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-dantoni-puigvert/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-beatriu-de-provenca/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-beatriu-de-provenca/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-beatriu-pinos-milany/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-beatriu-pinos-milany/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-ca-laranyo/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-ca-laranyo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-can-culleres/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-can-culleres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-carles-barral/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-carles-barral/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-carlit/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-carlit/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-carme-biada/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-carme-biada/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-caterina-albert/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-caterina-albert/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-cesar-martinell/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-cesar-martinell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-clotilde-cerda/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-clotilde-cerda/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-constanca-darago/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-constanca-darago/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-creu-casas/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-creu-casas/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-diagonal-ciutat-de-granada-bolivia-badajoz/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-diagonal-ciutat-de-granada-bolivia-badajoz/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-flora-tristan/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-flora-tristan/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-jaime-gil-de-biedma/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-jaime-gil-de-biedma/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-jaume-perich/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-jaume-perich/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-joan-fuster/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-joan-fuster/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-joana-tomas/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-joana-tomas/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-josep-maria-sostres/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-josep-maria-sostres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-la-casa-elizalde/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-la-casa-elizalde/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-la-favorita/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-la-favorita/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-la-galeta/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-la-galeta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-la-sedeta/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-la-sedeta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-la-torre-de-les-aigues/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-la-torre-de-les-aigues/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-lantic-cinema-novetats/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-lantic-cinema-novetats/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-lantiga-carretera-dhorta/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-lantiga-carretera-dhorta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-laura-albeniz/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-laura-albeniz/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-leonor-serrano/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-leonor-serrano/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/interior-dilla-antics-cinema-niza/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-les-treballadores-de-la-numax/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-lina-odena/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-lina-odena/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-manuel-de-pedrolo/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-manuel-de-pedrolo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-manuel-sacristan/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-manuel-sacristan/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-margarida-comas/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-margarida-comas/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-maria-assumpcio-catala/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-maria-assumpcio-catala/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-maria-manonelles/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-maria-manonelles/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-maria-matilde-almendros/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-maria-matilde-almendros/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-maria-merce-marcal/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-maria-merce-marcal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-menorca-treball-huelva-selva-de-mar/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-menorca-treball-huelva-selva-de-mar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-merce-plantada/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-merce-plantada/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-merce-vilaret/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-merce-vilaret/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-montserrat-figueras/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-montserrat-figueras/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-montserrat-roig/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-montserrat-roig/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-paula-montal/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-paula-montal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-pepa-colomer/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-pepa-colomer/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-rosa-deulofeu/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-rosa-deulofeu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-safo-2/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-safo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-sebastia-gasch/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-sebastia-gasch/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-sofia-barat/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-sofia-barat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-tanger-pamplona-sancho-de-avila-zamora/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-tanger-pamplona-sancho-de-avila-zamora/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-tecla-sala/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-tecla-sala/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-tete-montoliu/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-tete-montoliu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-del-cami-antic-de-valencia-lope-de-vega-pallars-bilbao/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-del-cami-antic-de-valencia-lope-de-vega-pallars-bilbao/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-del-palau-robert/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-del-palau-robert/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-del-rector-oliveras/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-del-rector-oliveras/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-delena-maseras/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-delena-maseras/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-dels-tres-tombs/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-dels-tres-tombs/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-demma-de-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-demma-de-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-denriqueta-seculi/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-denriqueta-seculi/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-dermessenda-de-carcassona/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-dermessenda-de-carcassona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-direne-polo/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-direne-polo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-pallars-josep-pla-pujades-agricultura/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-pallars-josep-pla-pujades-agricultura/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-pere-iv-joan-daustria-av-bogatell/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-pere-iv-joan-daustria-av-bogatell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/passatge-de-maria-vila/ | https://guiesbarcelona.elglobusvermell.org/elements/passatge-de-maria-vila/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placa-de-dolors-piera-placa-disabel-vila/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-de-dolors-piera-placa-disabel-vila/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placa-de-josep-rovira/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-de-josep-rovira/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placa-de-la-infancia/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-de-la-infancia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placa-de-ramon-calsina/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-de-ramon-calsina/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placa-de-rosa-peraulet/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-de-rosa-peraulet/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placa-de-soledad-gustavo/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-de-soledad-gustavo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placa-dhenry-dunant/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-dhenry-dunant/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placeta-de-joan-brossa/ | https://guiesbarcelona.elglobusvermell.org/elements/placeta-de-joan-brossa/ | ⚠️ |

### 3.7 avantguarda-1928-1938 (44 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/adaptacio-dun-convent-per-a-escola-del-cenu/ | https://guiesbarcelona.elglobusvermell.org/elements/adaptacio-dun-convent-per-a-escola-del-cenu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/antics-magatzems-sepu/ | https://guiesbarcelona.elglobusvermell.org/elements/antics-magatzems-sepu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/bloc-diagonal/ | https://guiesbarcelona.elglobusvermell.org/elements/bloc-diagonal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/botiga-cottet/ | https://guiesbarcelona.elglobusvermell.org/elements/botiga-cottet/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-bloc/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-bloc/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-cardenal/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-cardenal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-f-esponac/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-f-espona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-ginesta/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-ginesta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-j-espona/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-j-espona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-jaume-sans/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-jaume-sans/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-josefa-lopez/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-josefa-lopez/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-montepio-dempleats/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-montepio-dempleats/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-rodriguez-arias/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-rodriguez-arias/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-sardanes-i-bonet/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-sardanes-i-bonet/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-unifamiliar-placa-jaume-ii/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-unifamiliar-placa-jaume-ii/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-unifamiliar-placa-mons/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-unifamiliar-placa-mons/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-viladot/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-viladot/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-vilaro/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-vilaro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-xalet-passatge-roserar/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-xalet-passatge-roserar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/dispensari-central-antituberculos/ | https://guiesbarcelona.elglobusvermell.org/elements/dispensari-central-antituberculos/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/dispensari-de-sant-josep-de-la-muntanya/ | https://guiesbarcelona.elglobusvermell.org/elements/dispensari-de-sant-josep-de-la-muntanya/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-astoria/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-astoria/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-balmes/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-balmes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-balmes-2/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-balmes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-de-lart/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-de-lart/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-enric-granados/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-enric-granados/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-iradier/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-iradier/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-jonqueres/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-jonqueres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-lincoln/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-lincoln/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-navas-238/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-navas-238/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-navas-240/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-navas-240/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-padilla/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-padilla/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-padua/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-padua/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-pi-i-margall/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-pi-i-margall/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-rector-ubach/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-rector-ubach/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-rossello/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-rossello/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-viladomat/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-viladomat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-gran-via/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-gran-via/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-placa-bonanova/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-placa-bonanova/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/fabrica-myrurgia/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-myrurgia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/grup-escolar-blanquerna/ | https://guiesbarcelona.elglobusvermell.org/elements/grup-escolar-blanquerna/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/joieria-roca/ | https://guiesbarcelona.elglobusvermell.org/elements/joieria-roca/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/pavello-de-la-republica-de-1937/ | https://guiesbarcelona.elglobusvermell.org/elements/pavello-de-la-republica-biblioteca-crai-ub/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/reforma-de-laula-de-quimica-a-la-ub/ | https://guiesbarcelona.elglobusvermell.org/elements/reforma-de-laula-de-quimica-a-la-ub/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/reforma-dun-atic/ | https://guiesbarcelona.elglobusvermell.org/elements/reforma-dun-atic/ | ⚠️ |

### 3.8 moderna-1950-1975 (86 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/bloc-dels-pescadors/ | https://guiesbarcelona.elglobusvermell.org/elements/bloc-dels-pescadors/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/camp-nou/ | https://guiesbarcelona.elglobusvermell.org/elements/camp-nou/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/canodrom-meridiana/ | https://guiesbarcelona.elglobusvermell.org/elements/canodrom-meridiana/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/casa-fulla/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-fulla/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/casa-tapies/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-tapies/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/clinica-soler-i-roig/ | https://guiesbarcelona.elglobusvermell.org/elements/clinica-soler-i-roig/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/collegi-darquitectes-de-catalunya-coac/ | https://guiesbarcelona.elglobusvermell.org/elements/collegi-darquitectes-de-catalunya-coac/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/collegi-de-metges/ | https://guiesbarcelona.elglobusvermell.org/elements/collegi-de-metges/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/conjunt-del-congres-eucaristic/ | https://guiesbarcelona.elglobusvermell.org/elements/conjunt-del-congres-eucaristic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/conjunt-residencial-banco-urquijo/ | https://guiesbarcelona.elglobusvermell.org/elements/conjunt-residencial-banco-urquijo/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/conjunt-residencial-diagonal/ | https://guiesbarcelona.elglobusvermell.org/elements/conjunt-residencial-diagonal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/conjunt-residencial-gran-via/ | https://guiesbarcelona.elglobusvermell.org/elements/conjunt-residencial-gran-via/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/conjunt-residencial-les-cotxeres/ | https://guiesbarcelona.elglobusvermell.org/elements/conjunt-residencial-les-cotxeres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-2/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-avinguda-pedralbes/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-avinguda-meridiana-302/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-avinguda-meridiana-302/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-avinguda-meridiana-312/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-avinguda-meridiana-312/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-barceloneta/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-barceloneta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-bach-2/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-bach-2/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-bach-28/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-bach-28/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-bach-7/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-bach-7/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-calatrava/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-calatrava/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-compte-borrell/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-compte-borrell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-encarnacio/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-encarnacio/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-freixa/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-freixa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-juan-de-garay/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-juan-de-garay/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-mallorca/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-mallorca/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-monterols/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-monterols/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-muntaner/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-muntaner/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-nicaragua/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-nicaragua/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-pallar/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-pallars/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-roger-de-flor/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-roger-de-flor/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-rosello/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-rosello/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-sant-antoni-i-maria-claret/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-sant-antoni-i-maria-claret/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-tavern/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-tavern/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-carrer-vallmajor/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-vallmajor/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-casa-de-ferro/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-casa-de-ferro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-casa-dels-braus/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-casa-dels-braus/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-casa-tokio/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-casa-tokio/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-cyt/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-cyt/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-fregoli/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-fregoli/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-i-oficines-can-bruixa/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-i-oficines-can-bruixa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-la-casa-del-pati/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-la-casa-del-pati/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-la-colmena/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-la-colmena/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-mediterrani/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-mediterrani/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-mitre/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-mitre/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-monitor/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-monitor/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-monitor-2/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-monitor/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-passeig-maragall/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-passeig-maragall/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-seida/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-seida/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-talaia/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-talaia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-dhabitatges-via-augusta/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-via-augusta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-doficines-banca-catalana-ara-hotel/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-banca-catalana-ara-hotel/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-doficines-bbva/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-bbva/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-doficines-hispano-olivetti-ara-hotel/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-hispano-olivetti-ara-hotel/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-doficines-i-habitatges-carrer-rosello/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-i-habitatges-carrer-rosello/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-doficines-la-caixa/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-la-caixa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-doficines-monitor/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-monitor/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-doficines-ronda-universitat/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-ronda-universitat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/edifici-doficines-sandoz-novartis/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-sandoz-novartis/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/editorial-gustavo-gili/ | https://guiesbarcelona.elglobusvermell.org/elements/editorial-gustavo-gili/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/el-noticiero-universal/ | https://guiesbarcelona.elglobusvermell.org/elements/el-noticiero-universal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/escola-tecnica-superior-darquitectura-de-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/escola-tecnica-superior-darquitectura-de-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/escola-tecnica-superior-denginyeria-industrial-de-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/escola-tecnica-superior-denginyeria-industrial-de-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/escola-thau/ | https://guiesbarcelona.elglobusvermell.org/elements/escola-thau/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/fabrica-enmasa/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-enmasa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/facultat-de-ciencies-economiques/ | https://guiesbarcelona.elglobusvermell.org/elements/facultat-de-ciencies-economiques/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/facultat-de-dret/ | https://guiesbarcelona.elglobusvermell.org/elements/facultat-de-dret/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/facultat-deconomia-i-empresa/ | https://guiesbarcelona.elglobusvermell.org/elements/facultat-deconomia-i-empresa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/fundacio-joan-miro/ | https://guiesbarcelona.elglobusvermell.org/elements/fundacio-joan-miro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/habitatges-unifamiliars-agrupats-ceramica/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-unifamiliars-agrupats-ceramica/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/hotel-park/ | https://guiesbarcelona.elglobusvermell.org/elements/hotel-park/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/illa-escorial/ | https://guiesbarcelona.elglobusvermell.org/elements/illa-escorial/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/institucio-cultural-cic/ | https://guiesbarcelona.elglobusvermell.org/elements/institucio-cultural-cic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/institut-frances/ | https://guiesbarcelona.elglobusvermell.org/elements/institut-frances/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/joieria-mones/ | https://guiesbarcelona.elglobusvermell.org/elements/joieria-mones/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/laboratoris-uriach/ | https://guiesbarcelona.elglobusvermell.org/elements/laboratoris-uriach/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/les-escales-park/ | https://guiesbarcelona.elglobusvermell.org/elements/les-escales-park/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/menjadors-de-la-seat/ | https://guiesbarcelona.elglobusvermell.org/elements/menjadors-de-la-seat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/mutua-metallurgica/ | https://guiesbarcelona.elglobusvermell.org/elements/mutua-metallurgica/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/palau-municipal-desports/ | https://guiesbarcelona.elglobusvermell.org/elements/palau-municipal-desports/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/piscina-sant-jordi/ | https://guiesbarcelona.elglobusvermell.org/elements/piscina-sant-jordi/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/poligon-montbau/ | https://guiesbarcelona.elglobusvermell.org/elements/poligon-montbau/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/residencia-mare-guell/ | https://guiesbarcelona.elglobusvermell.org/elements/residencia-mare-guell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/torre-banco-atlantico-ara-banc-sabadell/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-banco-atlantico-ara-banc-sabadell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/torre-colom/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-colom/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/torre-urquinaona/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-urquinaona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/torres-doficines-trade/ | https://guiesbarcelona.elglobusvermell.org/elements/torres-doficines-trade/ | ⚠️ |

### 3.9 1975-2008 (64 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/1975-2008/48-habitatges-i-centre-civic/ | https://guiesbarcelona.elglobusvermell.org/elements/48-habitatges-i-centre-civic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/aparthotel-citadines/ | https://guiesbarcelona.elglobusvermell.org/elements/aparthotel-citadines/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/aulari-i-bar-per-a-la-facultat-de-dret/ | https://guiesbarcelona.elglobusvermell.org/elements/aulari-i-bar-per-a-la-facultat-de-dret/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/caixaforum/ | https://guiesbarcelona.elglobusvermell.org/elements/caixaforum/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/centre-darts-santa-monica/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-darts-santa-monica/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/centre-de-convencions-internacional-de-catalunya-ccib/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-de-convencions-internacional-de-catalunya-ccib/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/centre-de-cultura-contemporania-de-barcelona-cccb/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-de-cultura-contemporania-de-barcelona-cccb/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/conjunt-dhabitatges-tirant-lo-blanc/ | https://guiesbarcelona.elglobusvermell.org/elements/conjunt-dhabitatges-tirant-lo-blanc/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/cosmocaixa-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/cosmocaixa-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/cristalleries-planell/ | https://guiesbarcelona.elglobusvermell.org/elements/cristalleries-planell/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/edifici-dhabitatges-3/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/edifici-dhabitatges-i-escola-mallorca/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-i-escola-mallorca/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/edifici-dhabitatges-per-a-gent-gran/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-per-a-gent-gran/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/edifici-media-tic/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-media-tic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/edifici-mediapro/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-mediapro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/edifici-porta-vila-olimpica/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-porta-vila-olimpica/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/escola-josep-maria-jujol/ | https://guiesbarcelona.elglobusvermell.org/elements/escola-josep-maria-jujol/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/escola-municipal-de-vela/ | https://guiesbarcelona.elglobusvermell.org/elements/escola-municipal-de-vela/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/esplanada-forum-pergola-fotovoltaica/ | https://guiesbarcelona.elglobusvermell.org/elements/esplanada-forum-pergola-fotovoltaica/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/filmoteca-de-catalunya/ | https://guiesbarcelona.elglobusvermell.org/elements/filmoteca-de-catalunya/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/habitatges-de-proteccio-oficial-per-a-joves/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-de-proteccio-oficial-per-a-joves/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/habitatges-diagonal-mar-illa-de-la-llum/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-diagonal-mar-illa-de-la-llum/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/habitatges-mas-de-roda/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-mas-de-roda/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/habitatges-per-a-joves/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-per-a-joves/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/habitatges-socials-al-22/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-socials-al-22/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/habitatges-socials-per-a-joves-can-caralleu/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-socials-per-a-joves-can-caralleu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/habitatges-vertix/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-vertix/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/habitatges-vista-park/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-vista-park/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/illa-diagonal/ | https://guiesbarcelona.elglobusvermell.org/elements/illa-diagonal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/installacions-dentrenament-de-tir-amb-arc/ | https://guiesbarcelona.elglobusvermell.org/elements/installacions-dentrenament-de-tir-amb-arc/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/institut-del-teatre/ | https://guiesbarcelona.elglobusvermell.org/elements/institut-del-teatre/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/jardi-botanic-de-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/jardi-botanic-de-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/jardins-de-la-villa-cecilia/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-de-la-villa-cecilia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/jardins-del-doctor-pla-i-armengol/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-del-doctor-pla-i-armengol/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/lauditori/ | https://guiesbarcelona.elglobusvermell.org/elements/lauditori/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/lleialtat-santsenca/ | https://guiesbarcelona.elglobusvermell.org/elements/lleialtat-santsenca/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/moll-de-la-fusta/ | https://guiesbarcelona.elglobusvermell.org/elements/moll-de-la-fusta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/museu-can-framis-i-jardins-de-miquel-marti-i-pol/ | https://guiesbarcelona.elglobusvermell.org/elements/museu-can-framis-i-jardins-de-miquel-marti-i-pol/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/museu-dart-contemporani-de-barcelona-macba/ | https://guiesbarcelona.elglobusvermell.org/elements/museu-dart-contemporani-de-barcelona-macba/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/ordenacio-de-la-ronda-del-mig-rambla-brasil/ | https://guiesbarcelona.elglobusvermell.org/elements/ordenacio-de-la-ronda-del-mig-rambla-brasil/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/palau-nou-de-la-rambla/ | https://guiesbarcelona.elglobusvermell.org/elements/palau-nou-de-la-rambla/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/palau-sant-jordi/ | https://guiesbarcelona.elglobusvermell.org/elements/palau-sant-jordi/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/parc-central-de-nou-barris/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-central-de-nou-barris/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/parc-de-la-creueta-del-coll/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-de-la-creueta-del-coll/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/parc-de-lestacio-del-nord/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-de-lestacio-del-nord/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/parc-de-recerca-biomedica-de-barcelona-prbb/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-de-recerca-biomedica-de-barcelona-prbb/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/parc-del-clot/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-del-clot/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/parc-del-nus-de-la-trinitat/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-del-nus-de-la-trinitat/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/parc-diagonal-mar/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-diagonal-mar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/piscina-de-salts-de-montjuic/ | https://guiesbarcelona.elglobusvermell.org/elements/piscina-de-salts-de-montjuic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/placa-dels-paisos-catalans/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-dels-paisos-catalans/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/plug-in-building/ | https://guiesbarcelona.elglobusvermell.org/elements/plug-in-building/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/rambla-de-sants-jardins-elevats-de-sants/ | https://guiesbarcelona.elglobusvermell.org/elements/rambla-de-sants-jardins-elevats-de-sants/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/reforma-i-ampliacio-del-museu-picasso/ | https://guiesbarcelona.elglobusvermell.org/elements/reforma-i-ampliacio-del-museu-picasso/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/reforma-i-millora-de-les-places-de-gracia/ | https://guiesbarcelona.elglobusvermell.org/elements/reforma-i-millora-de-les-places-de-gracia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/residencia-geriatrica-dhorta/ | https://guiesbarcelona.elglobusvermell.org/elements/residencia-geriatrica-dhorta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/seu-central-de-la-diputacio-de-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/seu-central-de-la-diputacio-de-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/seu-de-gas-natural/ | https://guiesbarcelona.elglobusvermell.org/elements/seu-de-gas-natural/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/seu-de-la-cmt/ | https://guiesbarcelona.elglobusvermell.org/elements/seu-de-la-cmt/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/torre-de-telecomunicacions-de-collserola/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-de-telecomunicacions-de-collserola/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/torre-glories-torre-agbar/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-glories-torre-agbar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/tres-illes-dhabitatges-a-leixample-de-cerda/ | https://guiesbarcelona.elglobusvermell.org/elements/tres-illes-dhabitatges-a-leixample-de-cerda/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/velodrom-municipal-dhorta/ | https://guiesbarcelona.elglobusvermell.org/elements/velodrom-municipal-dhorta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/1975-2008/via-julia/ | https://guiesbarcelona.elglobusvermell.org/elements/via-julia/ | ⚠️ |

### 3.10 2010-2025 (51 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/2010-2025/ateneu-de-fabricacio-de-gracia/ | https://guiesbarcelona.elglobusvermell.org/elements/ateneu-de-fabricacio-de-gracia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/bloc4bcn-espai-cooperatiu/ | https://guiesbarcelona.elglobusvermell.org/elements/bloc4bcn-espai-cooperatiu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/carrer-cristobal-de-moura/ | https://guiesbarcelona.elglobusvermell.org/elements/carrer-cristobal-de-moura/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/casal-de-barri-can-carol/ | https://guiesbarcelona.elglobusvermell.org/elements/casal-de-barri-can-carol/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/casal-de-barri-de-trinitat-nova/ | https://guiesbarcelona.elglobusvermell.org/elements/casal-de-barri-de-trinitat-nova/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/centre-civic-baro-de-viver/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-civic-baro-de-viver/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/centre-de-primera-acollida-per-a-persones-sense-llar/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-de-primera-acollida-per-a-persones-sense-llar/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/centre-de-vida-comunitaria-de-trinitat-vella/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-de-vida-comunitaria-de-trinitat-vella/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/centre-kalida/ | https://guiesbarcelona.elglobusvermell.org/elements/centre-kalida/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/cirerers-cohabitatges-cooperatius/ | https://guiesbarcelona.elglobusvermell.org/elements/cirerers-cohabitatges-cooperatius/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/conjunt-dhabitatges-illa-glories/ | https://guiesbarcelona.elglobusvermell.org/elements/conjunt-dhabitatges-illa-glories/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-110-rooms/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-110-rooms/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-ali-bei/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-ali-bei/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-aprop-ciutat-vella/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-aprop-ciutat-vella/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-dotacionals-greenhuse/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-dotacionals-greenhuse/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-hpo-living-lattice/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-hpo-living-lattice/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-per-a-4-amics/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-per-a-4-amics/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-set-vides/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-set-vides/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-socials/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-socials/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-dhabitatges-socials-2/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-socials/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-doficines-entegra/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-entegra/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-doficines/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-doficines-2/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/edifici-residencial/ | https://guiesbarcelona.elglobusvermell.org/elements/edifici-residencial/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/eixos-verds-de-leixample-superilla/ | https://guiesbarcelona.elglobusvermell.org/elements/eixos-verds-de-leixample-superilla/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/entorns-del-mercat-del-born/ | https://guiesbarcelona.elglobusvermell.org/elements/entorns-del-mercat-del-born/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/entorns-del-rec-comtal/ | https://guiesbarcelona.elglobusvermell.org/elements/entorns-del-rec-comtal/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/escola-dels-encants/ | https://guiesbarcelona.elglobusvermell.org/elements/escola-dels-encants/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/escola-la-mar-bella/ | https://guiesbarcelona.elglobusvermell.org/elements/escola-la-mar-bella/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/estacions-de-metro-l9-mercabarna-parc-logistic-i-europa-fira/ | https://guiesbarcelona.elglobusvermell.org/elements/estacions-de-metro-l9-mercabarna-parc-logistic-i-europa-fira/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/estudis-industrials/ | https://guiesbarcelona.elglobusvermell.org/elements/estudis-industrials/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/fabrica-de-creacio-fabra-i-coats/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-de-creacio-fabra-i-coats/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/habitatges-socials-fabra-i-coats/ | https://guiesbarcelona.elglobusvermell.org/elements/habitatges-socials-fabra-i-coats/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/jardins-antonia-vilas/ | https://guiesbarcelona.elglobusvermell.org/elements/jardins-antonia-vilas/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/la-balma-cohabitatges-cooperatius/ | https://guiesbarcelona.elglobusvermell.org/elements/la-balma-cohabitatges-cooperatius/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/la-borda-cohabitatges-cooperatius/ | https://guiesbarcelona.elglobusvermell.org/elements/la-borda-cohabitatges-cooperatius/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/la-comunal-espai-cooperatiu/ | https://guiesbarcelona.elglobusvermell.org/elements/la-comunal-espai-cooperatiu/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/la-seca-fundacio-joan-brossa/ | https://guiesbarcelona.elglobusvermell.org/elements/la-seca-fundacio-joan-brossa/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/lci-barcelona-22-campus/ | https://guiesbarcelona.elglobusvermell.org/elements/lci-barcelona-22-campus/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/nest-city-lab/ | https://guiesbarcelona.elglobusvermell.org/elements/nest-city-lab/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/oliva-artes-muhba/ | https://guiesbarcelona.elglobusvermell.org/elements/oliva-artes-muhba/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/parc-de-les-glories/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-de-les-glories/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/passeig-de-sant-joan/ | https://guiesbarcelona.elglobusvermell.org/elements/passeig-de-sant-joan/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/placa-soller-i-ateneu-la-bobila/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-soller-i-ateneu-la-bobila/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/poliesportiu-municipal-camp-del-ferro/ | https://guiesbarcelona.elglobusvermell.org/elements/poliesportiu-municipal-camp-del-ferro/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/poliesportiu-turo-de-la-peira/ | https://guiesbarcelona.elglobusvermell.org/elements/poliesportiu-turo-de-la-peira/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/rehabilitacio-de-les-bateries-antiaeries/ | https://guiesbarcelona.elglobusvermell.org/elements/rehabilitacio-de-les-bateries-antiaeries/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/skate-park-mar-bella/ | https://guiesbarcelona.elglobusvermell.org/elements/skate-park-mar-bella/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/switch-nova-seu-de-simon/ | https://guiesbarcelona.elglobusvermell.org/elements/switch-nova-seu-de-simon/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/torre-de-bombers/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-de-bombers/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/torre-julia/ | https://guiesbarcelona.elglobusvermell.org/elements/torre-julia/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/vall-dhebron-institut-de-recerca/ | https://guiesbarcelona.elglobusvermell.org/elements/vall-dhebron-institut-de-recerca/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/2010-2025/villa-urania/ | https://guiesbarcelona.elglobusvermell.org/elements/villa-urania/ | ⚠️ |

### 3.11 marina-prat-vermell (18 fitxes)

| URL WordPress | URL Hugo | Estat |
|---|---|---|
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/casa-del-rellotge/ | https://guiesbarcelona.elglobusvermell.org/elements/casa-del-rellotge/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/cases-barates-eduard-aunos/ | https://guiesbarcelona.elglobusvermell.org/elements/cases-barates-eduard-aunos/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/castell-del-port/ | https://guiesbarcelona.elglobusvermell.org/elements/castell-del-port/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/cementiri-de-montjuic/ | https://guiesbarcelona.elglobusvermell.org/elements/cementiri-de-montjuic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/colonia-bausili/ | https://guiesbarcelona.elglobusvermell.org/elements/colonia-bausili/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/colonia-santiveri/ | https://guiesbarcelona.elglobusvermell.org/elements/colonia-santiveri/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/fabrica-philips-actualment-coneguda-com-illa-philips/ | https://guiesbarcelona.elglobusvermell.org/elements/fabrica-philips-actualment-coneguda-com-illa-philips/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/far-de-montjuic/ | https://guiesbarcelona.elglobusvermell.org/elements/far-de-montjuic/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/fira-barcelona/ | https://guiesbarcelona.elglobusvermell.org/elements/fira-barcelona/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/fossar-de-la-pedrera/ | https://guiesbarcelona.elglobusvermell.org/elements/fossar-de-la-pedrera/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/graner/ | https://guiesbarcelona.elglobusvermell.org/elements/graner/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/jardi-dels-drets-humans/ | https://guiesbarcelona.elglobusvermell.org/elements/jardi-dels-drets-humans/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/la-bascula/ | https://guiesbarcelona.elglobusvermell.org/elements/la-bascula/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/la-chalmeta/ | https://guiesbarcelona.elglobusvermell.org/elements/la-chalmeta/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/masia-can-mestres/ | https://guiesbarcelona.elglobusvermell.org/elements/masia-can-mestres/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/mercadillo-de-la-marina-zona-franca/ | https://guiesbarcelona.elglobusvermell.org/elements/mercadillo-de-la-marina-zona-franca/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/parc-can-sabate/ | https://guiesbarcelona.elglobusvermell.org/elements/parc-can-sabate/ | ⚠️ |
| https://guiesbarcelona.elglobusvermell.org/marina-prat-vermell/placa-del-moviment-obrer-skatepark/ | https://guiesbarcelona.elglobusvermell.org/elements/placa-del-moviment-obrer-skatepark/ | ⚠️ |


---

## 4. URLs eliminades (no migrades)

| URL WordPress | Motiu |
|---|---|
| https://guiesbarcelona.elglobusvermell.org/wp-statistics-honey-pot-page-2021-09-02-105732/ | Artefacte del plugin WP-Statistics; mai ha estat contingut real |
| https://guiesbarcelona.elglobusvermell.org/sitemap.html | Pàgina de sitemap HTML generada per WP; substituïda pel sitemap Hugo |

---

## 5. Contingut nou a Hugo (sense origen WP)

### 5.1 Arquitectes (197 pàgines)

Col·lecció nova, no existent a WordPress. Cada arquitecte/a és una pàgina de taxonomia generada per Hugo.

| URL Hugo |
|---|
| https://guiesbarcelona.elglobusvermell.org/arquitectes/a&eb/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/adolf-florensa/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/agence-ter/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/aia/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/albert-de-pineda-álvarez/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/albert-viaplana/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/alfonso-de-luna/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/alfonso-milà/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/amadeu-llopart/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ana-coello/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-bonet-castellana/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-de-ferrater/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-de-moragas-i-gallissà/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-falguera/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-fisas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-perpiñà/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-pineda-i-gualba/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-puig-gairalt/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-solanas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/antoni-vila-i-bruguera/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/apocapoc-bcn/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/arata-isozaki/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/arquitectura-g/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ateliers-jean-nouvel/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/b720-arquitectes/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/baas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/barceló-balanzó/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/batlle-i-roig/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/bayona-valero/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/bcq-arquitectes/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/beatriz-borque/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/benedetta-tagliabue/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/bernardo-de-solá/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/beth-galí/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/beverly-pepper/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/boma/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/bonaventura-bassegoda/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/cantallops-vicente/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/carles-buïgas-i-sans/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/carles-enrich/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/carles-martínez/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/carlos-marquès-i-maristany/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/carme-ribas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/celobert/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/cierto-estudio/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/circular-studio/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/claudi-duran-i-ventosa/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/cloud-9/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/coll-leclerc/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/conxita-balcells/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/daniel-gelabert/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/dataae/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/david-mackay/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/elías-torres-tur/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/embt/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/emili-donato-folch/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/enric-miralles/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/enric-sagnier-villavecchia/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/enric-tous/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/enrico-peressutti/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ensenyat-tarrida/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ernesto-n.-rogers/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/espai-lur/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/esteve-bonell-costa/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/eusebi-bona-i-puig/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/federico-correa/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/francesc-bassó-i-birulés/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/francesc-de-paula-quintana-vidal/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/francesc-de-paula-villar-carmona/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/francesc-mitjans-i-miró/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/francesc-perales/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/francesc-rius/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/g.-guiteras/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/garcés-de-seta-bonet/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/germà-rodríguez-arias/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/guillem-cosp-i-vilaró/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/guillem-giráldez-i-dávila/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/gustau-gili/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/harquitectes/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/haz-arquitectura/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/heliodoro-piñón-pallarés/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/imma-jansana/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ítalo-lauro/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/jaime-pastor/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/jaume-mestres/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/javier-carvajal-ferrer/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joan-arias/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joan-baca/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joan-baptista-pons-trabal/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joan-baptista-subirana/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joan-bosch-agustí/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joan-carles-cardenal/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joan-vera/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joaquim-gili-i-morós/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/joaquim-vilaseca/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/jorge-vidal/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josé-antonio-coderch-de-sentmenat/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josé-antonio-martínez-lapeña/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josé-luis-sanz-magallón/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-alemany-i-juvé/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-anglada/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-domènech-i-estapà/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-gonzàlez/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-graner-i-prat/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-lluís-mateo/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-lluís-sert/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-m.-pericas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-maria-casadevall/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-maria-fargas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-maria-julià/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-maria-martorell-i-codina/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-maria-segarra-i-solsona/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-maria-sostres-i-maluquer/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-marimon-i-cot/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-masdeu/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-miàs-i-gifré/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-plantada-i-artigas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-pujol-i-brull/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-ribas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-roselló-i-til/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-soteras-i-mauri/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/josep-torres-clavé/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/juli-m.-fossas-i-martínez/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/la-boqueria/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/lacol/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/länk-arquitectes/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/leandre-albareda-i-petit/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/lluís-cantallops/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/lluís-clotet/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/lluís-comerón/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/lluís-pérez-de-la-vega/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/lola-domènech/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/lorenzo-garcía-barbón/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/luis-castellón/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/lussi-studio/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/maio/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/manuel-baldrich/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/manuel-brullet/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/manuel-de-solà-morales-i-de-rosselló/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/manuel-de-solà-morales-i-rubió/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/manuel-puig-janer/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/manuel-ribas-i-piera/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/manuel-ruisánchez/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/manuel-valls-i-vergés/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/map-arquitectes/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/màrius-quintana/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/marta-cervelló/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/martí-franch/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/mbm-arquitectes/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/meritxell-inaraja/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/miguel-jiménez/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/miquel-mariné/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/miquel-ponsetí-i-vives/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/nilo-tusquets/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/núria-salvadó/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/oab-(carlos-ferrater)/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/oliveras-boix/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/op-team-arquitectura/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/oriol-bohigas-i-guardiola/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/òscar-tusquets/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/partner-ag/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/pau-monguió/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/pau-vidal/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/pelayo-martínez-paricio/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/pere-joan-ravetllat/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/pere-llimona/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/pere-lópez-i-íñigo/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/peris+toral/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/rafael-garcía-de-castro/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/rafael-moneo/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/rafael-serra-florensa/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/raimon-duran-i-reynals/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ramon-martí/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ramon-puig/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ramon-sanabria/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/rcr-arquitectes/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ricard-ribas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/ricardo-bofill-levi/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/robert-terradas-i-via/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/roger-méndez/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/roldán+berengué/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/sandra-martín-lara/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/santiago-balcells-gorina/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/scob/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/sergi-godia/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/sixte-illescas/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/slowup/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/straddle3/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/sumo/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/sv60-cordón-&-liñán-arquitectos/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/toyo-ito/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/toyo-ito-associates/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/víctor-rahola/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/vivas-arquitectos/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/xavier-busquets-i-sindreu/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/xavier-ruiz-i-vallès/ |
| https://guiesbarcelona.elglobusvermell.org/arquitectes/xavier-subias-i-fages/ |

### 5.2 Elements nous (sense origen WP)

11 elements que no existien al WordPress — no tenen `aliases:` al frontmatter.

| URL Hugo | Notes |
|---|---|
| https://guiesbarcelona.elglobusvermell.org/elements/casa-lluis-jara-urbano/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/casa-roca-barallat/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/casa-unifamiliar/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-carrer-navas/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/edifici-dhabitatges-placa-sant-miquel/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/edifici-doficines-llull-122/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/flors-de-la-rambla/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/jardins-ada-byron/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/masia-can-mestres-vallvidrera/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/pavello-de-la-republica-de-1937-replica/ | Fitxa nova, no existia a WP |
| https://guiesbarcelona.elglobusvermell.org/elements/placa-dolors-piera-isabel-vila/ | Fitxa nova, no existia a WP |

### 5.3 Publicacions noves

2 publicacions que no existien al WordPress (no hi ha categoria `text/` equivalent).

| URL Hugo |
|---|
| https://guiesbarcelona.elglobusvermell.org/publicacions/new-babylon/ |
| https://guiesbarcelona.elglobusvermell.org/publicacions/tapies/ |

### 5.4 Pàgines noves

Pàgines estàtiques creades a Hugo sense equivalent WP.

| URL Hugo |
|---|
| https://guiesbarcelona.elglobusvermell.org/accessibilitat/ |
| https://guiesbarcelona.elglobusvermell.org/contacte/ |
| https://guiesbarcelona.elglobusvermell.org/estadistiques/ |
| https://guiesbarcelona.elglobusvermell.org/legal/avis-legal/ |
| https://guiesbarcelona.elglobusvermell.org/legal/cookies/ |
| https://guiesbarcelona.elglobusvermell.org/legal/privacitat/ |
| https://guiesbarcelona.elglobusvermell.org/llicencia/ |
| https://guiesbarcelona.elglobusvermell.org/mapa/ |
| https://guiesbarcelona.elglobusvermell.org/presentacio/ |

---

## 6. Notes per al deploy

- Els `aliases:` de Hugo generen redirects HTML automàtics (meta-refresh) — funcionen sense configuració de servidor addicional.
- Per redirects 301 reals (millor per SEO): generar fitxer de regles Nginx/Apache a partir d'aquest document.
- El canonical de cada pàgina Hugo apunta a la URL Hugo nova (no a la WP antiga).
- Verificació post-deploy: `curl -I https://guiesbarcelona.elglobusvermell.org/{URL-WP-antiga}` ha de retornar 200 (meta-refresh) o 301 (si es configura redirect real al servidor).
- Les URLs WP amb suffix `-2`, `-3`, `-4` (duplicats de categoria) apunten al mateix element Hugo; els `aliases:` inclouen tots els sufixos.
- Pàgines WP sense alias Hugo: `/politica-de-privadesa/` i `/arquitectura-i-urbanisme/` no tenen `aliases:` al Hugo — cal afegir-los manualment o gestionar-los al servidor.
- `defaultContentLanguageInSubdir = false` a `hugo.toml` confirma que les URLs Hugo no tenen prefix `/ca/`.
 