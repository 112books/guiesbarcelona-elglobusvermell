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
2. Fer-los crear un **PAT clàssic** de GitHub amb permís `public_repo` (el fine-grained NO funciona per a convidats d'aquest repo; vegeu el mail rectificatiu de l'1 set)
3. Enviar-los la URL: `.../admin/cms/`

---

## Actualització 2026-09-30

- Editor master: `/admin/cms/` · Editor administrador: `/admin/cms-admin/`. L'antic `/admin-editor/` ja no s'usa.
- Autenticació Fase 0: PAT clàssic (vegeu més amunt).
- Versió de Sveltia servida: **0.224.0** (CDN sense fixar).
- **Diagnosi del 30 set**: el CMS funciona; el que passa és que el **primer carregament és lent** (660 fitxes d'elements + 197 d'arquitectes + assets). Els carregaments següents van amb la memòria cau (IndexedDB). Detall a `.ai/canvis/CMS-diagnosi-2026-09-30.md`.
