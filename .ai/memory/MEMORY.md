# Memory index — elglobusvermell.org

- [CMS Sveltia](project_cms_sveltia.md) — Sveltia CMS per guiesbarcelona: arquitectura, decisions, limitacions, com activar editors
- [LinuxBCN Analytics for GoatCounter](project_linuxbcn_analytics.md) — Família de 3 projectes germans (WP plugin, dashboard standalone, Hugo module). Logo existent. Pla Hugo: .ai/GOATCOUNTER-HUGO-PLAN.md
- [Doble llicència — consulta client](project_doble_llicencia.md) — Web original té © i CC BY-SA 4.0 simultàniament; cal aclarir amb El Globus Vermell
- [Tasques pendents](project_tasques_pendents.md) — Títol home (pendent client), llicència, imatges, GoatCounter, OAuth, geocodificació, accessibilitat
- [Diari del projecte](diary/) — Sessions de treball amb durades estimades. Invocar amb /documenta al final de cada sessió.
- [Servidor de producció](project_servidor_produccio.md) — Root SSH confirmat per Jorge (Virtubio.net). BD a wp-config.php a /var/www. DNS a joker.com (accés El Globus Vermell).
- [Credencials servidor — pendent Jorge](project_servidor_pendents_jorge.md) — Mail enviat 26/10. Pendent: port SSH, pla Hetzner, YunoHost admin, comptes correu, accés backups.
- [Stadia Maps](reference_stadiamaps.md) — Compte webmaster@linuxbcn.com, domain auth, dashboard property 104841, estils en ús
- [Sense emojis](feedback_no_emojis.md) — L'usuari no vol emojis en cap context, mai.
- [To missatges Xavi](feedback_to_xavi.md) — Tracte proper, salutació sempre, acabar amb "Seguim!"
- [Commits i deploys](feedback_commits.md) — Commits individuals per tasca, deploys agrupats per tasques similars

## INICI DE SESSIÓ — llegeix sempre primer

Al principi de cada sessió, llegeix en aquest ordre:
1. `.ai/PLAN.md` — pla actiu amb estat actual i pròxims passos
2. `.ai/TASKS.md` — llista completa de tasques amb estat ✅/⏳/🔴
3. `memory/project_tasques_pendents.md` — resum de deute tècnic i pendents client

No exploris el codi fins haver llegit aquests tres fitxers.

## Sessió 2026-09-13 — tancat

- Sveltia CMS localització catalana: PR #973 mergetat, shiped a v0.211.3. Tancat.
- Informe seguretat: tots els fixes accionables ja estaven aplicats. Tancat.
- Informe accessibilitat: tots els fixes crítics ja estaven aplicats. Fix addicional: `aria-required` + `aria-describedby` estàtic al formulari de contacte (commits `c236d11` + `9acf9d4`). Tancat.

## Pròxima sessió

Tasques accionables (sense blocants externs):
1. **SEO** — aplicar pendents de `.ai/informe-seo-geo-aeo-2026-09-01.md`
2. **GoatCounter** — integrar al Hugo (layout stats, script fetch, workflow horari)
3. **Guia editor** — afegir captures reals dels passos
