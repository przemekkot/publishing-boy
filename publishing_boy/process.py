import glob
import os


def build_tuple(filepath, fullpath):
    filename = os.path.basename(filepath)

    content = ''
    with open(fullpath, 'r') as f:
        content = f.read()

    return filename, filepath, fullpath, content


def file_tuples(folder):
    """Generate file tuples from files in folder"""
    folder = os.path.join(folder, '**/*.md')
    results = glob.glob(folder, recursive=True)
    for fullpath in results:
        filepath = fullpath.split(folder)[1]  # substract folder
        yield build_tuple(filepath, fullpath)


def save_content(obj):
    return obj
