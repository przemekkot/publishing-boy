import os
"""Here are functions that serve the
role of plugins. Each function
accepts tuple object with:
- filename
- content
- path

Those functions are loaded to the program
by a decorator, during module loading.
Functions are stored inside a list.
"""


def title_extractior(obj):
    """Extract title from content.
    Use NTLK to do stuff with text.

    @return: 'title', generated_content"""
    pass
    return 'title', 'Some example title'


def creation_date(obj):
    """Extract date when the file was
    created.

    @return: 'date', date(YYYY-mm-dd HH:MM:SS)"""
    pass
    return 'date', '2019-07-01 01:00:00'


def modified_date(obj):
    """Extract date when the file was
    modified.

    @return: 'modified', date(YYYY-mm-dd HH:MM:SS)"""
    pass
    return 'date', '2019-07-01 01:01:00'


def category_extract(obj):
    """Extract category. Category are
    the folder names in path file.

    @return: 'category', 'String, Separated, by'
    """
    _, filepath, _, _ = obj
    return  os.path.dirname(filepath).split("/")


def authors(obj):
    """Return authors"""
    return 'authors', 'Przemek Kot' # TODO: use config file for that
