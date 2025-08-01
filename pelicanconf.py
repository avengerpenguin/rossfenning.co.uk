from pathlib import Path

from voltaire.pelican import *  # noqa

SITENAME = "Ross Fenning"
MENUITEMS_START = (
    ("Home", "/"),
    ("CV", "/cv"),
    ("Papers", "/papers"),
    ("Blog", "https://avengerpenguin.com/"),
)

if "PLUGINS" not in globals():
    PLUGINS = []

PLUGINS += [
    "cv.pelican",
    # "projects",
]

STATIC_PATHS = ["extra/cv.pdf", "extra/cv.ttl", "papers", "../icon"]
EXTRA_PATH_METADATA = {
    "extra/cv.pdf": {"path": "cv.pdf"},
    "extra/cv.ttl": {"path": "cv.ttl"},
    "../icon/android-chrome-512x512.png": {"path": "android-chrome-512x512.png"},
    "../icon/android-chrome-192x192.png": {"path": "android-chrome-192x192.png"},
    "../icon/apple-touch-icon.png": {"path": "apple-touch-icon.png"},
    "../icon/favicon-16x16.png": {"path": "favicon-16x16.png"},
    "../icon/favicon-32x32.png": {"path": "favicon-32x32.png"},
    "../icon/mstile-150x150.png": {"path": "mstile-150x150.png"},
    "../icon/favicon.ico": {"path": "favicon.ico"},
    "../icon/safari-pinned-tab.svg": {"path": "safari-pinned-tab.svg"},
    "../icon/browserconfig.xml": {"path": "browserconfig.xml"},
    "../icon/site.webmanifest": {"path": "site.webmanifest"},
}

TEMPLATE_PAGES = {
    "projects.html": "projects/index.html",
}
GITHUB_USER = "avengerpenguin"
THEME_TEMPLATES_OVERRIDES = ["theme/templates"]


path: Path = Path.cwd() / "static" / "css" / "style.css"
LOCAL_SCSS = str(path)
