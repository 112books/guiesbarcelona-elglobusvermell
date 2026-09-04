# Guia ràpida per a editors — Sveltia CMS

Guies Barcelona · El Globus Vermell

---

## Primer accés (una sola vegada)

### Pas 1 — Crea un compte a GitHub

Si no en tens, ves a [github.com](https://github.com) → Sign up. L'usuari de GitHub és la teva identitat per editar.

Comunica l'usuari a Joan (LinuxBCN) perquè et doni accés al repositori.

---

### Pas 2 — Genera un token d'accés

Un **token d'accés** és una clau que permet al CMS modificar el contingut en el teu nom. Es genera una vegada i queda desat al navegador.

1. Ves a: **github.com → icona del teu avatar (dalt a la dreta) → Settings**

   ![Menú d'usuari de GitHub amb l'opció Settings ressaltada](https://docs.github.com/assets/images/help/settings/userbar-account-settings-global-nav-update.png)

2. Menú esquerre, fins al final: **Developer settings**

3. **Personal access tokens → Fine-grained tokens → Generate new token**

4. Omple el formulari:
   - **Token name:** `Sveltia CMS — Guies Barcelona`
   - **Expiration:** 1 year (o el termini que vulguis)
   - **Resource owner:** selecciona `112books` (no el teu usuari personal)
   - **Repository access:** Only selected repositories → `guiesbarcelona-elglobusvermell`
   - **Repository permissions:**
     - `Contents` → **Read and write**
     - `Metadata` → **Read-only** (s'activa automàticament)

5. Clica **Generate token**

6. **Copia el token** (comença per `github_pat_...`) — només es veu una vegada

   ![Avís de GitHub i token generat amb el botó de còpia ressaltat](https://docs.github.com/assets/images/help/settings/personal-access-tokens.png)

   > **Important:** Un cop tanques aquesta pàgina, el token no el pots tornar a veure. Si el perds, cal generar-ne un de nou.

---

### Pas 3 — Accedeix al CMS

Obre al navegador:

```
https://112books.github.io/guiesbarcelona-elglobusvermell/admin-editor/
```

1. Clica **"Sign in with a Personal Access Token"** (o "Sign In Using Access Token")
2. Enganxa el token que has copiat
3. Clica **Sign in**

Ja tens accés. La propera vegada que obris el CMS al mateix navegador, entraràs directament sense tornar a introduir el token.

Un cop dins, veuràs la llista d'edificis i el panell d'edició:

![Interfície principal de Sveltia CMS amb la llista d'entrades i el panell d'edició](https://sveltiacms.app/images/highlights/screenshot-1.webp?20250405)

---

## Editar una fitxa d'edifici

1. Al menú esquerre: **Edificis i elements**
2. Busca l'edifici per nom (camp de cerca a la part superior)
3. Clica l'edifici per obrir-lo
4. Modifica els camps que calgui:
   - **Títol** — nom de l'edifici
   - **Publicacions** — a quins plànols-guia pertany
   - **Adreça**, **Any**, **Arquitectes** — dades principals
   - **Descripció** — text descriptiu
5. Clica **Save** (dalt a la dreta)

Els canvis s'apliquen directament al web en uns minuts (GitHub Pages tarda ~2 min en reconstruir).

---

## Crear una fitxa nova

1. **Edificis i elements → New Edifici** (botó superior dret)
2. Omple els camps
3. El **Títol** generarà automàticament l'URL (slug) de la fitxa
4. Guarda

---

## Camps del formulari

| Camp | Obligatori | Descripció |
|------|-----------|------------|
| Títol | Sí | Nom de l'edifici |
| Esborrany | — | Marca si no vol aparèixer al web |
| Publicacions | Sí | Plànol(s)-guia (selecció múltiple) |
| Temes transversals | No | Espai públic, Art públic, etc. |
| Adreça | Recomanat | Carrer i número |
| Any | Recomanat | Any de construcció |
| Arquitectes | Recomanat | Un nom per línia |
| Latitud / Longitud | Recomanat | Coordenades GPS per al mapa |
| Descripció | Recomanat | Text descriptiu de l'edifici |

---

## Preguntes freqüents

**El web no s'ha actualitzat.** Els canvis triguen ~2 minuts. Si passa de 5 minuts, avisa a Joan.

**He perdut el token.** Genera'n un de nou seguint el Pas 2. L'anterior quedarà invàlid.

**Veig un missatge d'error en desar.** Comprova que tens connexió a internet i que el token no ha caducat. Si ha passat 1 any des que el vas crear, cal generar-ne un de nou.

**Vull canviar una publicació o un tema transversal.** Aquests no els pots editar tu — contacta amb Joan.

---

## Contacte

Joan Roca · LinuxBCN · linuxbcn@gmail.com
