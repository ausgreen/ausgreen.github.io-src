#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Austin Green'
SITENAME = 'Austin Green'
SITEURL = ''
FAVICON = '/images/favicon.ico'
PATH = 'content'

# STATIC_PATHS = ['images']

TIMEZONE = 'America/Regina'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = [('Home','/')]
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# Note, I added another variable to the theme so images could be used
# logo images are to be placed in 'themes/<theme>/static/img'
SOCIAL = [('GitHub', 'https://github.com/ausgreen', "github_32_light.png"),
          ('LinkedIn', 'https://www.linkedin.com/in/austin-green-b2aba16a/', "linked_in_28.png")]

DEFAULT_PAGINATION = False

THEME = "./themes/Flex"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
