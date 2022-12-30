import os

AUTHOR = 'Paul Hummer'
SITENAME = 'Help computer'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

THEME = os.path.join(os.path.dirname(__file__), 'theme')
DISABLE_SEARCH = True
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/rockstar_'),
    ('github', 'https://github.com/rockstar'),
    ('facebook', 'https://facebook.com/paulhummer'),
    ('fa-brands fa-mastodon', 'https://mastodon.social/@iamtherockstar'),
    )

DEFAULT_PAGINATION = 3
DEFAULT_METADATA = {
    'status': 'hidden',
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGINS = [
    'pelican.plugins.figures'
    ]