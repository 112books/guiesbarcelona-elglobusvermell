---
name: LinuxBCN Analytics for GoatCounter - família de projectes
description: Tres projectes germans d'analítica web amb GoatCounter, marca LinuxBCN Analytics
type: project
originSessionId: 6a3c2b1c-61f1-4d4d-831d-a20461e3c8de
---
Família de projectes d'analítica web sota la marca **LinuxBCN Analytics for GoatCounter**:

1. **goatcounter-wp** (existent, publicat) — Plugin WordPress
   Path: `/Users/joan/Documents/Obsidian/goatcounter-wp/`
   Logo: `Logotip-wordpress-modul/icon-128x128.png` i `icon-256x256.png`

2. **goatcounter-dashboard** (existent) — Dashboard estàtic standalone
   Path: `/Users/joan/Documents/Obsidian/goatcounter-dashboard/`
   Motor Python + JSON + HTML amb login per contrasenya (SHA-256)
   Ja funciona per llumatics.com i pocallum.cat

3. **hugo-goatcounter-dashboard** (planificat) — Hugo Module
   Repo futur: `github.com/112books/hugo-goatcounter-dashboard`
   Germà del plugin WP, mateixa marca i estètica
   Config: un sol fitxer `.md` per projecte (frontmatter: gc_site, gc_url, pw_hash, sections)
   Pla detallat: `.ai/GOATCOUNTER-HUGO-PLAN.md`

**Why:** Tenir un sol mòdul reutilitzable per a tots els projectes Hugo de LinuxBCN.
Primer ús: guiesbarcelona.elglobusvermell.org

**Estètica:** IBM Plex Mono, fons #f5f4f0 (paper càlid), accent #d4600a (taronja LinuxBCN).
El dashboard NO s'adapta al tema del projecte hoste — manté identitat pròpia.

**How to apply:** Quan s'implementi el mòdul Hugo, recordar:
- Reutilitzar logo existent de goatcounter-wp
- Portar CSS/JS de goatcounter-dashboard/admin/index.html tal qual
- Afegir tracking d'events del mapa (marcadors, filtres, temes A/B/C)
- Token GoatCounter sempre com a GitHub Secret, mai al repo
