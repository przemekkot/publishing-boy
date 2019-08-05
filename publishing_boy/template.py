TEMPLATE = """
Title: {title}
Date: {cdate}
Modified: {mdate}
Category: {categories}
Authors: {authors}

{content}
"""


def render(context):
    return TEMPLATE.format(**context)
