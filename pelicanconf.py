AUTHOR = 'Mark'
SITENAME = "Mark's Blog"
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

THEME = '/Users/bush/Developer/IdeaProjects/notmyidea-spatial'

DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

STATIC_PATHS = [
    "images"
    # , "js"
]
ARTICLE_URL = "{category}/{slug}.html"
ARTICLE_SAVE_AS = "{category}/{slug}.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    # ("Pelican", "https://getpelican.com/")
    # ,("Python.org", "https://www.python.org/")
    # ,("Jinja2", "https://palletsprojects.com/p/jinja/")
    # ,("You can modify those links in your config file", "#")
)

# Social widget
SOCIAL = (
    # ("You can add links in your config file", "#"),
    # ("Another social link", "#"),
    # ("GitHub", "https://github.com/markbush")
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
