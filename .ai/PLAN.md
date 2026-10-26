# PLAN.md — Pla de treball actiu

Última actualització: 26 octubre 2026

---

## Estat actual (26 oct 2026)

El web és funcional i en producció a https://guiesbarcelona.elglobusvermell.org/. El CMS (Sveltia) està actiu i en Xavi hi treballa diàriament. Les tasques actuals giren al voltant de la qualitat del contingut (arquitectes, fotos, intervencions) i petites millores del CMS.

### ✅ Completat avui (26 oct 2026)

- **Arquitectes al CMS**: script de migració `corregeix-arquitectes-orfes.py` ha corregit 106 fitxes d'edificis que tenien noms d'arquitecte obsolets (Xavi havia canviat el títol de les fitxes d'arquitecte). 83 noms resolts automàticament. 80 pendents de revisió per Xavi.
- **Links Viquipèdia**: 3 links canviats d'es.wikipedia a ca.wikipedia (Federico Correa, Beth Galí, Sixte Illescas). Link de Luis Castellón eliminat (apuntava a una persona diferent).
- **Mapa fullscreen**: desactivació de gestureHandling en entrar a pantalla completa (roda del ratolí lliure). En mòbil: pseudo-fullscreen CSS per evitar overlay del navegador.
- **fotos_addicionals**: migrades 4 fitxes de format string antic a format objecte `{url, autoria, peu}`. Causa de l'error de guardar al CMS.
- **autors a intervencions**: camp canviat de `string` a `relation` (selector d'arquitectes). Template `single.html` actualitzat amb backward compat (string antic i llista nova).
- **Xavi crea arquitectes**: ha creat ~30 fitxes noves d'arquitecte dels 80 pendents (confirmat via pull).

### ✅ Completat anteriorment (oct 2026)

- CMS Sveltia actiu amb tots els editors
- Camp `arquitectes` a fitxes d'edificis: migrat de text lliure a widget de relació
- Etiqueta `tipus: individual` eliminada de totes les fitxes
- 3 fitxes de biblioteca noves amb fotos de Xavi
- Script de verificació diària de números arreglat
- Tauler de revisió `/admin/revisio/` actiu

---

## Blocants actius

### ✅ Jorge — accés al servidor resolt (26 oct 2026)
Jorge (hola@linuxbcn.com / Virtubio.net) ha confirmat:
- **Accés root SSH** al servidor de producció
- **Credencials BD**: als fitxers `wp-config.php` dins `/var/www` (dues instal·lacions WP)
- **DNS**: domini a joker.com, accés de El Globus Vermell per canviar registres DNS quan calgui

Pendent: OK definitiu de Joan per fer el tall del domini (WordPress → Hugo).
⚠️ El WordPress NO es toca fins a l'OK explícit de Joan.

### 🟡 80 arquitectes sense fitxa — revisió pendent de Xavi
Llistat enviat per mail (26 oct). Xavi n'ha creat ~30 avui. Els 50 restants
poden generar pàgines "fantasma" fins que es creïn o es corregeixi el nom.

### 🟡 OAuth pel CMS
Fase 1 (PAT GitHub) activa. Fase 2 (OAuth propi a linuxbcn.com) pendent de Jorge.

---

## Pròxims passos

### Immediat (sense blocants)
1. Esperar que Xavi acabi de crear/revisar els 80 arquitectes pendents.
2. SEO — pendents de `.ai/informe-seo-geo-aeo-2026-09-01.md`.
3. GoatCounter — integrar mòdul Hugo per a estadístiques.

### Quan arribin credencials de Jorge
- Configurar deploy directe SSH (rsync) al servidor de producció.
- Configurar OAuth per al CMS (eliminar dependència de PAT GitHub per als editors).

---

## Decisions obertes

| Decisió | Estat |
|---------|-------|
| OAuth pel CMS | Pendent credencials Jorge |
| GoatCounter integració | Pendent (no blocant) |
| SEO pendents | Pendent (no blocant) |
