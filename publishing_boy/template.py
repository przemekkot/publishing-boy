TEMPLATE = """
Title: {title}
Date: {date}
Modified: {modified}
Category: {categories}
Tags: {tags}
Authors: {author}

{content}
"""


def render(context):
    return TEMPLATE.format(**context)
