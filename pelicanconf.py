#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Diego Bruciaferri'
SITENAME = u'Diego Bruciaferri'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
SLUGIFY_SOURCE = 'basename'  # use the file name for slug


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PAGE_ORDER_BY = 'date'

# Blogroll
LINKS = (
         ('Researchgate', 'https://www.researchgate.net/profile/Diego_Bruciaferri'),
         ('POFC', 'https://www.plymouth.ac.uk/research/plymouth-ocean-forecasting-centre'),
)

# Social widget
SOCIAL = (
          ('github', 'https://github.com/oceandie/oceandie.github.io'),
          ('twitter', 'https://twitter.com/soundieg'),
          ('linkedin', 'https://www.linkedin.com/in/diego-bruciaferri-6300a194/'),
          ('Researchgate', 'https://www.researchgate.net/profile/Diego_Bruciaferri'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing

THEME = "../pelican-themes/pure"

COVER_IMG_URL = '/images/Research_Oceans.jpg'
TAGLINE = 'Physical oceanographer and ocean modeller.'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

MENUITEMS = [
    ('About', '/about.html'),
    ('Research', '/research.html'),
    ('Publications', '/publications.html'),
]
DISPLAY_PAGES_ON_MENU = True

