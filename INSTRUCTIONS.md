# Luca Brodo — academic website

Static Jekyll site deployed to GitHub Pages with GitHub Actions.

- Site URL: **https://lucabrodohshl.github.io/** (GitHub Pages *user site*, repository `lucabrodohshl/lucabrodohshl.github.io`)
- `url` and `baseurl` (empty) are set in [`_config.yml`](_config.yml) and drive canonical links, Open Graph, `citation_pdf_url`, JSON-LD and the sitemap.

## Structure

| Path | Content |
|---|---|
| `index.html` | Home: introduction, research overview, selected publications, contact |
| `research/index.html` | Research page, generated from [`_data/research.yml`](_data/research.yml) |
| `publications/index.html` | Publication list (selected, then by year) |
| `_publications/*.md` | One file per paper (see below) |
| `teaching/index.html` | Teaching page, generated from [`_teaching/`](_teaching/) |
| `impressum/index.html` | Legal notice |
| `_data/navigation.yml` | Main navigation (Home, Research, Publications, Teaching) |
| `_includes/pub-entry.html` | One bibliography entry, used on every list |
| `_plugins/legacy_redirects.rb` | Redirects from the old `/lucabrodohshl/...` URLs |
| `assets/css/main.css` | The only stylesheet |
| `assets/js/copy-citation.js` | The only script (BibTeX copy button; pages work without it) |

## Run and build locally

Requires Ruby ≥ 3.1 (macOS: `brew install ruby`, then put `/opt/homebrew/opt/ruby/bin` on `PATH`).

```bash
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve            # http://localhost:4000/
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py       # links, sitemap, metadata, JSON-LD checks
```

## Deployment

Every push to `main` runs [`.github/workflows/pages.yml`](.github/workflows/pages.yml). It builds the site with the Pages base path, runs `scripts/check_site.py` and deploys. **Settings → Pages → Source** must be **GitHub Actions**.

### Moving to the root URL (one-time)

The site used to be a *project site* at `https://lucabrodohshl.github.io/lucabrodohshl/`. GitHub serves a site at the domain root only from a repository named exactly `<username>.github.io`, so changing `baseurl` alone is not enough:

1. On GitHub, open the repository → **Settings → General**. Under **Repository name**, enter `lucabrodohshl.github.io` and click **Rename**.
2. Open **Settings → Pages** and check that **Source** is still **GitHub Actions**.
3. Open **Actions → Build and deploy site to GitHub Pages → Run workflow** (or push any commit). The site is then published at `https://lucabrodohshl.github.io/`.
4. Point your local clone at the new name (GitHub also redirects the old one):
   `git remote set-url origin https://github.com/lucabrodohshl/lucabrodohshl.github.io.git`

Note: a repository named exactly `lucabrodohshl` is GitHub's special *profile README* repository. After the rename your profile no longer shows a README from it; create a new `lucabrodohshl` repository with a `README.md` if you want one.

**Old URLs.** After the rename, GitHub no longer serves `/lucabrodohshl/...` on its own. [`_plugins/legacy_redirects.rb`](_plugins/legacy_redirects.rb) therefore generates `/lucabrodohshl/<path>/` for every page and paper. Each one has an immediate redirect and a canonical link to the new URL, and is marked `noindex`; search engines treat these as permanent redirects. The old PDF URLs (`/lucabrodohshl/publications/<slug>/<file>.pdf`) are not redirected, because a static host cannot redirect a PDF; the paper pages that link to them are. A copy of the Google verification file is kept at `/lucabrodohshl/google48875e0f9175e1b8.html`, so the old Search Console property stays verified.

## Adding or editing a publication

Each paper is one Markdown file in [`_publications/`](_publications/). The file name is the slug and the URL (`/publications/<slug>/`). Adding a file creates all of the following:

- its entry on the publications page, on the Research page (by `research_area`), and on the home page if `featured`
- its own paper page
- `<title>`, meta description, canonical link and Open Graph tags
- Google Scholar `citation_*` tags and `ScholarlyArticle` / `BreadcrumbList` JSON-LD
- the BibTeX box with its Copy button
- related-paper links
- a sitemap entry and an `llms.txt` entry

Front-matter fields (copy an existing file as a template):

| Field | Purpose |
|---|---|
| `title`, `authors`, `date` | Exact title, author list, and the date used for sorting and `citation_publication_date` |
| `date_note` | Optional explanation of what the date means |
| `venue`, `venue_detail`, `venue_short` | Full venue line on the paper page, and the short venue in publication lists |
| `venue_type` | `journal`, `conference`, `preprint` or `other`; controls `citation_journal_title` / `citation_conference_title` |
| `citation_venue`, `publisher`, `volume`, `issue`, `firstpage`, `lastpage` | Scholar metadata (only emitted if present) |
| `status`, `status_note` | `Published`, `Accepted`, `Preprint`, … shown in lists (when not Published) and on the page |
| `award` | Shown in dark red next to the venue (e.g. `award: "Best Paper Award"`) |
| `doi` | Publisher DOI (without `https://doi.org/`) |
| `zenodo`, `zenodo_doi` | Zenodo record URL and DOI |
| `pdf`, `pdf_note` | Site path of the local PDF; omit the field if no PDF may be shared |
| `code`, `code_label` | Optional code/artifact link (currently unused) |
| `license`, `license_label` | License of the shared version |
| `featured`, `featured_order` | Show under "Selected publications" (home page and top of publications page), in this order |
| `research_area` | `id` of a research direction in `_data/research.yml`; the paper is listed under it on the Research page |
| `topics` | Short labels (kept as data; not displayed) |
| `keywords` | Paper keywords (page, `citation_keywords`, JSON-LD) |
| `description` | Meta description, roughly 50–160 characters, specific to the paper |
| `summary_short` | One- or two-sentence description in publication lists |
| `abstract` | Complete author-written abstract |
| `bibtex` | Citation shown in the copy box |
| `cite_note` | Optional note above the BibTeX |
| `related` | Explicit list of related paper slugs; unknown slugs are silently skipped |
| body (Markdown) | Detailed original summary: research question, approach, results, relevance |

**PDFs.** Put the PDF in `publications/<slug>/`, next to the paper page, and set `pdf: /publications/<slug>/<file>.pdf`. Google Scholar expects the PDF in the same directory as the HTML abstract page. The supplied originals stay unchanged in `assets/paper/`; that folder is excluded from the build so each PDF has a single public URL.

**Selected publications** are currently RTWBS (MEMOCODE 2026, Best Paper Award), the FSE 2026 LTL paper and the SEAMS 2026 paper.

## Research page

[`_data/research.yml`](_data/research.yml) holds the three research directions. `summary` appears on the home page, and `body` (one or more paragraphs) on the Research page, followed by every paper whose `research_area` matches the direction's `id`.

## Teaching page

Each item is one Markdown file in [`_teaching/`](_teaching/). Items are grouped by `course` and listed newest first. The file has only front matter:

| Field | Purpose |
|---|---|
| `course` | Group heading (course name, or e.g. `Templates`) |
| `title`, `type`, `description` | Entry title, kind of material (`Lecture slides`, `Exercise sheet`, `Templates`, …) and a short description |
| `file`, `format`, `size` | For a downloadable file: its site path (put files in `assets/teaching/`), format (`PDF`) and optional size. The page shows "<download_label> (<format>)" and "Open in browser" |
| `download_label` | Link text before the format, e.g. `Download slides` |
| `link`, `link_label` | For an external resource instead of a file: its URL and link text |
| `released` | Optional date (`YYYY-MM-DD`), shown as month and year |

Currently listed: the Team Henkler LaTeX and PowerPoint templates (GitHub repository).

## Content sources and open items

Metadata was taken from the supplied PDFs and checked against Crossref (DOIs, pages, CC BY 4.0 licences), Zenodo records and ORCID `0009-0005-1437-9861`.

| Paper | PDF on site | Notes |
|---|---|---|
| FSE 2026, Property Refinement in LTL | yes (`FSELTL.pdf`) | DOI 10.1145/3808127 |
| ICSE 2026 Companion, What Do We Really Need? | yes (`PropRef.pdf`) | DOI 10.1145/3774748.3795661 |
| CAIESA 2026, Property Refinement in CTL | yes (`CTlRef.pdf`) | IFIP AICT (Springer), Barcelona; cited with the Zenodo DOI 10.5281/zenodo.22734609 (as given by Luca). Add the Springer DOI and page numbers when available |
| MEMOCODE 2026, Asymmetric Timed Refinement (RWTBS) | yes (`RTWBS.pdf`) | Best Paper Award (confirmed by Luca). **Add the proceedings DOI and update the BibTeX when available**; currently cites the Zenodo record 10.5281/zenodo.22746507 |
| SEAMS 2026, Runtime Self-Optimization | yes (`RTOPT.pdf`) | DOI 10.1145/3788550.3794861 |
| MODELS 2026 Companion, Social norm pattern catalog | yes (`norms.pdf`) | DOI 10.1145/3837062.3838903 |
| ASYDE 2026, Correct-by-Construction Evolution of Digital Twins | **missing** | Found via ORCID/Crossref; CC BY 4.0. Add an author PDF to `publications/digital-twin-evolution-asyde-2026/` and set `pdf:` |
| MoVe4SPS 2025, Digital Twin Framework for Transportation | **missing** | Found via ORCID/Crossref; licence not stated in Crossref. Add a PDF only if sharing is permitted |

The summaries for the last two papers are based on their published abstracts only.

Three supplied PDFs (`RTOPT.pdf`, `RTWBS.pdf`, `norms.pdf`) embed Type 3 fonts (DejaVu, from matplotlib figures). Body text extracts fine, but Google Scholar recommends avoiding Type 3 fonts. When regenerating the figures, set `matplotlib.rcParams["pdf.fonttype"] = 42`.

## Impressum checklist

The Impressum at `/impressum/` uses the details Luca provided:

- [x] Name: Luca Brodo
- [x] Address: Hochschule Hamm-Lippstadt, Campus Lippstadt, Dr.-Arnold-Hueck-Straße 3, 59557 Lippstadt, Deutschland
- [x] E-mail: luca.brodo@hshl.de
- [ ] Have the Impressum reviewed and confirm that using the institutional address is acceptable (the page has not been legally reviewed).
- [ ] Decide whether a separate privacy notice (*Datenschutzerklärung*) is needed. GitHub Pages processes visitor IP addresses in server logs; the site itself sets no cookies and loads no third-party resources.

## Search engines, Google Scholar and AI crawlers

What the site already does:

- One static HTML page per paper, with the exact title as `<h1>`, the full abstract, authors and keywords as visible text
- A unique title and description on every page
- A canonical URL, Open Graph tags and Scholar `citation_*` tags, with the PDF in the same directory as the paper page
- JSON-LD: `ProfilePage`/`Person`/`WebSite` on the home page; `ScholarlyArticle` and `BreadcrumbList` on paper pages
- A sitemap and a permissive robots policy
- No JavaScript needed for content or navigation, no tracking, and system fonts only

Indexing, ranking and appearance in AI answers are not guaranteed.

**robots.txt.** Crawlers read `https://lucabrodohshl.github.io/robots.txt` at the host root, so once the repository is the user site, [`robots.txt`](robots.txt) is in effect. The redirect pages under `/lucabrodohshl/` are deliberately not blocked.

The current policy allows all search engines and all AI search, user-fetch and training crawlers, including OpenAI's `OAI-SearchBot` (search), `GPTBot` (training) and `ChatGPT-User`. This is deliberate, for broad discoverability. To opt out of AI training only, add `Disallow: /` groups for `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended` and `CCBot`.

`llms.txt` is a small optional index. The HTML pages and the sitemap are what matter.

### Next steps after the move to the root URL

1. **Google Search Console.** Add a new *URL-prefix* property for `https://lucabrodohshl.github.io/`. It verifies with the meta tag (`google_site_verification` in `_config.yml`) or the file `google48875e0f9175e1b8.html` at the root; both are already deployed. Submit `sitemap.xml` and request indexing for the home, research, publications and teaching pages. Keep the old `/lucabrodohshl/` property to watch the redirects being processed.
2. **Bing Webmaster Tools.** Add `https://lucabrodohshl.github.io/` (meta tag `bing_site_verification`, or `BingSiteAuth.xml` at the root, which now works) and submit the sitemap. Bing's index also serves DuckDuckGo, Ecosia, Qwant and Yahoo, and is used by ChatGPT search and Copilot.
3. **Google Scholar profile.** Create or claim a Scholar profile, add the papers, and set the homepage to the site. Scholar has no submission form: it finds pages that follow its inclusion guidelines, usually within a few weeks.
4. **Link the site from your profiles.** Add the URL to ORCID (*Websites & social links*), your GitHub profile, LinkedIn, the HSHL staff page, Semantic Scholar and DBLP author pages, and the email signature. Links from these established pages are the strongest discovery signal.
5. **Keep it current.** Update the RWTBS entry when its proceedings DOI is known.
