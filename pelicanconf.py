#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Ross Fenning'
SITENAME = u'Ross Fenning'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

DISQUS_SITENAME = u'rossfenning'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = './theme'

STATIC_PATHS = ['images', 'extra/CNAME', 'papers']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    }

PLUGINS = ['cv.cv', 'plugins.assets', 'plugins.sitemap', 'plugins.summary', 'plugins.post_stats']

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

MENUITEMS = (
    ('Home', '/'),
    ('CV', '/cv'),
    ('Papers', '/papers'),
    ('Blog', 'http://avengerpenguin.com/'),
)
