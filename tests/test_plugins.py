content = """
In order to do that, it’s important to have both overlapping and complementary skills on your team: A good rule of thumb is that any task should have at least two people who can do it, and any two people should have a number of significant tasks where one would obviously be better suited to work on it than another. The former is much more important than the latter, but both are important."""
obj = ('test_file.md', './test_file.md', '/test_file.md', content,)


def test_title_extractor():
    pass


def test_creation_date():
    # storage is django stuff
    self.assertEqual(ctime, datetime.fromtimestamp(os.path.getctime(self.storage.path(f_name))))

    pass


def test_modified_date():
        """
        File storage returns a datetime for the last modified time of a file.
        """
        self.assertFalse(self.storage.exists('test.file'))

        f = ContentFile('custom contents')
        f_name = self.storage.save('test.file', f)
        self.addCleanup(self.storage.delete, f_name)
        mtime = self.storage.get_modified_time(f_name)

        self.assertEqual(mtime, datetime.fromtimestamp(os.path.getmtime(self.storage.path(f_name))))
        self.assertLess(timezone.now() - self.storage.get_modified_time(f_name), timedelta(seconds=2))
    self.assertEqual(atime, datetime.fromtimestamp(os.path.getatime(self.storage.path(f_name))))
    pass
