TEMPLATE = """
Title: {title}
Date: {cdate}
Modified: {mdate}
Category: {categories}
Authors: {authors}

{content}
"""


def render(context):
    """Use simple template render to generate content"""
    print(context)
    return TEMPLATE.format(**context)
