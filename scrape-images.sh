#!/usr/bin/env bash
# Script to scrape images from WP site for Hugo elements
# Requires bash 4+ (brew install bash) or uses python for associative arrays

BASE_DIR="/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org"
ELEMENTS_DIR="$BASE_DIR/content/ca/elements"
IMG_DIR="$BASE_DIR/static/img/elements"
WP_URLS_FILE="/Users/joan/.claude/projects/-Users-joan-Documents-Obsidian-elglobusvermell-org/6a3c2b1c-61f1-4d4d-831d-a20461e3c8de/tool-results/bqdyb7l9s.txt"

mkdir -p "$IMG_DIR"

# Use python to do all the heavy work
python3 << 'PYEOF'
import os
import re
import sys
import time
import urllib.request
import urllib.error

BASE_DIR = "/Users/joan/Documents/Obsidian/elglobusvermell.org/guiesbarcelona.elglobusvermell.org"
ELEMENTS_DIR = os.path.join(BASE_DIR, "content/ca/elements")
IMG_DIR = os.path.join(BASE_DIR, "static/img/elements")
WP_URLS_FILE = "/Users/joan/.claude/projects/-Users-joan-Documents-Obsidian-elglobusvermell-org/6a3c2b1c-61f1-4d4d-831d-a20461e3c8de/tool-results/bqdyb7l9s.txt"

os.makedirs(IMG_DIR, exist_ok=True)

# Load WP URLs: extract slug -> full URL
wp_url_map = {}
with open(WP_URLS_FILE) as f:
    for line in f:
        url = line.strip()
        # Match post URLs: https://domain/section/slug/
        m = re.match(r'^https://guiesbarcelona\.elglobusvermell\.org/[^/]+/([^/]+)/$', url)
        if m:
            slug = m.group(1)
            wp_url_map[slug] = url

print(f"Loaded {len(wp_url_map)} WP post URLs")

def get_og_image(url):
    """Fetch a URL and extract og:image meta tag"""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=20) as resp:
            html = resp.read().decode('utf-8', errors='replace')

        # Try both orderings of og:image attributes
        patterns = [
            r'<meta\s+property=["\']og:image["\']\s+content=["\'](https?://[^"\']+)["\']',
            r'<meta\s+content=["\'](https?://[^"\']+)["\']\s+property=["\']og:image["\']',
            r'<meta\s+property=["\']og:image["\']\s+content=["\'](//[^"\']+)["\']',
        ]
        for pat in patterns:
            m = re.search(pat, html, re.IGNORECASE)
            if m:
                img = m.group(1)
                if img.startswith('//'):
                    img = 'https:' + img
                return img
        return None
    except Exception as e:
        print(f"  Fetch error: {e}")
        return None

def download_image(img_url, dest_path):
    """Download image to dest_path, return True on success"""
    try:
        req = urllib.request.Request(img_url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) < 1000:
            print(f"  File too small ({len(data)} bytes)")
            return False
        with open(dest_path, 'wb') as f:
            f.write(data)
        return True
    except Exception as e:
        print(f"  Download error: {e}")
        return False

def add_foto_to_frontmatter(md_file, foto_path):
    """Add foto field to YAML front matter if not already present"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'foto:' in content:
        return False  # already has foto

    # Insert foto after draft line
    new_content = re.sub(
        r'^(draft: (?:false|true))$',
        r'\1\nfoto: ' + foto_path,
        content,
        count=1,
        flags=re.MULTILINE
    )

    if new_content == content:
        # Try inserting before closing ---
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front = parts[1]
            front = front.rstrip() + '\nfoto: ' + foto_path + '\n'
            new_content = '---' + front + '---' + parts[2]

    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

# Stats
matched = 0
images_found = 0
images_downloaded = 0
no_match = []
no_image = []
already_has_foto = []

# Get all element md files
md_files = sorted([
    f for f in os.listdir(ELEMENTS_DIR)
    if f.endswith('.md') and f != '_index.md'
])

print(f"Processing {len(md_files)} Hugo elements\n")

for filename in md_files:
    hugo_slug = filename[:-3]  # remove .md
    md_file = os.path.join(ELEMENTS_DIR, filename)

    # Check if already has foto
    with open(md_file, 'r', encoding='utf-8') as f:
        existing_content = f.read()
    if 'foto:' in existing_content:
        already_has_foto.append(hugo_slug)
        print(f"[{hugo_slug}] Already has foto, skipping")
        continue

    # Try to find matching WP URL
    wp_url = None

    # Direct match
    if hugo_slug in wp_url_map:
        wp_url = wp_url_map[hugo_slug]
    else:
        # Try stripping trailing -2, -3, etc
        base = re.sub(r'-\d+$', '', hugo_slug)
        if base != hugo_slug and base in wp_url_map:
            wp_url = wp_url_map[base]
        else:
            # Try partial slug matching: hugo slug might have more or fewer words
            # Find WP slugs that start with hugo_slug or vice versa
            for wp_slug, url in wp_url_map.items():
                if hugo_slug.startswith(wp_slug) or wp_slug.startswith(hugo_slug):
                    wp_url = url
                    break

    if not wp_url:
        no_match.append(hugo_slug)
        print(f"[{hugo_slug}] NO WP MATCH")
        continue

    matched += 1
    print(f"[{hugo_slug}] -> {wp_url}")

    # Get og:image
    img_url = get_og_image(wp_url)

    if not img_url:
        no_image.append(hugo_slug)
        print(f"  No og:image found")
        time.sleep(0.5)
        continue

    print(f"  Image: {img_url}")
    images_found += 1

    # Determine extension
    ext_match = re.search(r'\.(jpg|jpeg|png|webp|gif)(\?|$)', img_url, re.IGNORECASE)
    ext = ext_match.group(1).lower() if ext_match else 'jpg'
    if ext == 'jpeg':
        ext = 'jpg'

    dest_filename = f"{hugo_slug}.{ext}"
    dest_path = os.path.join(IMG_DIR, dest_filename)

    # Download
    if download_image(img_url, dest_path):
        file_size = os.path.getsize(dest_path)
        print(f"  Downloaded: {dest_filename} ({file_size:,} bytes)")
        images_downloaded += 1

        # Add foto to front matter
        foto_path = f"/img/elements/{dest_filename}"
        if add_foto_to_frontmatter(md_file, foto_path):
            print(f"  Added foto: {foto_path}")
        else:
            print(f"  foto already present")
    else:
        no_image.append(f"{hugo_slug} (download error)")

    time.sleep(0.5)

print("\n" + "="*50)
print("SUMMARY")
print("="*50)
print(f"Hugo elements processed: {len(md_files)}")
print(f"Already had foto (skipped): {len(already_has_foto)}")
print(f"Matched to WP URL: {matched}")
print(f"Images found (og:image): {images_found}")
print(f"Images downloaded: {images_downloaded}")
print(f"\nNO WP MATCH ({len(no_match)}):")
for s in no_match:
    print(f"  - {s}")
print(f"\nNO IMAGE ({len(no_image)}):")
for s in no_image:
    print(f"  - {s}")
print(f"\nALREADY HAD FOTO ({len(already_has_foto)}):")
for s in already_has_foto:
    print(f"  - {s}")
PYEOF
