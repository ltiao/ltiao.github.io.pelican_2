#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Louis Tiao'
SITENAME = u'Louis Tiao'
SITEURL = ''

# SITESUBTITLE = '(Computer Scientist) &and; (Software Engineer)'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', '#'),
		  ('Linkedin', '#'),
          ('Facebook', '#'),
          ('Instagram', '#'),
          ('Github', '#'),)

DEFAULT_PAGINATION = 5

GOOGLE_ANALYTICS = 'UA-43722566-1'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
# PLUGINS = ['twitter_bootstrap_rst_directives']

THEME = 'themes/tiao-pelican-bootstrap3'
BOOTSTRAP_USE_CDN = True
BOOTSTRAP_THEME = 'yeti'

# BOOTSTRAP_FLAT = True