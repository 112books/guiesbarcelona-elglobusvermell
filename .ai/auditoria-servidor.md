# Auditoria del servidor — El Globus Vermell
**Data:** 26 octubre 2026  
**Redactada per:** LinuxBCN  
**Fonts:** inspecció remota (DNS, headers HTTP) + correu de Jorge (Virtubio.net, 26/10/2026)  
**Estat:** COMPLETA (seccions [PENDENT] requereixen accés al servidor per verificar detalls menors)

---

## 1. Infraestructura

| Camp | Valor |
|------|-------|
| Proveïdor hosting | **Hetzner** (VPS) |
| Tipus de servidor | **VPS (servidor virtual privat)** |
| Gestió del servidor | Virtubio.net — Jorge (hola@linuxbcn.com) |
| IP pública | 195.201.2.76 |
| PTR (reverse DNS) | elglobusvermell.org |
| Sistema operatiu | **Debian** (base de YunoHost) |
| Programari de gestió | **YunoHost** — https://yunohost.org |
| Panell d'administració | https://panel.elglobusvermell.org/yunohost/admin/ |
| CLI administració | `yunohost help` / `yunohost app list` (doc: https://doc.yunohost.org/en/admin/command_line) |
| RAM / Disc / CPU | [PENDENT — veure panel YunoHost o `free -h` / `df -h`] |

---

## 2. Webs allotjades

### 2a. elglobusvermell.org — web principal

| Camp | Valor |
|------|-------|
| URL | https://elglobusvermell.org |
| CMS | WordPress |
| Directori | `/var/www/elglobusvermell/` → symlink a `/var/www/wordpress__2/` |
| wp-config.php | `/var/www/wordpress__2/wp-config.php` |
| Versió WordPress | [PENDENT] |
| Estat | Actiu en producció |
| Notes | Web principal d'El Globus Vermell. **No tocar fins a OK de Joan.** |

### 2b. guiesbarcelona.elglobusvermell.org — guies de Barcelona

| Camp | Valor |
|------|-------|
| URL | https://guiesbarcelona.elglobusvermell.org |
| CMS | WordPress (actual) → **Hugo** (migració en curs) |
| Directori | `/var/www/guiesbarcelona/` → symlink a `/var/www/wordpress__3/` |
| wp-config.php | `/var/www/wordpress__3/wp-config.php` |
| Versió WordPress | [PENDENT] |
| Estat | En producció (WP) — Hugo disponible a GitHub Pages com a staging |
| Notes | Quan Joan doni l'OK, el deploy Hugo substituirà el contingut d'aquest directori via rsync SSH. |

### 2c. my_webapp

| Camp | Valor |
|------|-------|
| Directori | `/var/www/my_webapp/` |
| Estat | Probable import o backup antic (confirmar amb Jorge) |
| Acció | Revisar i eliminar si no cal |

---

## 3. Servidor web

| Camp | Valor |
|------|-------|
| Programari | **nginx** (confirmat per headers HTTP `Server: nginx`) |
| Versió nginx | [PENDENT — `nginx -v`] |
| Gestió vhosts | Via YunoHost (configuració automàtica per app) |
| PHP | [PENDENT — `php -v`] |
| PHP-FPM | Probable (YunoHost gestiona PHP-FPM per defecte) |

**Capçaleres de seguretat detectades (correctes):**
- `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload`
- `X-Content-Type-Options: nosniff`
- `X-XSS-Protection: 1; mode=block`
- `X-Frame-Options: SAMEORIGIN`
- `Content-Security-Policy: upgrade-insecure-requests`
- `Permissions-Policy: interest-cohort=()`

---

## 4. Base de dades

| Camp | Valor |
|------|-------|
| Motor | **MariaDB** (confirmat per Jorge) |
| Versió | [PENDENT — `mariadb --version`] |
| Credencials webs | Als `wp-config.php` de cada instal·lació |
| Dump fàcil | `yunohost backup create` o `mysqldump` directe |
| Accés remot | Port 3306 no accessible des de l'exterior (bo) |

---

## 5. Correu electrònic

| Camp | Valor |
|------|-------|
| Arquitectura | El servidor **rep el correu** i el **reenvia a Gmail** |
| Gestió | YunoHost (gestor de correu integrat) |
| SMTP | Actiu — el fan servir per enviar correus des de les webs (WordPress, formularis) |
| Recepció | Servidor rep → redirigit a Gmail (no s'emmagatzema localment) |
| MX | `elglobusvermell.org` (prioritat 10) → 195.201.2.76 |
| SPF | `v=spf1 a mx -all` — configurat |
| DKIM | [PENDENT — YunoHost configura DKIM automàticament; cal verificar] |
| DMARC | [PENDENT — `dig TXT _dmarc.elglobusvermell.org`] |
| Comptes | [PENDENT — `yunohost user list`] |

**Nota:** L'arquitectura actual (servidor de correu propi + redirecció a Gmail) és funcional però comporta responsabilitat de manteniment del servidor de correu (reputació IP, llistes negres, actualitzacions). Alternativa més simple: migrar MX directament a Gmail/Google Workspace i eliminar el relay.

---

## 6. Còpies de seguretat

| Camp | Valor |
|------|-------|
| Còpies automàtiques | **Sí — Hetzner fa backup diari de tot el VPS** |
| Freqüència | Diària |
| Gestor còpies | YunoHost també té sistema de backup propi (`yunohost backup list`) |
| Backup BD | `yunohost backup create` inclou BD / o `mysqldump` manual |
| Còpies repositori | Contingut Hugo: sí (GitHub, branca main) |
| Imatges/PDFs WP | Incloses al backup Hetzner del VPS |

**Bon nivell de protecció.** El backup diari de Hetzner cobreix tot el servidor. Recomanable fer també exports manuals periòdics de la BD i pujar-los a un lloc extern (S3, Drive) per tenir còpia independent del proveïdor.

---

## 7. Accés SSH i usuaris

| Camp | Valor |
|------|-------|
| Port SSH | [PENDENT — no és el 22; filtrat des de l'exterior. Confirmar amb Jorge.] |
| Usuari | root (accés confirmat per Jorge) |
| Autenticació | Clau pública SSH (clau LinuxBCN ja afegida) |
| Permisos anteriors | Limitats (corregit per Jorge el 26/10/2026 — ara root) |
| Gestió usuaris | `yunohost user list` |
| Panell web alternatiu | https://panel.elglobusvermell.org/yunohost/admin/ |

---

## 8. Certificats SSL

| Camp | Valor |
|------|-------|
| Proveïdor | **Let's Encrypt** (YunoHost gestiona Let's Encrypt automàticament) |
| Renovació | Automàtica via YunoHost (`yunohost domain cert-status`) |
| Dominis coberts | elglobusvermell.org, guiesbarcelona.elglobusvermell.org, panel.elglobusvermell.org |
| HSTS | Actiu amb preload |
| Caducitat | [PENDENT — `yunohost domain cert-status`] |

---

## 9. DNS (joker.com)

| Camp | Valor |
|------|-------|
| Registrar | **joker.com** |
| Nameservers | x.ns.joker.com, y.ns.joker.com, z.ns.joker.com |
| Accés | El Globus Vermell (Joan) té accés directe al panell joker.com |
| A elglobusvermell.org | 195.201.2.76 |
| A guiesbarcelona.elglobusvermell.org | 195.201.2.76 |
| A panel.elglobusvermell.org | 195.201.2.76 |
| MX elglobusvermell.org | elglobusvermell.org (prioritat 10) → 195.201.2.76 |

---

## 10. Versions de programari

| Programari | Versió | Notes |
|------------|--------|-------|
| Sistema operatiu | Debian (base YunoHost) | [versió exacta PENDENT] |
| YunoHost | [PENDENT — `yunohost version`] | Gestor del servidor |
| nginx | [PENDENT — `nginx -v`] | Servidor web |
| PHP | [PENDENT — `php -v`] | |
| MariaDB | [PENDENT — `mariadb --version`] | Base de dades |
| WordPress (elglobusvermell.org) | [PENDENT] | |
| WordPress (guiesbarcelona) | [PENDENT] | Serà substituït per Hugo |

Per obtenir tot en una línia, des del servidor:
```bash
yunohost version && nginx -v 2>&1 && php -v | head -1 && mariadb --version && yunohost app list
```

---

## 11. Resum per valorar la responsabilitat de gestió del servei

### Què inclou gestionar aquest servidor

| Àrea | Responsabilitat | Complexitat |
|------|----------------|-------------|
| Actualitzacions YunoHost/Debian | Aplicar updates de seguretat periòdicament | Baixa (YunoHost ho simplifica) |
| WordPress (elglobusvermell.org) | Actualitzar WP + plugins + temes | Mitjana |
| WordPress (guiesbarcelona) | Transitòria — serà substituït per Hugo estàtic | Baixa un cop migrat |
| Servidor de correu | Mantenir reputació IP, evitar blacklists, DKIM/DMARC | Mitjana-Alta |
| Còpies de seguretat | Supervisar que el backup Hetzner funciona; backup BD manual | Baixa |
| SSL/TLS | Automàtic via YunoHost | Cap |
| DNS | Gestió al panell joker.com (accés del client) | Baixa |
| Monitorització | Cap sistema actiu detectat | Caldria configurar-ne |
| Deploy Hugo | Rsync SSH manual o via GitHub Actions | Baixa un cop configurat |

### Punt crític: el correu

El servidor de correu propi és el component de major risc operatiu: si la IP apareix en una llista negra (spam blacklist), els correus de les dues webs deixarien d'arribar. Recomanació: valorar si val la pena mantenir el servidor de correu propi o migrar MX a un servei gestionat (Google Workspace, Fastmail).

### Simplificació possible un cop migrat Hugo

Un cop `guiesbarcelona` sigui Hugo estàtic, el servidor quedarà amb:
- Un WordPress (elglobusvermell.org)
- Fitxers estàtics Hugo (guiesbarcelona)
- Servidor de correu (relay → Gmail)

Càrrega de manteniment baixa, adequada per gestió ocasional.
