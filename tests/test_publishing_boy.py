#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `publishing_boy` package."""
import os
import pytest

from publishing_boy import publishing_boy


TEST_FILE = 'test.md'
TEST_FOLDER = 'test_folder'
TEST_OUTPUT_FILE = 'test_output/test.md'


def test_running():
    """Test working on a test folder"""
    publishing_boy.process(TEST_FOLDER)

    assert os.path.exists(TEST_OUTPUT_FILE)

    with open(TEST_OUTPUT_FILE, 'r') as f:
        content = f.read()

        assert content.find('Title:')
        assert content.find('Date:')
        assert content.find('Modified:')
        assert content.find('Category:')
        assert content.find('Tags:')
        assert content.find('Authors:')

        assert content.find('This is a test content')


def test_command_line_folders():
    """Go to cookiecutter download folder, and
    extract the contents with cli testing.

    Test different types of input folders
    """
    pass
