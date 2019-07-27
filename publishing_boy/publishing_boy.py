# -*- coding: utf-8 -*-
from publishing_boy.process import (
    file_tuples,
    save_content,
)
"""Main module."""


def process(folder):
    """Process files in folder."""
    for obj in file_tuples(folder):
        save_content(transform(obj))

    pass
