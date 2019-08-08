# -*- coding: utf-8 -*-
from publishing_boy.process import (
    create_content_folder,
    file_tuples,
    save_content,
)
from publishing_boy.transformation import (
    transform,
)
"""Main module."""


def process(folder):
    """Process files in a given folder.

    Create data tuples from files and their contents.
    Pass each tuple thorough transformation function,
    and save it into the  content/ folder.

    """
    for obj in file_tuples(folder):
        save_content(transform(obj))
