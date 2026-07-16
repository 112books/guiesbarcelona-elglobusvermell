# Graph Report - .  (2026-07-16)

## Corpus Check
- Corpus is ~14,198 words - fits in a single context window. You may not need a graph.

## Summary
- 331 nodes · 481 edges · 34 communities (28 shown, 6 thin omitted)
- Extraction: 83% EXTRACTED · 16% INFERRED · 1% AMBIGUOUS · INFERRED: 77 edges (avg confidence: 0.71)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Leaflet Functions (Static)
- Leaflet Functions (Theme)
- GATCPAC & Rationalist Architecture
- Industrial Adaptive Reuse & 22@
- Barcelona Residential Buildings
- Web Structure & i18n
- Contemporary Architects
- Iconic Rationalist Works
- Hugo Project & Tech Stack
- Leaflet Functions (Static)
- Leaflet Functions (Theme)
- Leaflet Core (Static)
- Leaflet Core (Theme)
- Leaflet Geometry (Static)
- Leaflet Geometry (Theme)
- Leaflet Events (Static)
- Leaflet Events (Theme)
- SQL Import Script
- Map JavaScript
- Change Publishing Script
- Leaflet Util (Static)
- Leaflet Util (Theme)
- Biblioteca El Clot
- Leaflet Marker (Static)
- Leaflet Marker (Theme)
- TMB Bus Depots
- Map Marker Icon
- Map Marker Icon 2x
- Hugo Archetypes
- Elements Index
- Map Marker Shadow
- Theme Marker Shadow

## God Nodes (most connected - your core abstractions)
1. `Publicació GATCPAC` - 20 edges
2. `Publicació GATCPAC (guide)` - 15 edges
3. `Barcelona 22@ District` - 12 edges
4. `e()` - 10 edges
5. `e()` - 10 edges
6. `Conjunt d'habitatges Illa Glòries` - 10 edges
7. `F()` - 8 edges
8. `m()` - 8 edges
9. `F()` - 8 edges
10. `m()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Header Partial` --references--> `Guies Barcelona Logo`  [INFERRED]
  themes/guiesbcn-elglobusvermell/layouts/partials/header.html → static/img/logo-guiesbarcelona.jpg
- `Leaflet Marker Icon 2x` --semantically_similar_to--> `Theme Leaflet Marker Icon 2x`  [INFERRED] [semantically similar]
  static/vendor/leaflet/images/marker-icon-2x.png → themes/guiesbcn-elglobusvermell/static/vendor/leaflet/images/marker-icon-2x.png
- `Leaflet Marker Icon` --semantically_similar_to--> `Theme Leaflet Marker Icon`  [INFERRED] [semantically similar]
  static/vendor/leaflet/images/marker-icon.png → themes/guiesbcn-elglobusvermell/static/vendor/leaflet/images/marker-icon.png
- `Project Overview (README)` --references--> `Guies d'Arquitectura i Urbanisme de Barcelona`  [EXTRACTED]
  README.md → content/ca/_index.md
- `Project Overview (README)` --references--> `LinuxBCN (Web Developer)`  [EXTRACTED]
  README.md → content/ca/credits/_index.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **GATCPAC Publication Building Elements** — content_ca_elements_adaptacio_dun_convent_per_a_escola_del_cenu, content_ca_elements_antics_magatzems_sepu, content_ca_elements_bloc_diagonal, content_ca_elements_botiga_cottet, content_ca_elements_casa_bloc, content_ca_elements_casa_f_espona, content_ca_elements_casa_ginesta, content_ca_elements_casa_jaume_sans, content_ca_elements_casa_josefa_lopez, content_ca_elements_casa_montepio_dempleats, content_ca_elements_casa_rodriguez_arias, content_ca_elements_casa_sardanes_i_bonet, content_ca_elements_casa_unifamiliar, content_ca_elements_casa_viladot [EXTRACTED 1.00]
- **Poblenou Publication Building Elements** — content_ca_elements_ca_laranyo, content_ca_elements_can_tiana_il3_ub [EXTRACTED 1.00]
- **Deployment Pipeline Technology Stack** — _github_workflows_deploy_prod_yml_deploy_pipeline, concept_hugo, concept_staticrypt, concept_github_pages [EXTRACTED 1.00]
- **GATCPAC-related buildings** — content_ca_elements_casa_vilaro, content_ca_elements_casa_xalet_passatge_roserar, content_ca_elements_dispensari_central_antituberculos, content_ca_elements_dispensari_de_sant_josep_de_la_muntanya, content_ca_elements_edifici_astoria, content_ca_elements_edifici_dhabitatges_carrer_balmes, content_ca_elements_edifici_dhabitatges_carrer_de_lart, content_ca_elements_edifici_dhabitatges_carrer_enric_granados, content_ca_elements_edifici_dhabitatges_carrer_iradier, content_ca_elements_edifici_dhabitatges_carrer_jonqueres, content_ca_elements_edifici_dhabitatges_carrer_lincoln, content_ca_elements_edifici_dhabitatges_carrer_navas, content_ca_elements_edifici_dhabitatges_carrer_padilla, content_ca_elements_edifici_dhabitatges_carrer_padua, content_ca_elements_edifici_dhabitatges_carrer_pi_i_margall, content_ca_elements_edifici_dhabitatges_carrer_rector_ubach, content_ca_elements_edifici_dhabitatges_carrer_rossello, content_ca_elements_edifici_dhabitatges_carrer_viladomat, content_ca_elements_edifici_dhabitatges_gran_via, content_ca_elements_edifici_dhabitatges_placa_bonanova [EXTRACTED 1.00]
- **Architects of Illa Glòries** — content_ca_elements_conjunt_dhabitatges_illa_glories, architect_bayona_valero, architect_cantallops_vicente, architect_cierto_estudio, architect_ensenyat_tarrida, architect_fran_llonch, architect_haz_arquitectura, architect_pau_vidal, architect_sv60_cordon_linan, architect_vivas_arquitectos [EXTRACTED 1.00]
- **Poblenou-area buildings** — content_ca_elements_cotxeres_de_tmb, content_ca_elements_edifici_doficines_entegra, content_ca_elements_edifici_media_tic, content_ca_elements_edifici_mediapro [INFERRED 0.75]
- **Poblenou/22@ Industrial Heritage Buildings** — content_ca_elements_fabrica_de_llorenc_pons_i_clerch_md, content_ca_elements_farinera_sant_jaume_la_farinera_del_clot_md, content_ca_elements_hispano_olivetti_md, content_ca_elements_industrias_metalicas_sa_md, content_ca_elements_museu_can_framis_i_jardins_de_miquel_marti_i_pol_md, content_ca_elements_netol_md, content_ca_elements_la_ciutat_groga_md [INFERRED 0.85]
- **GATCPAC Publication Referenced Buildings** — content_ca_elements_fabrica_myrurgia_md, content_ca_elements_fundacio_joan_miro_md, content_ca_elements_grup_escolar_blanquerna_md, content_ca_elements_joieria_roca_md, content_ca_elements_les_escales_park_md, content_ca_elements_pavello_de_la_republica_de_1937_replica_md, content_ca_elements_reforma_de_laula_de_quimica_a_la_ub_md, content_ca_elements_reforma_dun_atic_md [EXTRACTED 1.00]
- **Interiors de l'Illa Publication Referenced Elements** — content_ca_elements_jardins_ada_byron_md, content_ca_elements_jardins_ca_laranyo_md, content_ca_elements_jardins_de_diagonal_ciutat_de_granada_bolivia_badajoz_md, content_ca_elements_jardins_diagonal_ciutat_de_granada_md, content_ca_elements_placa_de_dolors_piera_placa_disabel_vila_md, content_ca_elements_placa_dolors_piera_isabel_vila_md [EXTRACTED 1.00]
- **Page Chrome Composition (baseof + partials)** — themes_guiesbcn_elglobusvermell_layouts__default_baseof, themes_guiesbcn_elglobusvermell_layouts_partials_head, themes_guiesbcn_elglobusvermell_layouts_partials_header, themes_guiesbcn_elglobusvermell_layouts_partials_footer [EXTRACTED 1.00]
- **Legal Compliance Pages (all stub/placeholder)** — content_ca_legal_avis_legal, content_ca_legal_cookies, content_ca_legal_privacitat [EXTRACTED 1.00]
- **Internationalization Translation System** — i18n_ca, i18n_en, i18n_es [INFERRED 0.85]

## Communities (34 total, 6 thin omitted)

### Community 0 - "Leaflet Functions (Static)"
Cohesion: 0.07
Nodes (7): a(), Ci(), ei(), ii(), l(), ri(), x()

### Community 1 - "Leaflet Functions (Theme)"
Cohesion: 0.07
Nodes (7): a(), Ci(), ei(), ii(), l(), ri(), x()

### Community 2 - "GATCPAC & Rationalist Architecture"
Cohesion: 0.10
Nodes (24): Elements Archetype Schema, Arquitectura racionalista, GATCPAC (Grup d'Arquitectes i Tècnics Catalans per al Progrés de l'Arquitectura Contemporània), Habitatge obrer (Workers' Housing), Josep Lluís Sert, Josep Marimon i Cot, Publicació GATCPAC (guide), Publicació Poblenou (guide) (+16 more)

### Community 3 - "Industrial Adaptive Reuse & 22@"
Cohesion: 0.12
Nodes (22): Adaptive Reuse of Industrial Heritage, Barcelona 22@ District, Pharmacy-Art Material Connection, Civic Memory in Urban Space, Landscape as Cultural Transition, Fàbrica de Llorenç Pons i Clerch, Farinera Sant Jaume / La Farinera del Clot, Hispano Olivetti (+14 more)

### Community 4 - "Barcelona Residential Buildings"
Cohesion: 0.10
Nodes (21): Casa Vilaró, Casa xalet passatge Roserar, Dispensari Central Antituberculós, Dispensari de Sant Josep de la Muntanya, Edifici Astoria, Edifici d'habitatges, carrer Balmes, Edifici d'habitatges, carrer de l'Art, Edifici d'habitatges, carrer Enric Granados (+13 more)

### Community 5 - "Web Structure & i18n"
Cohesion: 0.14
Nodes (20): Seu de la CMT, Torre Glòries / Torre Agbar, En paper (Publications Collection), Avís legal (Legal Notice), Cookies Policy, Privacitat (Privacy Policy), Publicacions (Publications Data Registry), Catalan Translations (+12 more)

### Community 6 - "Contemporary Architects"
Cohesion: 0.13
Nodes (17): Batlle i Roig, Bayona-Valero, Cantallops-Vicente, Cierto Estudio, Cloud 9, Ensenyat-Tarrida, Franc Llonch, Haz Arquitectura (+9 more)

### Community 7 - "Iconic Rationalist Works"
Cohesion: 0.19
Nodes (14): Form Follows Function, GATCPAC Rationalism, Mediterranean Modernism, Museographic Circulation Design, Rationalist Architecture, 1937 Paris International Exhibition Republican Pavilion, Fàbrica Myrurgia, Fundació Joan Miró (+6 more)

### Community 8 - "Hugo Project & Tech Stack"
Cohesion: 0.17
Nodes (13): Deploy to Production Pipeline, Ajuntament de Barcelona, El Globus Vermell (Publisher), GitHub Pages, Guies d'Arquitectura i Urbanisme de Barcelona, Hugo (Static Site Generator), LinuxBCN (Web Developer), OpenRouteService (+5 more)

### Community 9 - "Leaflet Functions (Static)"
Cohesion: 0.24
Nodes (11): at(), be(), d(), hi(), m(), Qe(), ve(), W() (+3 more)

### Community 10 - "Leaflet Functions (Theme)"
Cohesion: 0.24
Nodes (11): at(), be(), d(), hi(), m(), Qe(), ve(), W() (+3 more)

### Community 11 - "Leaflet Core (Static)"
Cohesion: 0.24
Nodes (10): bi(), c(), e(), F(), p(), Pi(), q(), Ti() (+2 more)

### Community 12 - "Leaflet Core (Theme)"
Cohesion: 0.24
Nodes (10): bi(), c(), e(), F(), p(), Pi(), q(), Ti() (+2 more)

### Community 13 - "Leaflet Geometry (Static)"
Cohesion: 0.28
Nodes (9): G(), i(), k(), me(), Mi(), Oe(), Se(), ze() (+1 more)

### Community 14 - "Leaflet Geometry (Theme)"
Cohesion: 0.28
Nodes (9): G(), i(), k(), me(), Mi(), Oe(), Se(), ze() (+1 more)

### Community 15 - "Leaflet Events (Static)"
Cohesion: 0.25
Nodes (8): h(), j(), Jt(), ke(), ne(), Qt(), s(), $t()

### Community 16 - "Leaflet Events (Theme)"
Cohesion: 0.25
Nodes (8): h(), j(), Jt(), ke(), ne(), Qt(), s(), $t()

### Community 17 - "SQL Import Script"
Cohesion: 0.52
Nodes (6): main(), parse_copy_block(), Extreu les files d'un bloc COPY com a llista de dicts., slugify(), toml_list(), toml_str()

### Community 18 - "Map JavaScript"
Cohesion: 0.43
Nodes (5): actualitzaBotons(), colorPub(), primerColor(), togglePub(), toggleTots()

### Community 19 - "Change Publishing Script"
Cohesion: 0.60
Nodes (5): publica-canvis script, dim(), err(), ok(), print()

### Community 20 - "Leaflet Util (Static)"
Cohesion: 0.33
Nodes (6): Ae(), Ie(), Le(), O(), Re(), te()

### Community 21 - "Leaflet Util (Theme)"
Cohesion: 0.33
Nodes (6): Ae(), Ie(), Le(), O(), Re(), te()

### Community 22 - "Biblioteca El Clot"
Cohesion: 0.50
Nodes (4): Josep Benet, MBM Arquitectes, Publicació Biblioteques (guide), Biblioteca El Clot - Josep Benet

### Community 23 - "Leaflet Marker (Static)"
Cohesion: 0.67
Nodes (4): Je(), ni(), oi(), si()

### Community 24 - "Leaflet Marker (Theme)"
Cohesion: 0.67
Nodes (4): Je(), ni(), oi(), si()

### Community 25 - "TMB Bus Depots"
Cohesion: 0.67
Nodes (3): Josep Alemany, Cotxeres de TMB, Publicació Poblenou

## Ambiguous Edges - Review These
- `Jardins d'Ada Byron (2026-07-09)` → `Jardins d'Ada Byron (original)`  [AMBIGUOUS]
  content/ca/elements/jardins-ada-byron.md · relation: semantically_similar_to
- `Jardins de Ca l'Aranyó (2026-07-09)` → `Jardins de Ca l'Aranyó (full description)`  [AMBIGUOUS]
  content/ca/elements/jardins-ca-laranyo.md · relation: semantically_similar_to
- `Jardins de Diagonal - Ciutat de Granada - Bolívia - Badajoz (full path)` → `Jardins de Diagonal - Ciutat de Granada - Bolívia - Badajoz (2026-07-09)`  [AMBIGUOUS]
  content/ca/elements/jardins-de-diagonal-ciutat-de-granada-bolivia-badajoz.md · relation: semantically_similar_to
- `Plaça de Dolors Piera + Plaça d'Isabel Vilà (full description)` → `Plaça de Dolors Piera + Plaça d'Isabel Vilà (nomenclator)`  [AMBIGUOUS]
  content/ca/elements/placa-de-dolors-piera-placa-disabel-vila.md · relation: semantically_similar_to

## Knowledge Gaps
- **84 isolated node(s):** `Default Hugo Archetype`, `Elements Archetype Schema`, `Elements Index Page`, `Adaptació d'un convent per a escola del CENU`, `Antics magatzems SEPU` (+79 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Jardins d'Ada Byron (2026-07-09)` and `Jardins d'Ada Byron (original)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Jardins de Ca l'Aranyó (2026-07-09)` and `Jardins de Ca l'Aranyó (full description)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Jardins de Diagonal - Ciutat de Granada - Bolívia - Badajoz (full path)` and `Jardins de Diagonal - Ciutat de Granada - Bolívia - Badajoz (2026-07-09)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **What is the exact relationship between `Plaça de Dolors Piera + Plaça d'Isabel Vilà (full description)` and `Plaça de Dolors Piera + Plaça d'Isabel Vilà (nomenclator)`?**
  _Edge tagged AMBIGUOUS (relation: semantically_similar_to) - confidence is low._
- **Are the 12 inferred relationships involving `Barcelona 22@ District` (e.g. with `Fàbrica de Llorenç Pons i Clerch` and `Hispano Olivetti`) actually correct?**
  _`Barcelona 22@ District` has 12 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `e()` (e.g. with `u()` and `F()`) actually correct?**
  _`e()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 4 inferred relationships involving `e()` (e.g. with `u()` and `F()`) actually correct?**
  _`e()` has 4 INFERRED edges - model-reasoned connections that need verification._