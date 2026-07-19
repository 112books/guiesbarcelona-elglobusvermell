# Revisió qualitat d'elements — guiesbarcelona.elglobusvermell.org

**Data de creació:** 2026-07-19
**Propòsit:** Document de suport intern per a la revisió de qualitat de les fitxes d'elements importades.

---

## Resum

| Categoria | Nombre | Acció recomanada |
|-----------|--------|------------------|
| Elements totals | 656 | — |
| Tots amb coordenades | 656 | ✅ Cap absent del mapa |
| Coordenades aproximades | 3 | Verificar ubicació exacta |
| Importats manualment (format YAML) | 66 | Revisar coherència de dades |
| Sense camp d'adreça | 22 | Afegir adreça si es coneix |

---

## 1. Coordenades aproximades (3 elements)

Geocodificats el 2026-07-19 però amb ubicació aproximada perquè l'adreça original no era prou precisa per a Nominatim.

| Slug | Problema | Acció |
|------|----------|-------|
| `masia-can-papanaps` | Coordenades aproximades (zona Horta-Guinardó). Adreça real: cantonada Mura / Dosrius, Gràcia | Localitzar coordenades exactes al Google Maps |
| `masia-can-muntaner` | Coordenades al Park Güell (genèriques). L'edifici és l'Escola Baldiri Reixach dins el parc | Localitzar coordenades exactes al Google Maps |
| `masia-mas-enric` | Coordenades a la Plaça de la Ciutadella (genèriques). Cal localitzar la Torre dels Moros exacta | Localitzar coordenades exactes al Google Maps |

---

## 2. Elements importats manualment — format YAML (66 elements)

Aquests elements es van crear manualment (no via l'script d'importació automàtica del WP). Poden tenir diferències de format o dades menys completes que els importats automàticament. Cal revisar que el contingut sigui complet i coherent.

| Slug | Té adreça |
|------|-----------|
| `adaptacio-dun-convent-per-a-escola-del-cenu` | ✅ |
| `antics-magatzems-sepu` | ✅ |
| `biblioteca-el-clot-josep-benet` | ✅ |
| `bloc-diagonal` | ✅ |
| `botiga-cottet` | ✅ |
| `ca-laranyo` | ✅ |
| `can-tiana-il3-ub` | ✅ |
| `casa-bloc` | ✅ |
| `casa-f-espona` | ✅ |
| `casa-ginesta` | ✅ |
| `casa-j-espona` | ✅ |
| `casa-jaume-sans` | ✅ |
| `casa-josefa-lopez` | ✅ |
| `casa-montepio-dempleats` | ✅ |
| `casa-rodriguez-arias` | ✅ |
| `casa-sardanes-i-bonet` | ✅ |
| `casa-unifamiliar` | ✅ |
| `casa-viladot` | ✅ |
| `casa-vilaro` | ✅ |
| `casa-xalet-passatge-roserar` | ✅ |
| `conjunt-dhabitatges-illa-glories` | ✅ |
| `cotxeres-de-tmb` | ✅ |
| `dispensari-central-antituberculos` | ✅ |
| `dispensari-de-sant-josep-de-la-muntanya` | ✅ |
| `edifici-astoria` | ✅ |
| `edifici-dhabitatges-carrer-balmes` | ✅ |
| `edifici-dhabitatges-carrer-de-lart` | ✅ |
| `edifici-dhabitatges-carrer-enric-granados` | ✅ |
| `edifici-dhabitatges-carrer-iradier` | ✅ |
| `edifici-dhabitatges-carrer-jonqueres` | ✅ |
| `edifici-dhabitatges-carrer-lincoln` | ✅ |
| `edifici-dhabitatges-carrer-navas` | ✅ |
| `edifici-dhabitatges-carrer-padilla` | ✅ |
| `edifici-dhabitatges-carrer-padua` | ✅ |
| `edifici-dhabitatges-carrer-pi-i-margall` | ✅ |
| `edifici-dhabitatges-carrer-rector-ubach` | ✅ |
| `edifici-dhabitatges-carrer-rossello` | ✅ |
| `edifici-dhabitatges-carrer-viladomat` | ✅ |
| `edifici-dhabitatges-gran-via` | ✅ |
| `edifici-dhabitatges-placa-bonanova` | ✅ |
| `edifici-doficines-entegra` | ✅ |
| `edifici-media-tic` | ✅ |
| `edifici-mediapro` | ✅ |
| `fabrica-de-llorenc-pons-i-clerch` | ✅ |
| `fabrica-myrurgia` | ✅ |
| `farinera-sant-jaume-la-farinera-del-clot` | ✅ |
| `fundacio-joan-miro` | ✅ |
| `grup-escolar-blanquerna` | ✅ |
| `hispano-olivetti` | ✅ |
| `industrias-metalicas-sa` | ✅ |
| `jardins-ada-byron` | ✅ |
| `jardins-de-ca-laranyo` | ✅ |
| `jardins-de-diagonal-ciutat-de-granada-bolivia-badajoz` | ✅ |
| `joieria-roca` | ✅ |
| `la-ciutat-groga` | ✅ |
| `les-escales-park` | ✅ |
| `mercat-dels-encants-fira-de-bellcaire` | ✅ |
| `museu-can-framis-i-jardins-de-miquel-marti-i-pol` | ✅ |
| `netol` | ✅ |
| `parc-de-les-glories` | ✅ |
| `pavello-de-la-republica-de-1937-replica` | ✅ |
| `placa-dolors-piera-isabel-vila` | ✅ |
| `reforma-de-laula-de-quimica-a-la-ub` | ✅ |
| `reforma-dun-atic` | ✅ |
| `seu-de-la-cmt` | ✅ |
| `torre-glories-torre-agbar` | ✅ |

---

## 3. Elements TOML sense camp d'adreça

Aquests elements no tenen el camp `adreca` a la fitxa. Les coordenades hi poden ser, però no es mostra adreça al popup del mapa ni a la fitxa.

| Slug |
|------|
| `biblioteca-de-lateneu-barcelones` |
| `biblioteca-la-fraternitat` |
| `biblioteca-la-marina-del-prat-vermell` |
| `biblioteca-prosperitat-ideal-plastica-flor` |
| `biblioteca-publica-de-lestat-a-barcelona-biblioteca-central-de-barcelona` |
| `biblioteca-sant-gervasi-sud` |
| `biblioteca-sarria-j-v-foix` |
| `castell-del-port` |
| `escola-josep-maria-jujol` |
| `esplanada-forum-pergola-fotovoltaica` |
| `fossar-de-la-pedrera` |
| `habitatges-vista-park` |
| `moll-de-la-fusta` |
| `parc-del-clot` |
| `passeig-maritim-de-la-barceloneta` |
| `pavello-de-la-republica-biblioteca-crai-ub` |
| `pla-de-palau-i-passeig-joan-de-borbo` |
| `reforma-i-ampliacio-del-museu-picasso` |
| `reforma-i-millora-de-les-places-de-gracia` |
| `seu-central-de-la-diputacio-de-barcelona` |
| `velodrom-municipal-dhorta` |
| `via-julia` |

---

## Notes

### Coordenades: dos formats coexistents

- **590 fitxers TOML** (`+++`): coordenades com a número o string (`lat = 41.xxx` o `lat = "41.xxx"`)
- **66 fitxers YAML** (`---`): coordenades com a número (`lat: 41.xxx`)

Hugo llegeix ambdós formats correctament. No cal unificar-los.

### Filtres del mapa: totes les publicacions actives

Fins el 2026-07-19, 6 publicacions tenien `a_app: false` i els seus elements **no apareixien als botons de filtre** (però sí al mapa i al llistat). S'ha corregit: ara totes 13 publicacions apareixen als filtres.