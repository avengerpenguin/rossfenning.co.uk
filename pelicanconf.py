from voltaire.pelican import *


SITENAME = u'Ross Fenning'
MENUITEMS_START = (
    ('Home', '/'),
    ('CV', '/cv'),
    ('Papers', '/papers'),
    ('Blog', 'http://avengerpenguin.com/'),
)

PLUGINS += [
    'cv.pelican',
    'projects',
]

STATIC_PATHS = ["extra/CNAME", "extra/cv.pdf", "papers"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/cv.pdf": {"path": "cv.pdf"},
}

TEMPLATE_PAGES = {
    'projects.html': 'projects/index.html',
}
GITHUB_USER='avengerpenguin'
THEME_TEMPLATES_OVERRIDES = ['theme/templates']
