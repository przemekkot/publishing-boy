import builtins
import tempfile
import os
import shutil
import unittest
from django.core.files.base import File, ContentFile
from django.core.files.storage import FileSystemStorage
import django.core.files.storage


from publishing_boy.process import build_tuple, file_tuples

# dummy django.conf.settings
class Settings():
    MEDIA_ROOT = os.path.dirname(os.path.abspath(__file__))
    MEDIA_URL = 'http://local/'
    FILE_UPLOAD_PERMISSIONS = 0o777
    FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o777

# switch settings
django.core.files.storage.settings = Settings()


class ProcessTest(unittest.TestCase):

    def setUp(self):
        """Prepare file tests"""
        self.filename = 'testing/test_post.md'
        self.content = 'This is my content.'
        self.temp_dir = tempfile.mkdtemp()

        self.storage = FileSystemStorage(location=self.temp_dir, base_url='/')
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
        assert True
