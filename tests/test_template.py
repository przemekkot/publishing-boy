import datetime
from publishing_boy.template import render


TEMPLATE = """
Title: A b c
Date: 2019-01-01 01:00:00
Modified: 2019-01-01 01:00:00
Category: A, B, C
Authors: A. B

A b c. E f g. H i j.
"""

context = {
    'title': 'A b c',
    'cdate': datetime.datetime.strptime('2019-01-01 01:00:00'),
    'mdate': datetime.datetime.strptime('2019-01-01 01:00:00'),
    'category': 'A, B, C',
    'authors': 'A. B',
    'content': 'A b c. E f g. H i j.',
}


def test_render():
    assert TEMPLATE == render(context)
