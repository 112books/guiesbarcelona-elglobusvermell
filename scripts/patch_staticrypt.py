"""
Patch staticrypt-encrypted HTML files to replace document.write with a
DOMParser + chained-script approach that Chrome doesn't block.
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

def patch(root: Path):
    patched = 0
    skipped = 0
    for f in root.rglob("*.html"):
        content = f.read_text(encoding="utf-8")
        if OLD in content:
            f.write_text(content.replace(OLD, NEW), encoding="utf-8")
            patched += 1
        else:
            skipped += 1
    print(f"Patched {patched} files, skipped {skipped} (not staticrypt or already patched)")

if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("public")
    patch(root)
