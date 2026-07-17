#!/usr/bin/env python3
"""
Substitueix el cos de content/ca/publicacions/<slug>/_index.md pel text llarg
real de la categoria "text" (id 1) del WP en viu, preservant el frontmatter
(title, edicio) ja establert.
"""

import html
import json
import re
import urllib.request
from pathlib import Path

API = "https://guiesbarcelona.elglobusvermell.org/wp-json/wp/v2"
REPO = Path(__file__).parent.parent

WP_SLUG_TO_PUB = {
    "gatcpac": "gatcpac",
    "interiors-illa": "interiors-illa",
    "poblenou": "poblenou",
    "arquitectura-moderna-a-barcelona-1950-1975": "50-75",
    "mercats": "mercats",
    "barceloneta": "barceloneta",
    "la-marina-del-port-i-del-prat-vermell-passat-i-present": "marina",
    "masies": "masies",
    "biblioteques": "biblioteques",
    "arquitectura-a-barcelona-1975-2008-de-lesperanca-a-la-crisi": "76-08",
    "arquitectura-a-barcelona-2010-2025-la-revolucio-tranquilla": "09-25",
}


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def html_to_markdown_ish(raw_html: str) -> str:
    """Converteix el HTML de WP a text net amb paràgrafs i ## per subtítols
    en majúscules (patró recurrent: 'EVOLUCIÓ HISTÒRICA' com a <p><strong>)."""
    # Separem per paràgrafs
    paragraphs = re.findall(r"<p[^>]*>(.*?)</p>", raw_html, re.DOTALL)
    out = []
    for p in paragraphs:
        text = re.sub(r"<[^>]+>", "", p)
        text = html.unescape(text).strip()
        if not text or text in ("&nbsp;", " "):
            continue
        # Subtítol curt tot en majúscules -> ## Heading
        if text.isupper() and len(text) < 60:
            out.append(f"## {text.title()}")
        else:
            out.append(text)
    return "\n\n".join(out)


def main():
    posts = fetch_json(f"{API}/posts?categories=1&per_page=20&_fields=slug,title,content")
    print(f"{len(posts)} articles de text trobats")

    for post in posts:
        pub_slug = WP_SLUG_TO_PUB.get(post["slug"])
        if not pub_slug:
            print(f"  ! slug WP desconegut, omès: {post['slug']}")
            continue

        target = REPO / "content/ca/publicacions" / pub_slug / "_index.md"
        if not target.exists():
            print(f"  ! no existeix {target}, omès")
            continue

        current = target.read_text(encoding="utf-8")
        m = re.match(r"^(---\n.*?\n---\n)", current, re.DOTALL)
        if not m:
            print(f"  ! frontmatter no trobat a {target}, omès")
            continue
        frontmatter = m.group(1)

        body = html_to_markdown_ish(post["content"]["rendered"])
        target.write_text(frontmatter + "\n" + body + "\n", encoding="utf-8")
        print(f"  ✓ {pub_slug} actualitzat ({len(body)} caràcters)")


if __name__ == "__main__":
    main()
