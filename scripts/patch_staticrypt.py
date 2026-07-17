"""
Patch staticrypt-encrypted HTML files:
1. Replace document.write with DOMParser + chained-script (Chrome compatibility)
2. Replace staticrypt green (#4CAF50, #76B852) with El Globus Vermell red (#c81e1e, #a01818)
"""
import sys
from pathlib import Path

OLD = "replaceHtmlCallback: null,"

NEW = r"""replaceHtmlCallback: function(plainHTML) {
                    var parser = new DOMParser();
                    var newDoc = parser.parseFromString(plainHTML, 'text/html');
                    document.title = newDoc.title;
                    newDoc.querySelectorAll('link[rel="stylesheet"]').forEach(function(link) {
                        var el = document.createElement('link');
                        el.rel = 'stylesheet'; el.href = link.href;
                        if (link.integrity) { el.integrity = link.integrity; el.crossOrigin = 'anonymous'; }
                        document.head.appendChild(el);
                    });
                    document.body.innerHTML = newDoc.body.innerHTML;
                    var scripts = Array.from(newDoc.body.querySelectorAll('script'));
                    function loadNext(i) {
                        if (i >= scripts.length) return;
                        var s = scripts[i];
                        var el = document.createElement('script');
                        if (s.src) {
                            el.src = s.src;
                            if (s.integrity) { el.integrity = s.integrity; el.crossOrigin = 'anonymous'; }
                            el.onload = function() { loadNext(i + 1); };
                            el.onerror = function() { loadNext(i + 1); };
                            document.body.appendChild(el);
                        } else {
                            el.textContent = s.textContent;
                            document.body.appendChild(el);
                            loadNext(i + 1);
                        }
                    }
                    loadNext(0);
                },"""

COLOR_REPLACEMENTS = [
    ("#4CAF50", "#c81e1e"),
    ("#76B852", "#a01818"),
]

def patch(root: Path):
    patched = 0
    skipped = 0
    for f in root.rglob("*.html"):
        content = f.read_text(encoding="utf-8")
        if OLD in content:
            new_content = content.replace(OLD, NEW)
            for old_color, new_color in COLOR_REPLACEMENTS:
                new_content = new_content.replace(old_color, new_color)
            f.write_text(new_content, encoding="utf-8")
            patched += 1
        else:
            skipped += 1
    print(f"Patched {patched} files, skipped {skipped} (not staticrypt or already patched)")

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("public")
    patch(root)
