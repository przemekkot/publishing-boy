PLUGINS = []


def register_plugin(fn):
    """This decorator add a function to PLUGINS
    list.

    Order of plugins is not important"""
    def wrapps(*args, **kwargs):


        return wrapps


def transform(obj):
    """This function has to take the object
    and then transform it using plugin functions.

    the output is the object with replaced content
    that suits pelican static site generator.
    """
    name , filepath, fullpath, _ = obj
    context = {key: value for key, value in (plugin(obj) for plugin in plugins)}

    return name, filepath, fullpath, render(context)
