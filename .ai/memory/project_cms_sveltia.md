---
name: CMS Sveltia - guiesbarcelona
description: Estat i decisions del CMS editorial per El Globus Vermell
type: project
originSessionId: 6a3c2b1c-61f1-4d4d-831d-a20461e3c8de
---
Sveltia CMS afegit al repo guiesbarcelona-elglobusvermell (commit 694f1fb, 2026-07-16).

**Why:** El Globus Vermell necessita editar fitxes d'edificis sense tocar GitHub directament. No hi ha pressupost per backend.

**Arquitectura implementada:**
- `/admin/` — accés master Joan (tot: edificis + configuració + pàgines)
- `/admin-editor/` — accés editors Globus Vermell (només fitxes d'edificis)
- Autenticació Fase 0: PAT de GitHub (zero infraestructura, funciona avui)
- Fase 1 (pendent Dinahosting): PHP OAuth proxy (fitxer `oauth/index.php`)

**Decisions clau:**
- NO Cloudflare Workers (experiència negativa prèvia del client)
- NO Netlify
- Proxy futur: PHP a Dinahosting (LinuxBCN)

**Prerequisit resolt:** 70 fitxers d'elements migrats de TOML (+++) a YAML (---).
Bug Sveltia CMS: no pot crear fitxers TOML nous correctament.
Script: `scripts/toml-to-yaml.py`

**Limitacions actuals de Sveltia CMS (v0.171, beta):**
- Sense editorial workflow (previst v1.0 tardor 2026) — workaround: branca `drafts`
- Sense rols per col·lecció (previst v2.0 2027) — workaround: dos paths `/admin/` i `/admin-editor/`
- Sense PKCE (pendent GitHub)

**How to apply:** Quan el Globus Vermell demani accés per editar, recordar que cal:
1. Convidar el seu compte GitHub al repo (rol Write)
2. Fer-los crear un PAT fine-grained (Contents R/W + Metadata R)
3. Enviar-los la URL: `.../admin-editor/`
