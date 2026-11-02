---
name: CMS Sveltia - guiesbarcelona
description: Estat i decisions del CMS editorial per El Globus Vermell
type: project
originSessionId: 6a3c2b1c-61f1-4d4d-831d-a20461e3c8de
---
Sveltia CMS afegit al repo guiesbarcelona-elglobusvermell (commit 694f1fb, 2026-07-16).

**Why:** El Globus Vermell necessita editar fitxes d'edificis sense tocar GitHub directament. No hi ha pressupost per backend.

**Arquitectura actual (des del 2026-09-30):**
- **Un sol editor:** `/admin/cms/` — crea i edita tot el contingut (fitxes d'element, pàgines, plànols-guia, arquitectes).
- `/admin/cms-admin/` **redirigeix** a `/admin/cms/`. Abans era un segon editor amb `create: true`; l'única diferència era crear fitxes noves i calia mantenir dues configs sincronitzades a mà.
- Autenticació Fase 0: PAT clàssic de GitHub (zero infraestructura, funciona avui).
- Fase 1 (pendent Dinahosting): PHP OAuth proxy (`oauth/index.php`).

**Decisions clau:**
- NO Cloudflare Workers (experiència negativa prèvia del client)
- NO Netlify
- Proxy futur: PHP a Dinahosting (LinuxBCN)
- **Un editor únic amb creació** (2026-09-30): els editors necessiten crear fitxes noves. La "protecció" dels dos paths era només que l'enllaç no es divulgava, no un control real.

**Prerequisit resolt:** 70 fitxers d'elements migrats de TOML (+++) a YAML (---).
Bug Sveltia CMS: no pot crear fitxers TOML nous correctament.
Script: `scripts/toml-to-yaml.py`

**Limitacions actuals de Sveltia CMS (beta):**
- Sense editorial workflow (previst v1.0 tardor 2026) — workaround: branca `drafts`
- Sense rols per col·lecció (previst v2.0 2027) — un sol editor
- Sense PKCE (pendent GitHub)

**How to apply:** Quan el Globus Vermell demani accés per editar, cal:
1. Convidar el seu compte GitHub al repo (rol Write)
2. Fer-los crear un **PAT clàssic** de GitHub amb permís `public_repo` (el fine-grained NO funciona per a convidats d'aquest repo)
3. Enviar-los la URL: `.../admin/cms/`

---

## Actualització 2026-09-30

- **Unificació:** `/admin/cms/` és l'únic editor (amb creació de fitxes noves). `/admin/cms-admin/` redirigeix allà.
- Guia de l'editor (`static/admin/guia/`) actualitzada: ja no diu «No creïs edificis nous»; explica com crear-ne i l'avís de duplicats. `/admin/guia-admin/` redirigeix a la guia.
- Autenticació Fase 0: PAT clàssic (vegeu més amunt).
- Versió de Sveltia servida: **0.224.0** (CDN fixada).
- **Diagnosi del 30 set**: el CMS funciona; el primer carregament és lent (660 fitxes + 197 arquitectes + assets). Detall a `.ai/canvis/CMS-diagnosi-2026-09-30.md`.
