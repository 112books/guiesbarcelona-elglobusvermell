---
name: Auditoria seguretat i accessibilitat (juliol 2026)
description: Resultats de l'auditoria SEC/A11Y/XB del projecte guiesbarcelona. Pendents d'aplicar.
type: project
originSessionId: 6a3c2b1c-61f1-4d4d-831d-a20461e3c8de
---
Auditoria completada el 2026-07-17. Correccions crítica i fàcils aplicades al commit. Resten les complexes.

**Why:** Revisió nocturna demanada per l'usuari abans de continuar amb el backend.
**How to apply:** Quan es reprengui el projecte, aplicar per ordre de severitat.

## Pendents (no aplicats)

### HIGH
- **A11Y-1**: `#mapa-contenidor` necessita `role="region" aria-label="Mapa interactiu dels elements"`. A `mapa.js` post-init: `map.getContainer().setAttribute('aria-label', 'Mapa')`.
- **A11Y-2**: `#mapa-filtres` i `#cerca-filtres` necessiten `aria-live="polite"` al template HTML.
- **A11Y-3**: Els `<label>` de grups de filtres (Publicacions, Temes, Cerca, Dècada, Arquitecte) no estan associats als controls. Fix: `role="group" aria-labelledby="..."` o `<fieldset>/<legend>`. Per inputs: `label.setAttribute('for', inputId)` + `input.id = inputId`.
- **SEC-2**: No hi ha CSP headers al lloc principal. Afegir `static/_headers` (GitHub Pages no ho suporta — caldrà via servidor Dinahosting o meta-tag limitat).

### MEDIUM
- **A11Y-5**: Text blanc sobre `--pub-color` sense garantia de contrast. Documentar colors permesos a `data/publicacions.yaml` o afegir lògica JS per triar blanc/negre.
- **A11Y-10**: `<div id="fitxa-mapa">` necessita `role="region" aria-label="Mapa de localització"`.
- **A11Y-11**: Input de cerca necessita `id` i `label[for]` associat.
- **SEC-4**: `oauth/index.php` — `$allowedOrigin` hauria de validar-se contra una whitelist hardcoded dins el PHP.
- **XB-1**: `Object.values()` sense fallback (IE11). Acceptable si no cal IE11.

### LOW
- **A11Y-4**: Botons toggle llistat alfabètic: afegir `aria-controls="grup-elements-X"`.
- **A11Y-8**: `<section class="llistat-alfabetic">` sense heading visible — afegir `<h2>` sr-only.
- **A11Y-9**: `<span class="llistat-lletra-count">` — afegir `aria-hidden="true"`.
- **SEC-5**: `oauth/index.php` — `die()` sense `Content-Type: text/plain` consistent.
- **SEC-6**: Falta `X-Content-Type-Options: nosniff` i `X-Frame-Options: SAMEORIGIN` — via Dinahosting.
- **XB-2/3/10**: `closest()`, `URLSearchParams`, `NodeList.forEach` sense fallback IE11 — acceptable.
- **XB-5**: `aspect-ratio` CSS — fallback per Safari <15 opcional.

## Ja aplicats (commit post-auditoria)
- SEC-1: GoatCounter URL canviat a `https://`
- SEC-3: `lat`/`long` ara passen per `jsonify | safeJS`
- A11Y-6: Logos amb `alt=""` (nom al `aria-label` del parent `<a>`)
- A11Y-7: Classe `sr-only` afegida al CSS; nav labels usen `sr-only` en lloc de `display:none`
