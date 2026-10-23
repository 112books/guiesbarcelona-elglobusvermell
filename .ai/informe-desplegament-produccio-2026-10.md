# Informe de desplegament a producció — octubre 2026

**Objectiu:** documentar com es faria el desplegament al servidor de producció actual, quines credencials tenim i quines falten, i si el servidor és tècnicament viable. No s'implementa res en aquest informe.

---

## 1. Situació actual

| Element | Estat |
|---|---|
| Hugo (web nou) | GitHub Pages (`112books.github.io`) · entorn `staging` (noindex) |
| Domini de producció | `guiesbarcelona.elglobusvermell.org` → `195.201.2.76` (Hetzner) → WordPress antic |
| Formulari de contacte | `contacte/envia.php` (acció relativa al layout) · el PHP **no és al repo Hugo** |
| Clau SSH LinuxBCN | Generada (`~/.ssh/linuxbcn`) i pujada a GitHub ✅ |
| Credencials servidor | **Pendents de Jorge** (host, usuari, ruta, clau SSH) 🔴 |

El WordPress actual continua viu al Hetzner. El Hugo no substituirà res fins que el DNS apunti a una nova destinació.

---

## 2. Dos escenaris possibles

### Escenari A — Hugo a GitHub Pages + formulari al servidor actual

El web queda hostatjat a GitHub Pages (gratuït, CDN global, deploy automàtic) i el servidor actual només serveix el PHP del formulari.

**Com funciona el formulari en aquest escenari:**
- El formulari envia el POST a una URL absoluta del servidor (p.e., `https://guiesbarcelona.elglobusvermell.org/contacte/envia.php`).
- El servidor respon i redirigeix de nou al web Hugo a GitHub Pages.
- Cal modificar l'`action` del formulari al layout (`contacte/list.html` línia 19) per fer-la absoluta o parametritzada per entorn.

**Canvis al codi necessaris (petits):**
1. `config/production/params.toml`: afegir `envia_php_url = "https://guiesbarcelona.elglobusvermell.org/contacte/envia.php"`
2. `layouts/contacte/list.html` línia 19: `action="{{ .Site.Params.envia_php_url }}"`
3. Crear/instal·lar `envia.php` al servidor (vegeu § 4).
4. Canvi DNS: `guiesbarcelona CNAME → 112books.github.io` (ja documentat a `.ai/TALL-DOMINI.md`).
5. `deploy-prod.yml` línia 56: `staging` → `production`.

**Pro:** GitHub Pages gestiona el servidor, el CDN i el TLS. Zero cost d'allotjament.
**Contra:** el formulari depèn del servidor de Jorge; cal coordinar CORS si el servidor ho exigeix.

---

### Escenari B — Hugo servit directament des del servidor actual

El servidor de Jorge (Hetzner o Dinahosting) substitueix GitHub Pages com a origen del web.

**Mecanisme de deploy:**
- `hugo --minify --environment production` → genera `public/`
- `rsync -avz --delete public/ usuari@host:/ruta/document-root/` (per SSH)
- Ja previst al `CLAUDE.md`: «Deploy prod: rsync SSH → servidor LinuxBCN (manual post-validació)»

**Canvis al workflow (`deploy-prod.yml`) necessaris:**
- Substituir el bloc `actions/deploy-pages` per un pas `rsync` que llegeixi les credencials SSH des de GitHub Secrets.
- Afegir els secrets al repo GitHub: `SSH_HOST`, `SSH_USER`, `SSH_PATH`, `SSH_KEY` (la clau LinuxBCN privada).
- Línia 56: `staging` → `production`.

**DNS:** no cal canviar-lo. El domini ja apunta al servidor (195.201.2.76); n'hi ha prou amb desplegar els fitxers estàtics al document root del subdomini.

**Pro:** tot en un sol lloc; `envia.php` al mateix document root, l'`action` relativa del formulari funciona sense cap canvi al codi.
**Contra:** perdem la CDN de GitHub Pages; el deploy passa a dependre de la disponibilitat del servidor.

---

## 3. Credencials: tenim / no tenim

| Credencial | Estat | Notes |
|---|---|---|
| Clau SSH privada LinuxBCN | ✅ Generada (`~/.ssh/linuxbcn`) | Cal afegir-la com a GitHub Secret si es fa CI/CD |
| Clau SSH pública | ✅ Pujada a GitHub (com a deploy key del repo) | Cal que Jorge l'instal·li al servidor |
| Host del servidor | 🔴 Pendent de Jorge | Probablement `195.201.2.76` però cal confirmar |
| Usuari SSH | 🔴 Pendent de Jorge | |
| Ruta del document root del subdomini | 🔴 Pendent de Jorge | On ha d'anar el `public/` del Hugo |
| Credencials panell DNS | ⚠️ El gestiona Jorge | Cal coordinar el canvi CNAME si es va a l'Escenari A |
| GitHub OAuth App (per al CMS) | 🔴 Pendent (Dinahosting) | No bloqueja el deploy del web; bloqueja el login al CMS sense PAT |

**Resum:** el bloqueig principal és d'un sol actor — Jorge — que ha de proporcionar host, usuari i ruta, i instal·lar la clau SSH pública al servidor. La resta ho podem preparar nosaltres.

---

## 4. El formulari de contacte (`envia.php`)

El fitxer `envia.php` **no és al repo Hugo**. Existeix al WordPress del Hetzner (herència) però no s'ha auditat. Cal crear-ne un de nou o adaptar l'existent.

### Requisits mínims d'un `envia.php` per a aquest projecte

- Llegeix els camps POST: `nom`, `email`, `missatge`, `rgpd`, `web` (honeypot).
- Si `web` té contingut → descarta (bot).
- Valida que `nom`, `email` i `missatge` no siguin buits i que `rgpd` sigui `on`.
- Envia un correu a `info@elglobusvermell.org` via `mail()` o SMTP.
- Redirigeix a una pàgina de confirmació o torna JSON per a AJAX (el formulari actual fa POST síncron).

### Viabilitat tècnica del servidor

Per executar `envia.php` el servidor necessita **PHP ≥ 7.4** i accés a `mail()` o a un servidor SMTP. Un VPS Hetzner típic (Linux, Apache/Nginx + PHP-FPM) ho cobreix de sèrie.

Si el servidor és **Dinahosting** (hosting compartit), PHP i `mail()` també hi són; no cal configuració addicional.

### Qüestió de CORS (Escenari A)

Si el Hugo viu a GitHub Pages i el PHP viu al servidor de Jorge, el navegador no bloquejarà el POST (és un formulari HTML clàssic, no una petició `fetch()`). No hi ha problema de CORS.

---

## 5. Viabilitat tècnica del servidor

Per servir el web Hugo (fitxers estàtics: HTML, CSS, JS, imatges) el servidor necessita:

| Requisit | Detall | Estat |
|---|---|---|
| Servidor web (Apache o Nginx) | Servir fitxers estàtics | Quasi segur present (ja serveix el WP) |
| PHP | Només per a `envia.php` | Present si hi ha WP |
| TLS/HTTPS | `Let's Encrypt` o certificat existent | Present (WP ja és HTTPS) |
| SSH i rsync | Per al deploy | Cal que Jorge instal·li la clau pública |
| Espai en disc | `public/` ocupa ~200 MB (HTML + imatges compreses) | Negligible en qualsevol VPS |

El servidor actual **és tècnicament viable** per als dos escenaris. No cal cap canvi de tecnologia.

### Capacitats bloquejades per Dinahosting (independents del deploy)

- **OAuth proxy per al CMS** (login sense PAT): requereix poder guardar secrets fora del webroot i executar PHP amb variables d'entorn. Possible a Dinahosting i a Hetzner, però cal accés SSH o panell de configuració avançat.
- **Headers HTTP de seguretat** (CSP, HSTS, X-Frame-Options): configurables via `.htaccess` (Apache) o `nginx.conf`. Possible un cop tinguem accés SSH.
- `analytics.json` públic: restringir el fitxer via `.htaccess` un cop migrat.

---

## 6. Tasques pendents abans del desplegament

### Bloquejants (espera Jorge)
1. Obtenir host, usuari, ruta i clau pública instal·lada al servidor.
2. Decidir si el domini es canvia via CNAME (Escenari A) o es manté apuntant al servidor (Escenari B).

### A preparar nosaltres (no bloquejants)
3. Crear `envia.php` (∼50 línies PHP) i provar-lo en local o en staging.
4. Si Escenari A: parametritzar l'`action` del formulari per entorn.
5. Si Escenari B: reescriure el bloc `deploy` de `deploy-prod.yml` amb `rsync` + GitHub Secrets.
6. En qualsevol cas: canviar la línia 56 de `deploy-prod.yml` de `staging` a `production`.

### Post-desplegament (del kit TALL-DOMINI.md)
7. Google Search Console + Bing Webmaster / IndexNow.
8. Auditar o substituir el `envia.php` del WordPress antic.
9. Headers HTTP de seguretat (`.htaccess` o `nginx.conf`).
10. OAuth proxy per al CMS (Fase 1 del CMS-PLAN).

---

## 7. Recomanació

**Escenari B** és més net: tot en un lloc, el formulari funciona sense cap canvi al codi Hugo, i el DNS ja apunta al servidor. L'únic prerequisit és tenir les credencials de Jorge.

Si les credencials triguen, **l'Escenari A** (formulari al servidor + web a GitHub Pages) és implementable ara amb canvis mínims al codi i sense esperar Jorge per al deploy del web.

En tots dos casos, el `envia.php` s'ha de crear de zero (l'existent del WP no s'ha auditat i és herència de WordPress).
