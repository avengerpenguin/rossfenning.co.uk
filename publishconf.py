#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://rossfenning.co.uk'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""


GOOGLE_AD_CLIENT = 'pub-7863038150136152'
GOOGLE_AD_SLOT = '2849293582'
GOOGLE_AD_WIDTH = 160
GOOGLE_AD_HEIGHT = 600

GOOGLE_ANALYTICS_ID = 'UA-786452-3'
