#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Roberto Izquierdo'
SITENAME = 'Roberto Izquierdo'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'pdfs']
THEME = 'theme'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'
DEFAULT_DATE_FORMAT = '%d %b %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Personal data
CONTACT = {
    'job': {
        'position': 'Data Scientist',
        'company': 'Telefonica I+D PHB team',
        'url': 'http://www.tid.es/es'
    },
    'social': {
        'github': 'http://github.com/robertoia',
        'linkedin': 'http://linkedin.com/in/robertoia'
    }
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
