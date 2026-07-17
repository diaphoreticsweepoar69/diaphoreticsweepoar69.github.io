#!/usr/bin/env python3
"""Generate the static portfolio site pages from shared chrome."""

from pathlib import Path
from typing import Optional

ROOT = Path(__file__).resolve().parent
SITE_NAME = "Kay Wilkinson"
SITE_TAGLINE = "Photography & illustration"
YEAR = "2026"


def asset(depth: int, path: str) -> str:
    """Relative path to a root asset. depth=0 root pages, depth=1 detail pages."""
    if depth == 0 and path == "":
        return "index.html"
    prefix = "../" * depth
    return f"{prefix}{path}"


def nav(depth: int, active: str) -> str:
    links = [
        ("photography.html", "photography", "Photography"),
        ("illustrations.html", "illustrations", "Illustrations"),
        ("about.html", "about", "About"),
        ("contact.html", "contact", "Contact"),
    ]
    items = []
    for filename, slug, label in links:
        href = asset(depth, filename)
        cls = ' cc-active' if active == slug else ""
        items.append(
            f"""\t\t\t\t\t<li class="menu__list__item">
\t\t\t\t\t\t<a href="{href}" class="menu__list__item__link{cls}">{label}</a>
\t\t\t\t\t</li>
"""
        )
    return "\n".join(items)


def socials() -> str:
    return """\t\t<ul class="socials">
\t\t\t<li class="socials__item">
\t\t\t\t<a href="https://instagram.com" target="_blank" class="socials__item__link js-no-ajax" title="Instagram">
\t\t\t\t\t<i class="fab fa-instagram" aria-hidden="true"></i>
\t\t\t\t</a>
\t\t\t</li>
\t\t</ul>
"""


def page(
    *,
    title: str,
    description: str,
    depth: int,
    active: str,
    page_url: str,
    content: str,
    og_image: Optional[str] = None,
) -> str:
    home = asset(depth, "index.html")
    css = asset(depth, "css/style.css")
    favicon = asset(depth, "images/favicon.png")
    plugins = asset(depth, "js/plugins-min.js")
    duet = asset(depth, "js/duet-min.js")
    home_active = " cc-active" if active == "home" else ""
    image = og_image or asset(depth, "images/favicon.png")

    return f"""<!DOCTYPE html>
<html class="no-js" lang="en">
<head>
\t<meta charset="utf-8" />
\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

\t<link rel="shortcut icon" href="{favicon}" />
\t<title>{title}</title>
\t<meta name="description" content="{description}" />

\t<meta name="twitter:card" content="summary_large_image" />
\t<meta name="twitter:title" content="{title}" />
\t<meta name="twitter:description" content="{description}" />
\t<meta name="twitter:image:src" content="{image}" />

\t<meta property="og:title" content="{title}" />
\t<meta property="og:description" content="{description}" />
\t<meta property="og:image" content="{image}" />

\t<link href="https://fonts.googleapis.com/css?family=Muli:300,400,600,700" rel="stylesheet" />

\t<meta name="viewport" content="width=device-width, initial-scale=1" />
\t<link rel="stylesheet" href="{css}" />

\t<script defer src="https://use.fontawesome.com/releases/v5.1.1/js/solid.js" integrity="sha384-GXi56ipjsBwAe6v5X4xSrVNXGOmpdJYZEEh/0/GqJ3JTHsfDsF8v0YQvZCJYAiGu" crossorigin="anonymous"></script>
\t<script defer src="https://use.fontawesome.com/releases/v5.1.1/js/brands.js" integrity="sha384-0inRy4HkP0hJ038ZyfQ4vLl+F4POKbqnaUB6ewmU4dWP0ki8Q27A0VFiVRIpscvL" crossorigin="anonymous"></script>
\t<script defer src="https://use.fontawesome.com/releases/v5.1.1/js/fontawesome.js" integrity="sha384-NY6PHjYLP2f+gL3uaVfqUZImmw71ArL9+Roi9o+I4+RBqArA2CfW1sJ1wkABFfPe" crossorigin="anonymous"></script>
</head>

<body class="loading" data-site-url="." data-page-url="{page_url}">

\t<header class="header">
\t\t<div class="wrap">
\t\t\t<a href="{home}" class="header__title{home_active}">
\t\t\t\t{SITE_NAME}
\t\t\t</a>

\t\t\t<div class="menu">
\t\t\t\t<div class="menu__toggle js-menu-toggle">
\t\t\t\t\t<div class="menu__toggle__icon"><span></span></div>
\t\t\t\t</div>
\t\t\t\t<div class="menu__wrap">
\t\t\t\t\t<ul class="menu__list">
{nav(depth, active)}
\t\t\t\t\t</ul>
\t\t\t\t</div>
\t\t\t</div>
\t\t</div>
\t</header>

\t<div class="loader"><svg width="120" height="30" viewBox="0 0 120 30" xmlns="http://www.w3.org/2000/svg"><circle cx="15" cy="15" r="15"><animate attributeName="r" from="15" to="15" begin="0s" dur="0.8s" values="15;9;15" calcMode="linear" repeatCount="indefinite"/><animate attributeName="fill-opacity" from="1" to="1" begin="0s" dur="0.8s" values="1;.5;1" calcMode="linear" repeatCount="indefinite"/></circle><circle cx="60" cy="15" r="9" fill-opacity="0.3"><animate attributeName="r" from="9" to="9" begin="0s" dur="0.8s" values="9;15;9" calcMode="linear" repeatCount="indefinite"/><animate attributeName="fill-opacity" from="0.5" to="0.5" begin="0s" dur="0.8s" values=".5;1;.5" calcMode="linear" repeatCount="indefinite"/></circle><circle cx="105" cy="15" r="15"><animate attributeName="r" from="15" to="15" begin="0s" dur="0.8s" values="15;9;15" calcMode="linear" repeatCount="indefinite"/><animate attributeName="fill-opacity" from="1" to="1" begin="0s" dur="0.8s" values="1;.5;1" calcMode="linear" repeatCount="indefinite"/></circle></svg></div>

\t<div class="page-loader"></div>

\t<div class="page">
\t\t<div class="page__content" data-page-title="{title}">
{content}
\t\t</div>
\t</div>

\t<footer class="footer">
\t\t<div class="wrap">
\t\t\t<a href="{home}" class="footer__title{home_active}">
\t\t\t\t{SITE_NAME}
\t\t\t</a>
\t\t\t<p class="footer__text">{SITE_TAGLINE}</p>
\t\t\t<div class="footer__copyright">
\t\t\t\t<span>© {YEAR} {SITE_NAME}</span>
\t\t\t</div>
{socials()}
\t\t</div>
\t</footer>

\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
\t<script src="{plugins}"></script>
\t<script src="{duet}"></script>
</body>
</html>
"""


def portfolio_item(href: str, image: str, title: str, subtitle: str) -> str:
    return f"""\t\t<div class="portfolio-item">
\t\t\t<a class="portfolio-item__link" href="{href}">
\t\t\t\t<div class="portfolio-item__image">
\t\t\t\t\t<img src="{image}" alt="{title}" />
\t\t\t\t</div>
\t\t\t\t<div class="portfolio-item__content">
\t\t\t\t\t<div class="portfolio-item__info">
\t\t\t\t\t\t<h2 class="portfolio-item__title">{title}</h2>
\t\t\t\t\t\t<p class="portfolio-item__subtitle">{subtitle}</p>
\t\t\t\t\t</div>
\t\t\t\t</div>
\t\t\t</a>
\t\t</div>
"""


def write(rel: str, html: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print(f"Wrote {rel}")


def detail_content(title: str, date: str, image: str, alt: str, writeup: str) -> str:
    paragraphs = "\n".join(f"\t<p>{p}</p>" for p in writeup.strip().split("\n\n"))
    return f"""
<section class="intro">
\t<div class="wrap">
\t\t<h1>{title}</h1>
\t\t<p>{date}</p>
\t</div>
</section>

<section class="single">
\t<p><img src="{image}" alt="{alt}" /></p>
{paragraphs}
</section>
"""


# --- Home ---

home_content = f"""
<section class="intro">
\t<div class="wrap">
\t\t<h1>Photography and illustration.</h1>
\t\t<p>A selection of personal work across light, place, and drawn form.</p>
\t</div>
</section>

<section class="portfolio">
\t<div class="content-wrap portfolio-wrap">
{portfolio_item("photography/golden-hour.html", "images/photography/golden-hour.svg", "Golden Hour", "Photography")}
{portfolio_item("illustrations/ink-study.html", "images/illustrations/ink-study.svg", "Ink Study", "Illustration")}
{portfolio_item("photography/harbour-light.html", "images/photography/harbour-light.svg", "Harbour Light", "Photography")}
{portfolio_item("illustrations/colour-wash.html", "images/illustrations/colour-wash.svg", "Colour Wash", "Illustration")}
\t</div>
</section>
"""

write(
    "index.html",
    page(
        title=f"{SITE_NAME} – Portfolio",
        description=SITE_TAGLINE,
        depth=0,
        active="home",
        page_url="/index.html",
        content=home_content,
    ),
)

# --- Section galleries (same portfolio grid as home) ---

photo_listing = f"""
<section class="intro">
\t<div class="wrap">
\t\t<h1>Photography</h1>
\t\t<p>Places, light, and quiet moments.</p>
\t</div>
</section>

<section class="portfolio">
\t<div class="content-wrap portfolio-wrap">
{portfolio_item("photography/golden-hour.html", "images/photography/golden-hour.svg", "Golden Hour", "July 2026")}
{portfolio_item("photography/harbour-light.html", "images/photography/harbour-light.svg", "Harbour Light", "June 2026")}
\t</div>
</section>
"""

write(
    "photography.html",
    page(
        title=f"Photography – {SITE_NAME}",
        description="Photography by Kay Wilkinson.",
        depth=0,
        active="photography",
        page_url="/photography.html",
        content=photo_listing,
    ),
)

ill_listing = f"""
<section class="intro">
\t<div class="wrap">
\t\t<h1>Illustrations</h1>
\t\t<p>Drawn studies, washes, and works on paper.</p>
\t</div>
</section>

<section class="portfolio">
\t<div class="content-wrap portfolio-wrap">
{portfolio_item("illustrations/ink-study.html", "images/illustrations/ink-study.svg", "Ink Study", "July 2026")}
{portfolio_item("illustrations/colour-wash.html", "images/illustrations/colour-wash.svg", "Colour Wash", "May 2026")}
\t</div>
</section>
"""

write(
    "illustrations.html",
    page(
        title=f"Illustrations – {SITE_NAME}",
        description="Illustrations by Kay Wilkinson.",
        depth=0,
        active="illustrations",
        page_url="/illustrations.html",
        content=ill_listing,
    ),
)

# --- Detail pages ---

write(
    "photography/golden-hour.html",
    page(
        title=f"Golden Hour – {SITE_NAME}",
        description="Golden Hour — a photography piece.",
        depth=1,
        active="photography",
        page_url="/photography/golden-hour.html",
        content=detail_content(
            "Golden Hour",
            "12 July 2026",
            "../images/photography/golden-hour.svg",
            "Golden Hour",
            """Replace this passage with your write-up about the photograph — where it was taken, what drew you to the light, or anything you want the viewer to know.

You can add as many paragraphs as you like. Keep the image file in images/photography/ and update the src path if you rename it.""",
        ),
        og_image="../images/photography/golden-hour.svg",
    ),
)

write(
    "photography/harbour-light.html",
    page(
        title=f"Harbour Light – {SITE_NAME}",
        description="Harbour Light — a photography piece.",
        depth=1,
        active="photography",
        page_url="/photography/harbour-light.html",
        content=detail_content(
            "Harbour Light",
            "3 June 2026",
            "../images/photography/harbour-light.svg",
            "Harbour Light",
            """Replace this passage with your write-up about the photograph.

Describe the subject, the evening, or the feeling you wanted to hold onto.""",
        ),
        og_image="../images/photography/harbour-light.svg",
    ),
)

write(
    "illustrations/ink-study.html",
    page(
        title=f"Ink Study – {SITE_NAME}",
        description="Ink Study — an illustration piece.",
        depth=1,
        active="illustrations",
        page_url="/illustrations/ink-study.html",
        content=detail_content(
            "Ink Study",
            "8 July 2026",
            "../images/illustrations/ink-study.svg",
            "Ink Study",
            """Replace this passage with your write-up about the illustration — materials, process, or what the piece is exploring.

Keep the artwork file in images/illustrations/ and point the image src at it.""",
        ),
        og_image="../images/illustrations/ink-study.svg",
    ),
)

write(
    "illustrations/colour-wash.html",
    page(
        title=f"Colour Wash – {SITE_NAME}",
        description="Colour Wash — an illustration piece.",
        depth=1,
        active="illustrations",
        page_url="/illustrations/colour-wash.html",
        content=detail_content(
            "Colour Wash",
            "21 May 2026",
            "../images/illustrations/colour-wash.svg",
            "Colour Wash",
            """Replace this passage with your write-up about the illustration.

Mention medium, palette, or the idea behind the wash.""",
        ),
        og_image="../images/illustrations/colour-wash.svg",
    ),
)

about_content = """
<section class="intro">
\t<div class="wrap">
\t\t<h1>About</h1>
\t\t<p>A short introduction to who you are and the work you make.</p>
\t</div>
</section>

<section class="single">
\t<p>Replace this text with your about page. Say a little about yourself, where you are based, and what draws you to photography and illustration.</p>

\t<p>You can keep this page short — a few paragraphs is enough — and update it whenever your practice shifts.</p>
</section>
"""

write(
    "about.html",
    page(
        title=f"About – {SITE_NAME}",
        description="About Kay Wilkinson.",
        depth=0,
        active="about",
        page_url="/about.html",
        content=about_content,
    ),
)

contact_content = """
<section class="intro">
\t<div class="wrap">
\t\t<h1>Contact</h1>
\t\t<p>How to get in touch.</p>
\t</div>
</section>

<section class="single">
\t<p>Replace this passage with how you would like people to reach you. For example, you might share an email address, a note about commissions, or links to social profiles.</p>

\t<p>There is no contact form on this page yet — just this space for your own wording.</p>
</section>
"""

write(
    "contact.html",
    page(
        title=f"Contact – {SITE_NAME}",
        description="Contact Kay Wilkinson.",
        depth=0,
        active="contact",
        page_url="/contact.html",
        content=contact_content,
    ),
)

print("Done.")
