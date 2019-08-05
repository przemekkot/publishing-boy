from datetime import datetime, timedelta
import os
from publishing_boy import config
from django.core.files.base import File, ContentFile
from publishing_boy.tests.utils import get_storage
from publishing_boy.plugins import title_extractior, creation_date, modified_date, category_extract, authors

temp_dir, storage = get_storage()
filename, path = 'test_file.md', 'test_file.md'
content = """
You have to do it Nicky. In order to do that, it’s important to have both overlapping and complementary skills on your team: A good rule of thumb is that any task should have at least two people who can do it, and any two people should have a number of significant tasks where one would obviously be better suited to work on it than another. The former is much more important than the latter, but both are important."""

storage.save(filename, ContentFile(content))

obj = (filename,
       filename,
       os.path.abspath(storage.path(filename)),
       content,)


def test_title_extractor():
    """Test title_extractor"""
    f2 = ('', 'file.c', '', 'A b c d',)
    f3 = ('', 'a/b/c/file.c', '', '',)

    label, r1 = title_extractior(obj)
    _, r2 = title_extractior(f2)
    _, r3 = title_extractior(f3)

    assert label == 'title'
    assert r1 == 'You have to do it Nicky'
    assert r2 == 'A b c d ...'
    assert r3 == ''


def test_creation_date():
    """Test for creation_date"""
    ctime = storage.get_created_time(filename)
    label, result_ctime = creation_date(obj)

    assert label == 'cdate'
    assert ctime == result_ctime
    assert datetime.now() - result_ctime < timedelta(seconds=2)


def test_modified_date():
    """Test getting the modification date"""
    storage.save('test.file', ContentFile('custom contents'))

    mtime = storage.get_modified_time(filename)
    label, result_mtime = modified_date(obj)

    assert label == 'mdate'
    assert mtime == result_mtime

    assert datetime.now() - result_mtime < timedelta(seconds=2)


def test_category_extract():
    """Test category extract"""

    f1 = ('', 'file.c', '', '',)
    f2 = ('', 'a/b/c/file.c', '', '',)
    f3 = ('', '/file.c', '', '',)

    label, r1 = category_extract(f1)
    _, r2 = category_extract(f2)
    _, r3 = category_extract(f3)

    assert label == 'categories'
    assert r1 == ''
    assert r2 == 'A, B, C'
    assert r3 == ''


def test_authors():
    def _author():
        return config['Posts'].get('author', '')

    label, author = authors(obj)

    assert label == 'authors'
    assert author == _author()
