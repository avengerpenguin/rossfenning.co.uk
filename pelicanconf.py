from voltaire.pelican import *

SITENAME = "Ross Fenning"
MENUITEMS_START = (
    ("Home", "/"),
    ("CV", "/cv"),
    ("Papers", "/papers"),
    ("Blog", "https://avengerpenguin.com/"),
)

PLUGINS += [
    "cv.pelican",
    "projects",
]

STATIC_PATHS = ["extra/cv.pdf", "extra/python.pdf", "papers"]
EXTRA_PATH_METADATA = {
    "extra/cv.pdf": {"path": "cv.pdf"},
    "extra/python.pdf": {"path": "python.pdf"},
}

TEMPLATE_PAGES = {
    "projects.html": "projects/index.html",
}
GITHUB_USER = "avengerpenguin"
THEME_TEMPLATES_OVERRIDES = ["theme/templates"]
