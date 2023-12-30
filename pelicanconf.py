import os

AUTHOR = 'Paul Hummer'
SITENAME = 'Help computer'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

THEME = os.path.join(os.path.dirname(__file__), 'theme')
DISABLE_SEARCH = True
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

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
    #('twitter', 'https://twitter.com/rockstar_'),
    ('github', 'https://github.com/rockstar'),
    ('facebook', 'https://facebook.com/paulhummer'),
    ('fa-brands fa-mastodon', 'https://mastodon.social/@iamtherockstar'),
    )

DEFAULT_PAGINATION = 3
DEFAULT_METADATA = {
    'status': 'hidden',
}

PLUGINS = ['pelican.plugins.figures']

GOODREADS_ACTIVITY_FEED = "https://www.goodreads.com/user/updates_rss/3283314"
GOODREADS_CURRENTLY_READING_FEED = "https://www.goodreads.com/review/list_rss/3283314?key=ciITNG4_sutJ2W5c3IRsR9Da63bhHGvRbwhkTEjAhZa8fW76&shelf=currently-reading"
