# Pla d'implementació: Sveltia CMS per a guiesbarcelona.elglobusvermell.org

Creat: 2026-07-16 | Estat: planificació

---

## Resum executiu

El Globus Vermell necessita una interfície web per editar les fitxes d'edificis sense tocar codi ni GitHub directament. La solució és **Sveltia CMS**, un CMS Git-based que s'afegeix al repositori existent (sense servidor separat) i permet editar el contingut via formularis web.

**Decisió d'autenticació:** PAT (Personal Access Token) de GitHub com a solució inicial — zero infraestructura addicional, funciona sobre GitHub Pages des del primer dia. OAuth proxy PHP sobre Dinahosting s'afegirà a la Fase 2 per millorar la UX d'accés.

---

## Limitacions conegudes de Sveltia CMS (juliol 2026)

Documentades a la recerca abans d'implementar per evitar sorpreses:

| Limitació | Impacte | Workaround |
|-----------|---------|------------|
| **Bug TOML**: fitxers nous creats sense delimitadors `+++` | CRÍTIC — cal resoldre abans | Migrar tot el contingut a frontmatter YAML (`---`) |
| **Sense editorial workflow** (implementació prevista v1.0, tardor 2026) | Moderat — no hi ha flux draft→revisió automàtic | Branca `drafts` + PR manual per Joan |
| **Sense rols per col·lecció** (previst v2.0, 2027) | Baix ara — pocs editors | Dos `config.yml` a paths separats (`/admin/` i `/admin-editor/`) |
| **Sense PKCE** (pendent GitHub) | Baix — cobert per PAT o proxy PHP | PAT auth o proxy PHP |
| **Edicions simultànies sense detecció de conflictes** | Baix ara | Coordinar editors (pocs usuaris) |

---

## Arquitectura per fases

```
FASE 0 (ara)          FASE 1 (Dinahosting llest)    FASE 2 (Sveltia v1.0)
─────────────────     ──────────────────────────     ─────────────────────
GitHub Pages          GitHub Pages + Dinahosting     + Editorial workflow
     │                        │                              │
/admin/               /admin/ (mateix)               Draft → PR → Publish
     │                        │
PAT auth              OAuth PHP proxy
(cada editor          (login amb compte
crea el seu PAT)       GitHub, 1 clic)
```

---

## PREREQUISIT CRÍTIC: Migrar frontmatter TOML → YAML

**Problema:** Tots els fitxers de contingut actuals usen `+++` (TOML). Sveltia CMS té un bug confirmat: els fitxers *nous* que crea no afegeixen els delimitadors `+++`, cosa que trenca el build de Hugo.

**Solució:** Convertir tots els fitxers `.md` de `content/ca/elements/` de TOML a YAML (`---`) abans d'activar el CMS. Això és una migració única, reversible, i no canvia el contingut — només el format dels delimitadors.

Exemple:
```
TOML (actual)              YAML (objectiu)
─────────────────          ─────────────────
+++                        ---
title = "Casa Batlló"      title: "Casa Batlló"
draft = false              draft: false
adreca = "Pg. de Gràcia"   adreca: "Pg. de Gràcia"
+++                        ---
```

Script Python de migració: `scripts/toml-to-yaml.py` (a crear).

---

## Fase 0 — Configuració inicial (sense servidor)

**Objectiu:** Sveltia CMS accessible a `/admin/` sobre GitHub Pages, autenticació via PAT.

**Prerequisits humans:**
- Joan crea una **GitHub OAuth App** (per a la Fase 1) — 5 min
- Joan invita el compte GitHub del Globus Vermell al repositori com a col·laborador (rol: Write)

### Fitxers a crear

#### `static/admin/index.html`
```html
<!doctype html>
<html lang="ca">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Administrador — Guies Barcelona</title>
</head>
<body>
  <script src="https://unpkg.com/@sveltia/cms/dist/sveltia-cms.js"></script>
</body>
</html>
```

**Notes importants:**
- NO afegir `type="module"` al script — trenca el CMS
- NO afegir `<link rel="stylesheet">` — el CMS té els seus estils

#### `static/admin/config.yml`
```yaml
backend:
  name: github
  repo: 112books/guiesbarcelona-elglobusvermell
  branch: main
  # Fase 0: PAT auth (cap base_url = mostra diàleg de PAT)
  # Fase 1: descomenta quan el proxy PHP estigui llest:
  # base_url: https://guiesbarcelona.elglobusvermell.org/oauth

media_folder: static/img/edificis
public_folder: /img/edificis

locale: ca

collections:

  # ── Fitxes d'edificis ─────────────────────────────────────────────────────
  - name: elements
    label: Edificis i elements
    label_singular: Edifici
    folder: content/ca/elements
    create: true
    extension: md
    format: yaml
    slug: "{{slug}}"
    fields:
      - { label: Títol,       name: title,      widget: string }
      - { label: Esborrany,   name: draft,      widget: boolean, default: false }
      - label: Publicacions
        name: publicacions
        widget: select
        multiple: true
        options:
          - { label: "GATCPAC",     value: gatcpac }
          - { label: "Interiors d'illa", value: interiors-illa }
          - { label: "Poblenou",    value: poblenou }
          - { label: "Mercats",     value: mercats }
          - { label: "Biblioteques", value: biblioteques }
          - { label: "76-08",       value: 76-08 }
          - { label: "09-25",       value: 09-25 }
      - { label: Adreça,      name: adreca,     widget: string,  required: false }
      - { label: Any,         name: any,        widget: number,  required: false }
      - label: Arquitectes
        name: arquitectes
        widget: list
        required: false
      - { label: Tipologia,   name: tipologia,  widget: string,  required: false }
      - { label: Protecció,   name: proteccio,  widget: string,  required: false }
      - { label: Superfície (m²), name: superficie, widget: number, required: false }
      - label: Anys de reforma
        name: anys_reforma
        widget: list
        required: false
      - label: Premis
        name: premis
        widget: list
        required: false
      - { label: Latitud,     name: lat,        widget: number,  required: false, step: 0.000001 }
      - { label: Longitud,    name: long,       widget: number,  required: false, step: 0.000001 }
      - { label: Descripció,  name: descripcio, widget: text,    required: false }
      - { label: Nomenclàtor, name: descripcio_nomenclator, widget: text, required: false }
      - { label: Cos (markdown), name: body,    widget: markdown, required: false }

  # ── Publicacions (dades) ──────────────────────────────────────────────────
  - name: publicacions
    label: Publicacions
    files:
      - label: Llista de publicacions
        name: publicacions
        file: data/publicacions.yaml
        fields:
          - label: Publicacions
            name: publicacions
            widget: list
            fields:
              - { label: Slug,   name: slug,  widget: string }
              - { label: Títol,  name: titol, widget: string }
              - { label: Color,  name: color, widget: color }
              - { label: Edició, name: edicio, widget: string }
```

### Com s'autentifiquen els editors (Fase 0 — PAT)

1. L'editor obre `https://112books.github.io/guiesbarcelona-elglobusvermell/admin/`
2. Sveltia CMS mostra un diàleg per introduir un PAT
3. Sveltia CMS ofereix un enllaç directe a GitHub per crear el PAT amb els permisos justos
4. L'editor copia el PAT generat per GitHub i el enganxa al diàleg
5. El PAT es desa al localStorage del navegador (no surt mai del dispositiu)
6. **Fet.** L'editor no torna a veure el diàleg fins que el PAT expiri o canviï d'ordinador

**PAT recomanat:** Fine-grained, scope `Contents: Read and write` + `Metadata: Read`, repositori específic, caducitat 1 any.

---

## Fase 1 — OAuth proxy PHP (quan Dinahosting estigui llest)

**Objectiu:** Login amb 1 clic "Iniciar sessió amb GitHub" en lloc del PAT manual.

### Fitxer: `oauth/index.php` (a Dinahosting)

```php
<?php
session_start();
$client_id     = $_ENV['GH_CLIENT_ID']     ?? getenv('GH_CLIENT_ID');
$client_secret = $_ENV['GH_CLIENT_SECRET'] ?? getenv('GH_CLIENT_SECRET');
$allowed_origin = 'https://guiesbarcelona.elglobusvermell.org';

// Pas 1: redirigeix a GitHub per autoritzar
if (!isset($_GET['code'])) {
    $state = bin2hex(random_bytes(16));          // CSRF token
    $_SESSION['oauth_state'] = $state;
    header("Location: https://github.com/login/oauth/authorize"
         . "?client_id=" . urlencode($client_id)
         . "&scope=public_repo"
         . "&state=" . urlencode($state));
    exit;
}

// Pas 2: GitHub retorna amb codi — valida CSRF
if (!isset($_GET['state']) || $_GET['state'] !== ($_SESSION['oauth_state'] ?? '')) {
    http_response_code(403);
    die('Invalid state — possible CSRF attack');
}
unset($_SESSION['oauth_state']);

// Pas 3: intercanvia codi per token (server-to-server)
$resp = file_get_contents('https://github.com/login/oauth/access_token', false,
    stream_context_create(['http' => [
        'method'  => 'POST',
        'header'  => "Content-Type: application/x-www-form-urlencoded\r\nAccept: application/json\r\n",
        'content' => http_build_query([
            'client_id'     => $client_id,
            'client_secret' => $client_secret,
            'code'          => $_GET['code'],
        ])
    ]])
);

$data  = json_decode($resp, true);
$token = $data['access_token'] ?? '';

if (!$token) {
    http_response_code(500);
    die('No token received from GitHub');
}

// Pas 4: retorna el token al CMS via postMessage
header('Content-Security-Policy: default-src \'none\'; script-src \'unsafe-inline\'');
echo '<script>
  (function() {
    var msg = JSON.stringify({
      token: ' . json_encode($token) . ',
      provider: "github"
    });
    window.opener.postMessage("authorization:github:success:" + msg, ' . json_encode($allowed_origin) . ');
    window.close();
  })();
</script>';
```

### Secrets a Dinahosting

Mai al repositori. Opcions per a shared hosting PHP:

1. **`.user.ini`** al directori del proxy (PHP el llegeix, Apache no el serveix):
   ```ini
   ; /oauth/.user.ini
   GH_CLIENT_ID = "abc123"
   GH_CLIENT_SECRET = "xyz..."
   ```

2. **`.htaccess` + `SetEnv`**:
   ```apache
   SetEnv GH_CLIENT_ID "abc123"
   SetEnv GH_CLIENT_SECRET "xyz..."
   ```

3. Fitxer fora del webroot (més segur): `/home/user/secrets.env` carregat amb `vlucas/phpdotenv`.

### Actualització del `config.yml` per a Fase 1

```yaml
backend:
  name: github
  repo: 112books/guiesbarcelona-elglobusvermell
  branch: main
  base_url: https://guiesbarcelona.elglobusvermell.org/oauth
```

---

## Flux editorial (workaround fins a Sveltia v1.0)

Sense editorial workflow natiu, el flux proposat és:

```
Editor edita fitxa → Sveltia guarda a branca `drafts`
                              ↓
                    Joan revisa a GitHub Pages (preview automàtic)
                              ↓
                    Joan fa merge de `drafts` → `main` via GitHub
                              ↓
                    GitHub Action → deploy a Dinahosting (producció)
```

Configuració de la branca:
```yaml
backend:
  branch: drafts   # editors escriuen aquí
```

Joan fa merge quan vol publicar. Simple, sense dependències.

---

## Gestió de rols (workaround fins a Sveltia v2.0)

Dos punts d'entrada al CMS amb `config.yml` diferent:

| Path | Qui | Pot fer |
|------|-----|---------|
| `/admin/` | Joan (master) | Tot: edificis, publicacions, temes, dades |
| `/admin-editor/` | Globus Vermell | Només edificis (fitxes) |

Cada path té el seu `index.html` i `config.yml` — el de l'editor simplement no inclou les col·leccions de configuració.

---

## Resum de tasques per implementar

Vegeu `TASKS.md` secció **CMS Editorial** per al seguiment.

### Fase 0 (sense servidor — implementable avui)
1. Script `scripts/toml-to-yaml.py` — migra frontmatter de tots els elements
2. Executar migració + verificar build Hugo
3. Commit + push dels fitxers migrats
4. Crear `static/admin/index.html` i `static/admin/config.yml`
5. Verificar CMS a GitHub Pages amb PAT de prova
6. Invitar compte GitHub del Globus Vermell al repo (rol Write)
7. Formar els editors: crear PAT i accedir al CMS

### Fase 1 (quan Dinahosting estigui llest)
8. Crear GitHub OAuth App (un per dev, un per prod)
9. Crear `oauth/index.php` amb tots els controls de seguretat
10. Configurar secrets a Dinahosting (`.user.ini` o `.htaccess`)
11. Actualitzar `config.yml` amb `base_url`
12. Provar flux OAuth complet

### Fase 2 (quan Sveltia CMS v1.0 — tardor 2026)
13. Activar editorial workflow (`publish_mode: editorial_workflow`)
14. Configurar branca de producció vs. branca de drafts
15. Revisar rols si v1.0 ja els implementa (sinó esperar v2.0)

---

## Seguretat — checklist final

- [ ] HTTPS actiu al domini de producció (Let's Encrypt via Dinahosting)
- [ ] Secrets fora del repositori i fora del webroot
- [ ] Paràmetre `state` (CSRF) implementat al proxy PHP
- [ ] `allowed_origin` validat al proxy (`window.opener.postMessage` apunta al domini correcte)
- [ ] GitHub OAuth App té el callback URL exacte (no wildcards)
- [ ] Scope mínim: `public_repo` (no `repo` complet si el repo és públic)
- [ ] PATs dels editors amb caducitat màxima 1 any
- [ ] Branca `drafts` protegida: editors no poden fer merge directament a `main`
- [ ] Revisió anual de permisos de col·laboradors al repo
