---
name: Servidor de producció — accés i credencials
description: Accés SSH root confirmat per Jorge (Virtubio.net). Credencials BD al wp-config.php. DNS a joker.com. Totes les credencials pendents rebudes el 28/10/2026.
type: project
originSessionId: 86331f59-486e-47bd-b6a2-f2899f4ab6bd
---
Jorge de Virtubio.net ha confirmat accés complet al servidor de producció.

## SSH
- **IP:** 195.201.2.76
- **Port:** 21100
- **Usuari:** tech
- **Clau:** id_ed25519 pròpia
- **Config recomanada:**
  ```
  host hetzner-elglobusvermell
    HostName 195.201.2.76
    Port 21100
    User tech
    IdentityFile ~/.ssh/id_ed25519-de-la-teva-clau
  ```
- Accés root: `sudo su -` des de l'usuari `tech`, o sessions tmux actives de Jorge

## Hetzner
- **Titular:** Jorge Vitoria Rubio (Virtubio.net) — vol traspassar la propietat
- **Customer ID Jorge:** K0628817718 (necessari per fer el transfer intern a Hetzner)
- **Pla:** CPX11 + Volum (40 GB) + Backup activat
  - 2 CPUs, 2 GB RAM, 40 GB disc NVMe
  - Backup diari (últims 7 dies), guarda 20% del preu instància
  - Cost mensual: ~9.38 € (sense IVA)
- **Acció pendent:** El Globus Vermell ha de crear compte Hetzner i demanar transfer intern (Customer ID: K0628817718)

## YunoHost
- **Panell:** https://panel.elglobusvermell.org/yunohost/admin/
- **Credencials admin:** al fitxer `/root/yunohost-elglobus-tech-admin.md` al servidor
- Accés via `sudo su -` des de `tech`

## Correu
- **Comptes i redireccions Gmail:** a `/root/2026-10-28-elglobus-users-info.txt` al servidor
- **DKIM:** configurat i actiu
  - Selector: `mail._domainkey.elglobusvermell.org`
  - Verificat a mxtoolbox

## Base de dades
- Credencials als fitxers `wp-config.php` dins `/var/www` — dues instal·lacions WordPress

## DNS
- Domini `guiesbarcelona.elglobusvermell.org` al registrar joker.com
- El Globus Vermell té accés per canviar registres DNS

## Backups Hetzner
- Backups diaris automàtics, últims 7 dies
- Accés actual: únicament Jorge des del seu panell Hetzner
- Quedarà accessible quan El Globus Vermell assumeixi el compte Hetzner

**Why:** Bloquejava el deploy directe Hugo → servidor. Ara és possible fer rsync SSH sense intermediaris.

**How to apply:** Quan Joan doni l'OK per al tall del domini:
1. Llegir credencials de `/root/yunohost-elglobus-tech-admin.md` i `/root/2026-10-28-elglobus-users-info.txt`
2. Fer rsync SSH del build Hugo al servidor
3. Configurar nginx/Apache per servir Hugo en lloc de WordPress
4. Canviar DNS a joker.com si cal apuntar a nou servidor
5. Iniciar procés de transfer del compte Hetzner a El Globus Vermell

⚠️ El WordPress de producció NO es toca fins a l'OK explícit de Joan (regla activa, 26/10/2026).
