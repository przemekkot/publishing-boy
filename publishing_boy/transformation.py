from publishing_boy.template import render

PLUGINS = []


def register_plugin(fn):
    """This decorator add a function to PLUGINS
    list.

    Order of plugins is not important"""
    PLUGINS.append(fn)

    return fn


def transform(obj):
    """This function has to take the object
    and then transform it using plugin functions.

    the output is the object with replaced content
    that suits pelican static site generator.
    """
    name , filepath, fullpath, _ = obj
    context = {key: value for key, value in (plugin(obj) for plugin in PLUGINS)}

    return name, filepath, fullpath, render(context)
