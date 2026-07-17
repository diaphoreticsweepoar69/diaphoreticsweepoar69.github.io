# Kay Wilkinson – Portfolio

Personal photography and illustration portfolio, styled from the [Duet](https://jekyllthemes.io/theme/duet-portfolio-jekyll-theme) theme and ready for GitHub Pages.

## Pages

| File | Purpose |
|------|---------|
| `index.html` | Home – featured work |
| `photography.html` | Photography gallery |
| `illustrations.html` | Illustrations gallery |
| `about.html` | About page |
| `contact.html` | Contact page (text only, no form) |
| `photography/*.html` | Photography detail pages |
| `illustrations/*.html` | Illustration detail pages |

Each gallery item links to a real HTML detail page (title, date, large image, write-up) — not a folder listing.

## Add a new photography piece

1. Put your image in `images/photography/` (e.g. `my-piece.jpg`).
2. Copy `photography/golden-hour.html` to `photography/my-piece.html` and update the title, date, image path, and write-up.
3. Add a portfolio card on `photography.html` and optionally `index.html`.

Same pattern under `illustrations/` for illustration pieces.

Or edit `_build_site.py` and run `python3 _build_site.py` to regenerate pages.

## Local preview

```bash
cd /path/to/portfolio-github-pages
python3 -m http.server 8000
```

Open http://localhost:8000

## GitHub Pages

1. Create a GitHub repository and push this project.
2. Settings → Pages → Deploy from branch `main` (root `/`).

## Customise

- Site name and tagline: edit `_build_site.py` (`SITE_NAME`, `SITE_TAGLINE`) and regenerate.
- About / Contact copy: `about.html`, `contact.html`.
- Replace placeholder SVGs in `images/` with your own photos and illustrations.
