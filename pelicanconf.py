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

THEME = './pelican-bootstrap3'

GOOGLE_AD_CLIENT = 'pub-7863038150136152'
GOOGLE_AD_SLOT = '2849293582'
GOOGLE_AD_WIDTH = 160
GOOGLE_AD_HEIGHT = 600

STATIC_PATHS = ['images', 'extra/CNAME', 'papers']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
