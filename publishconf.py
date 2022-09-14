import os
import sys
from pelicanconf import *

sys.path.append(os.curdir)

SITEURL = "https://rossfenning.co.uk"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = True

# GOOGLE_ANALYTICS = ""
