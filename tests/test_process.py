from django.core.files.base import File, ContentFile
import os
import shutil
import unittest
from publishing_boy.tests.utils import get_storage
from publishing_boy.process import build_tuple, file_tuples


class ProcessTest(unittest.TestCase):

    def setUp(self):
        """Prepare file tests"""
        self.filename = 'testing/test_post.md'
        self.content = 'This is my content.'
        temp_dir, storage = get_storage()
        self.temp_dir = temp_dir
        self.storage = storage
        self.storage.save(self.filename, ContentFile(self.content))

    def result_tuple(self):
        return (os.path.basename(self.filename),
                self.filename,
                os.path.abspath(self.storage.path(self.filename)),
                self.content,)

    def tearDown(self):
        """Remove temp dir"""
        shutil.rmtree(self.temp_dir)

    def test_setup(self):
        self.assertFalse(self.storage.exists('testing/second.md'))
        self.assertTrue(self.storage.exists(self.filename))

    def test_build_tuple(self):
        _, path, abspath, _ = self.result_tuple()
        result = build_tuple(path, abspath)

        assert result == self.result_tuple()

    def test_file_tuples(self):
        assert list(file_tuples(self.storage.path(''))) == [self.result_tuple()]

    def test_save_content(self):
        assert False
