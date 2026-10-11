# Luca Brodo — academic website

Static Jekyll site deployed to GitHub Pages with GitHub Actions.

- Project-site URL: **https://lucabrodohshl.github.io/lucabrodohshl/**
- `url` and `baseurl` are set in [`_config.yml`](_config.yml) and drive canonical links, Open Graph, `citation_pdf_url`, JSON-LD and the sitemap.

## Run and build locally

Requires Ruby ≥ 3.1 (macOS: `brew install ruby`, then put `/opt/homebrew/opt/ruby/bin` on `PATH`).

```bash
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve            # http://localhost:4000/lucabrodohshl/
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py       # links, sitemap, metadata, JSON-LD checks
```

## Deployment (one-time setup)

1. On GitHub, open **Settings → Pages** for `lucabrodohshl/lucabrodohshl` and set **Source** to **GitHub Actions**.
2. Every push to `main` runs [`.github/workflows/pages.yml`](.github/workflows/pages.yml). It builds the site, runs `scripts/check_site.py` and deploys.

## Adding or editing a publication

Each paper is one Markdown file in [`_publications/`](_publications/). The file name is the slug and the URL (`/publications/<slug>/`). Adding a file creates all of the following:

- its card on the publications page, and on the home page if `featured`
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
| `venue`, `venue_detail`, `venue_short` | Full venue line on the paper page, and the short subtitle on cards |
| `venue_type` | `journal`, `conference`, `preprint` or `other`; controls `citation_journal_title` / `citation_conference_title` |
| `citation_venue`, `publisher`, `volume`, `issue`, `firstpage`, `lastpage` | Scholar metadata (only emitted if present) |
| `status`, `status_note` | `Published`, `Accepted`, `Preprint`, … shown on the card (when not Published) and on the page |
| `award`, `award_short` | Shown in **red** next to the venue (e.g. `award: "Best Paper Award"`) |
| `doi` | Publisher DOI (without `https://doi.org/`) |
| `zenodo`, `zenodo_doi` | Zenodo record URL and DOI |
| `pdf`, `pdf_note` | Site path of the local PDF; omit the field if no PDF may be shared |
| `code`, `code_label` | Optional code/artifact link (currently unused) |
| `license`, `license_label` | License of the shared version |
| `featured`, `featured_order` | Show under "Selected publications" (home page and top of publications page), in this order |
| `topics` | 1–3 small labels for the card (use sparingly) |
| `keywords` | Paper keywords (page, `citation_keywords`, JSON-LD) |
| `description` | Meta description, roughly 50–160 characters, specific to the paper |
| `summary_short` | One- or two-sentence card text |
| `abstract` | Complete author-written abstract |
| `bibtex` | Citation shown in the copy box |
| `cite_note` | Optional note above the BibTeX |
| `related` | Explicit list of related paper slugs; unknown slugs are silently skipped |
| body (Markdown) | Detailed original summary: research question, approach, results, relevance |

**PDFs.** Put the PDF in `publications/<slug>/`, next to the paper page, and set `pdf: /publications/<slug>/<file>.pdf`. Google Scholar expects the PDF in the same directory as the HTML abstract page. The supplied originals stay unchanged in `assets/paper/`; that folder is excluded from the build so each PDF has a single public URL.

**Selected publications** are currently RTWBS (MEMOCODE 2026, Best Paper Award), the FSE 2026 LTL paper and the SEAMS 2026 paper.

## Content sources and open items

Metadata was taken from the supplied PDFs and checked against Crossref (DOIs, pages, CC BY 4.0 licences), Zenodo records and ORCID `0009-0005-1437-9861`.

| Paper | PDF on site | Notes |
|---|---|---|
| FSE 2026, Property Refinement in LTL | yes (`FSELTL.pdf`) | DOI 10.1145/3808127 |
| ICSE 2026 Companion, What Do We Really Need? | yes (`PropRef.pdf`) | DOI 10.1145/3774748.3795661 |
| Property Refinement in CTL | yes (`CTlRef.pdf`) | Conference paper published on Zenodo, 10.5281/zenodo.22734610; add the conference name to `venue` if it should be shown |
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

**robots.txt and the project-site path.** Crawlers only read `https://lucabrodohshl.github.io/robots.txt`, at the host root. This repository publishes its file at `/lucabrodohshl/robots.txt`, which is informational only. Today the root returns 404, which crawlers treat as "everything allowed", so nothing is blocked. For full control, use one of these:

- Rename this repository to `lucabrodohshl.github.io`, then set `baseurl: ""` in `_config.yml`.
- Add a custom domain, then update `url` and set `baseurl: ""`.

The current policy allows all search engines and all AI search, user-fetch and training crawlers, including OpenAI's `OAI-SearchBot` (search), `GPTBot` (training) and `ChatGPT-User`. This is deliberate, for broad discoverability. To opt out of AI training only, add `Disallow: /` groups for `GPTBot`, `ClaudeBot`, `Google-Extended`, `Applebot-Extended` and `CCBot`.

`llms.txt` is a small optional index. The HTML pages and the sitemap are what matter.

### Next steps after the first deployment

1. **Google Search Console.** Add a *URL-prefix* property for `https://lucabrodohshl.github.io/lucabrodohshl/`. Verify it with the HTML tag method by pasting the token into `google_site_verification` in `_config.yml` and pushing. Then submit `sitemap.xml` and use *URL Inspection → Request indexing* for the home page and each paper page.
2. **Bing Webmaster Tools.** Import from Search Console, or verify with `bing_site_verification`, and submit the sitemap. Bing's index also serves DuckDuckGo and is used by ChatGPT search and Copilot.
3. **Google Scholar profile.** Create or claim a Scholar profile, add the papers, and set the homepage to the site. Scholar has no submission form: it finds pages that follow its inclusion guidelines, usually within a few weeks.
4. **Link the site from your profiles.** Add the URL to ORCID (*Websites & social links*), your GitHub profile, LinkedIn, the HSHL staff page, Semantic Scholar and DBLP author pages, and the email signature. Links from these established pages are the strongest discovery signal.
5. **Keep it current.** Update the RWTBS entry when its proceedings DOI is known.
