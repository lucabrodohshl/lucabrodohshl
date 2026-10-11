#!/usr/bin/env python3
"""Sanity checks for the built site in _site/ (run after `jekyll build`).

Checks internal links and assets, sitemap URLs, per-paper SEO and citation
metadata, JSON-LD validity, and uniqueness of titles and descriptions.
Exit code 1 if any check fails. Standard library only.
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parent.parent / "_site"
SITE_URL = "https://lucabrodohshl.github.io"
BASEURL = "/lucabrodohshl"

errors = []


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.meta, self.jsonld = [], [], []
        self.title, self.h1 = "", []
        self._in = None
        self._buf = ""
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("a", "link") and "href" in a:
            self.links.append(a["href"])
            if tag == "link" and a.get("rel") == "canonical":
                self.canonical = a["href"]
        if tag in ("img", "script", "source") and ("src" in a or "srcset" in a):
            if "src" in a:
                self.links.append(a["src"])
            for part in a.get("srcset", "").split(","):
                if part.strip():
                    self.links.append(part.strip().split()[0])
        if tag == "meta":
            self.meta.append(a)
        if tag in ("title", "h1") or (tag == "script" and a.get("type") == "application/ld+json"):
            self._in, self._buf = tag, ""

    def handle_data(self, data):
        if self._in:
            self._buf += data

    def handle_endtag(self, tag):
        if self._in == tag or (self._in == "script" and tag == "script"):
            if tag == "title":
                self.title = self._buf.strip()
            elif tag == "h1":
                self.h1.append(" ".join(self._buf.split()))
            elif tag == "script":
                self.jsonld.append(self._buf)
            self._in = None


def resolve(href, page_path):
    """Map a site URL to a file in _site, or None for external links."""
    u = urlparse(href)
    if u.scheme in ("mailto", "tel", "data"):
        return None
    if u.scheme in ("http", "https"):
        if not href.startswith(SITE_URL + BASEURL):
            return None
        path = u.path[len(BASEURL):]
    elif href.startswith("#") or href == "":
        return None
    elif href.startswith("/"):
        if not u.path.startswith(BASEURL + "/") and u.path != BASEURL:
            errors.append(f"{page_path}: link without baseurl: {href}")
            return None
        path = u.path[len(BASEURL):]
    else:
        path = "/" + str((page_path.parent / u.path).relative_to(ROOT))
    path = unquote(path)
    target = ROOT / path.lstrip("/")
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def meta(page, key, attr="name"):
    return [m.get("content", "") for m in page.meta if m.get(attr) == key]


pages = {}
for f in sorted(ROOT.rglob("*.html")):
    p = Page()
    p.feed(f.read_text(encoding="utf-8"))
    pages[f] = p
    for href in p.links:
        t = resolve(href, f)
        if t is not None and not t.exists():
            errors.append(f"{f.relative_to(ROOT)}: broken link {href}")
    for block in p.jsonld:
        try:
            json.loads(block)
        except json.JSONDecodeError as e:
            errors.append(f"{f.relative_to(ROOT)}: invalid JSON-LD ({e})")

# Sitemap
sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
locs = re.findall(r"<loc>(.*?)</loc>", sm)
for loc in locs:
    t = resolve(loc, ROOT / "sitemap.xml")
    if t is None or not t.exists():
        errors.append(f"sitemap: URL has no page: {loc}")

# Per-paper checks
papers = [f for f in pages if f.parent.parent == ROOT / "publications" and f.name == "index.html"]
for f in papers:
    p, rel = pages[f], f.relative_to(ROOT)
    loc = SITE_URL + BASEURL + "/" + str(rel.parent) + "/"
    if loc not in locs:
        errors.append(f"{rel}: missing from sitemap")
    if p.canonical != loc:
        errors.append(f"{rel}: canonical {p.canonical} != {loc}")
    ct = meta(p, "citation_title")
    if not ct or not p.h1 or ct[0] != p.h1[0]:
        errors.append(f"{rel}: citation_title / h1 mismatch: {ct} vs {p.h1}")
    if not meta(p, "citation_author"):
        errors.append(f"{rel}: no citation_author")
    if not meta(p, "citation_publication_date"):
        errors.append(f"{rel}: no citation_publication_date")
    for pdf in meta(p, "citation_pdf_url"):
        t = resolve(pdf, f)
        if t is None or not t.exists():
            errors.append(f"{rel}: citation_pdf_url missing file {pdf}")
        elif t.parent != f.parent:
            errors.append(f"{rel}: PDF not in the same directory as the paper page")
    desc = meta(p, "description")
    if not desc or not (50 <= len(desc[0]) <= 170):
        errors.append(f"{rel}: description length {len(desc[0]) if desc else 0}")
    html = f.read_text(encoding="utf-8")
    if 'id="abstract"' not in html:
        errors.append(f"{rel}: no abstract section")
    if '"@type": "ScholarlyArticle"' not in html:
        errors.append(f"{rel}: no ScholarlyArticle JSON-LD")

# Uniqueness of titles and descriptions across indexable pages
seen_t, seen_d = {}, {}
for f, p in pages.items():
    if any("noindex" in c for c in meta(p, "robots")):
        continue
    for key, store, val in (("title", seen_t, p.title), ("description", seen_d, (meta(p, "description") or [""])[0])):
        if val in store:
            errors.append(f"duplicate {key}: {f.relative_to(ROOT)} and {store[val]}")
        store[val] = f.relative_to(ROOT)

print(f"Checked {len(pages)} HTML pages, {len(papers)} paper pages, {len(locs)} sitemap URLs.")
if errors:
    print("\n".join("FAIL  " + e for e in errors))
    sys.exit(1)
print("All checks passed.")
