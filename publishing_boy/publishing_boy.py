# -*- coding: utf-8 -*-
from publishing_boy.transformation import PLUGINS
from publishing_boy.template import render
from publishing_boy.process import (
    create_content_folder,
    file_tuples,
    save_content,
)

from publishing_boy.plugins import (
    authors,
    title_extractior,
    creation_date,
    modified_date,
    category_extract,
    content_function,
)

"""Main module."""


def transform(obj):
    """This function has to take the object
    and then transform it using plugin functions.

    the output is the object with replaced content
    that suits pelican static site generator.
    """
    name , filepath, fullpath, _ = obj
    context = {key: value for key, value in (plugin(obj) for plugin in PLUGINS)}

    return name, filepath, fullpath, render(context)


def process(folder):
    """Process files in a given folder.

    Create data tuples from files and their contents.
    Pass each tuple thorough transformation function,
    and save it into the  content/ folder.

    """
    for obj in file_tuples(folder):
        print(obj)
        save_content(transform(obj))
