import builtins
import tempfile
import os
import unittest
FILENAME, FULLPATH, CONTENT = '', '', ''

class ProcessTest(unittest.TestCase):

    def setup(self):
        # generate tempfolder
        # add folder in there
        # add file in there
        # add content in that file
        # generate filepath for testing
        # generate fullpath for testing
        # folder = tempfile.mkdtemp()
        pass

    def teardown():
        # remove files and folders
        pass

    def test_build_tuple(monkeypatch):
        fulpath = '/home/red/a/b/c/1.md'
        fulpath = 'a/b/c/1.md'

        monkeypatch.setattr(builtins, open)


    def test_file_tuples():
        pass


    def test_save_content():
        pass
