#!/usr/bin/env python3
"""
Download images from WordPress for Hugo elements that don't have a foto field.
"""

import os
import re
import sys
import urllib.request
import urllib.error

STATIC_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org/static/img/elements"
ELEMENTS_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org/content/ca/elements"

# All WP element URLs gathered from category pages
WP_URLS = """
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/fabrica-myrurgia/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-vilaro/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-josefa-lopez/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-rossello/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-viladot/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-rodriguez-arias/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-navas-240/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-navas-238/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-rector-ubach/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-jonqueres/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-ginesta/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-unifamiliar-placa-mons/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-f-esponac/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/grup-escolar-blanquerna/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-astoria/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-xalet-passatge-roserar/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-unifamiliar-placa-jaume-ii/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-j-espona/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-padua/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/joieria-roca/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-bloc/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/dispensari-central-antituberculos/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/antics-magatzems-sepu/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/reforma-de-laula-de-quimica-a-la-ub/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-jaume-sans/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-balmes/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/reforma-dun-atic/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/botiga-cottet/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-gran-via/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-iradier/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/bloc-diagonal/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-cardenal/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-de-lart/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/dispensari-de-sant-josep-de-la-muntanya/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-lincoln/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-padilla/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-placa-bonanova/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-pi-i-margall/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-enric-granados/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-sardanes-i-bonet/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-viladomat/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/edifici-dhabitatges-carrer-balmes-2/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/adaptacio-dun-convent-per-a-escola-del-cenu/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/pavello-de-la-republica-de-1937/
https://guiesbarcelona.elglobusvermell.org/avantguarda-1928-1938/casa-montepio-dempleats/
https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/les-escales-park/
https://guiesbarcelona.elglobusvermell.org/moderna-1950-1975/fundacio-joan-miro/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/farinera-sant-jaume-la-farinera-del-clot/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/can-tiana-il3-ub/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/fabrica-de-llorenc-pons-i-clerch/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/hispano-olivetti/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/netol/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/industrias-metalicas-sa/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/ca-laranyo/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/cotxeres-de-tmb/
https://guiesbarcelona.elglobusvermell.org/poblenou-industrial/la-ciutat-groga/
https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-diagonal-ciutat-de-granada-bolivia-badajoz/
https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-de-ca-laranyo/
https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/placa-de-dolors-piera-placa-disabel-vila/
https://guiesbarcelona.elglobusvermell.org/eixample-jardins-interiors/jardins-dada-byron/
https://guiesbarcelona.elglobusvermell.org/biblioteques/biblioteca-el-clot-josep-benet/
""".strip().splitlines()

# Build slug -> url mapping (slug is last path component)
wp_slug_to_url = {}
for url in WP_URLS:
    url = url.strip()
    if not url:
        continue
    slug = url.rstrip('/').split('/')[-1]
    # Keep first occurrence per slug (some appear in multiple categories)
    if slug not in wp_slug_to_url:
        wp_slug_to_url[slug] = url

print(f"Total WP slugs indexed: {len(wp_slug_to_url)}")

# Find Hugo elements without foto:
hugo_no_foto = []
for fname in sorted(os.listdir(ELEMENTS_DIR)):
    if fname == '_index.md' or not fname.endswith('.md'):
        continue
    fpath = os.path.join(ELEMENTS_DIR, fname)
    with open(fpath) as f:
        content = f.read()
    if not re.search(r'^foto:', content, re.MULTILINE):
        hugo_no_foto.append(fname[:-3])  # strip .md

print(f"Hugo elements without foto: {len(hugo_no_foto)}")
print()

# Also find elements already downloaded (in static/img/elements)
already_downloaded = set(
    f[:-4] for f in os.listdir(STATIC_DIR) if f.endswith('.jpg') or f.endswith('.png') or f.endswith('.webp')
)
print(f"Already in static/img/elements: {sorted(already_downloaded)}")
print()


def fetch_page_html(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.read().decode('utf-8', errors='replace')


# Known logo/placeholder URLs to skip — not real building photos
LOGO_URLS = {
    'https://guiesbarcelona.elglobusvermell.org/wp-content/uploads/2021/10/cropped-AU-guies_logoweb-gris-1.jpg',
    'https://guiesbarcelona.elglobusvermell.org/wp-content/uploads/2021/10/cropped-AU-guies_logoweb-gris-2-180x180.jpg',
    'https://guiesbarcelona.elglobusvermell.org/wp-content/uploads/2021/10/cropped-AU-guies_logoweb-gris-2-192x192.jpg',
    'https://guiesbarcelona.elglobusvermell.org/wp-content/uploads/2021/10/cropped-AU-guies_logoweb-gris-2-32x32.jpg',
}


def extract_main_image(html):
    """Extract the best candidate for the main/featured image from WP page HTML.
    Returns None if no real building photo is found (only logos/placeholders).
    """
    # Try og:image first
    og = re.findall(r'property=["\']og:image["\']\s+content=["\'](https?://[^"\']+)["\']', html)
    if not og:
        og = re.findall(r'content=["\'](https?://[^"\']+)["\'][^>]*property=["\']og:image["\']', html)
    if og and og[0] not in LOGO_URLS:
        return og[0]

    # Try -scaled.jpg (full-size WP image)
    scaled = re.findall(r'(https://guiesbarcelona\.elglobusvermell\.org/wp-content/uploads/[^"\']+?-scaled\.(jpg|jpeg|png|webp))', html, re.I)
    candidates = [u for u, _ in scaled if u not in LOGO_URLS]
    if candidates:
        return candidates[0]

    # Fallback: any WP uploads image that isn't a logo/thumbnail
    imgs = re.findall(r'(https://guiesbarcelona\.elglobusvermell\.org/wp-content/uploads/[^"\']+?\.(jpg|jpeg|png|webp))', html, re.I)
    non_thumb = [u for u, _ in imgs
                 if u not in LOGO_URLS
                 and not re.search(r'-\d+x\d+\.(jpg|jpeg|png|webp)$', u, re.I)]
    if non_thumb:
        return non_thumb[0]
    # Last resort: any non-logo image including thumbnails
    real_imgs = [u for u, _ in imgs if u not in LOGO_URLS]
    if real_imgs:
        return real_imgs[0]

    return None


def download_image(img_url, dest_path):
    req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    with open(dest_path, 'wb') as f:
        f.write(data)
    return len(data)


# --- Match and download ---
matched = []
no_match = []
already_have = []
download_errors = []
downloaded = []

for hugo_slug in hugo_no_foto:
    # Skip if image already downloaded
    if hugo_slug in already_downloaded:
        already_have.append(hugo_slug)
        continue

    # Direct slug match
    wp_url = wp_slug_to_url.get(hugo_slug)

    # Try partial/fuzzy matches for known variants
    if not wp_url:
        # e.g. casa-unifamiliar -> casa-unifamiliar-placa-mons or casa-unifamiliar-placa-jaume-ii
        candidates = [s for s in wp_slug_to_url if s.startswith(hugo_slug + '-') or hugo_slug.startswith(s + '-')]
        if len(candidates) == 1:
            wp_url = wp_slug_to_url[candidates[0]]
        elif len(candidates) > 1:
            print(f"  AMBIGUOUS match for {hugo_slug}: {candidates}")

    if not wp_url:
        no_match.append(hugo_slug)
        continue

    matched.append((hugo_slug, wp_url))

    # Determine file extension from URL
    ext = 'jpg'
    dest_path = os.path.join(STATIC_DIR, f"{hugo_slug}.{ext}")

    print(f"Fetching page: {wp_url}")
    try:
        html = fetch_page_html(wp_url)
    except Exception as e:
        print(f"  ERROR fetching page: {e}")
        download_errors.append((hugo_slug, wp_url, f"page fetch: {e}"))
        continue

    img_url = extract_main_image(html)
    if not img_url:
        print(f"  WARNING: No image found on {wp_url}")
        download_errors.append((hugo_slug, wp_url, "no image found on page"))
        continue

    # Determine extension from image URL
    img_ext_match = re.search(r'\.(jpg|jpeg|png|webp)$', img_url, re.I)
    if img_ext_match:
        ext = img_ext_match.group(1).lower()
        if ext == 'jpeg':
            ext = 'jpg'
    dest_path = os.path.join(STATIC_DIR, f"{hugo_slug}.{ext}")

    print(f"  Image: {img_url}")
    print(f"  -> {dest_path}")
    try:
        size = download_image(img_url, dest_path)
        print(f"  OK ({size} bytes)")
        downloaded.append((hugo_slug, img_url, dest_path, size))
    except Exception as e:
        print(f"  ERROR downloading image: {e}")
        download_errors.append((hugo_slug, wp_url, f"image download: {e}"))

print()
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"\nHugo elements without foto: {len(hugo_no_foto)}")
print(f"Already had image in static/: {len(already_have)} -> {already_have}")
print(f"Matched to WP page: {len(matched)}")
print(f"No WP match found: {len(no_match)}")
print()
print(f"Successfully downloaded: {len(downloaded)}")
for hugo_slug, img_url, dest_path, size in downloaded:
    print(f"  {hugo_slug}: {img_url} -> {os.path.basename(dest_path)} ({size} bytes)")

print()
print(f"Errors/warnings: {len(download_errors)}")
for hugo_slug, wp_url, err in download_errors:
    print(f"  {hugo_slug} ({wp_url}): {err}")

print()
print(f"No WP match ({len(no_match)}):")
for s in no_match:
    print(f"  {s}")
