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
SOCIAL = (
	('Github', 'https://github.com/ltiao', 'github'),
	('Linkedin', 'https://www.linkedin.com/in/ltiao', 'linkedin'),
	('Twitter', 'https://twitter.com/louistiao', 'twitter'),
	('Facebook', 'https://www.facebook.com/louis.tiao', 'facebook'),
	('Email', 'http://www.google.com/recaptcha/mailhide/d?k=01ZGES3iSWmUwr35sEbB8-VA==&c=PeD7vZlw1_DRu8fsayKDuVdVl_rtu18xfsGBgyvNXwc=', 'envelope')
)

# SOCIAL = [(a, b) for a, b, _ in SOCIAL]

DEFAULT_PAGINATION = 1

DISQUS_SITENAME = 'ltiao'

GOOGLE_ANALYTICS = 'UA-43722566-1'

GITHUB_URL = 'https://github.com/ltiao'

# MENUITEMS = [
# 	('Test', 'http://www.cse.unsw.edu.au/~ctia193'),
# 	('Something', 'http://www.reddit.com'),
# ]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
# PLUGINS = ['twitter_bootstrap_rst_directives']

THEME = 'themes/tiao-pelican-bootstrap3'
BOOTSTRAP_USE_CDN = True
BOOTSTRAP_THEME = 'yeti'
# BOOTSTRAP_USE_PAGER = True
BOOTSTRAP_FLAT = True