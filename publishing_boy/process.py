import glob
import os


def build_tuple(filepath, abspath):
    assert os.path.exists(abspath)

    filename = os.path.basename(filepath)

    content = ''

    with open(abspath, 'r') as f:
        content = f.read()

    return filename, filepath, abspath, content


def file_tuples(folder):
    """Generate file tuples from files in folder"""
    query = os.path.join(folder, '**/*.md')
    results = glob.glob(query, recursive=True)
    for abspath in results:
        filepath = str.lstrip(abspath.split(folder)[1], '/')  # substract folder
        yield build_tuple(filepath, abspath)


def save_content(obj):
    return obj


def create_content_folder(output_path):
    """Create in a folder current to running the software
    folder named 'content' that will keep the output."""
    pass
