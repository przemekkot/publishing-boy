

PLUGINS = []

def register_plugin(fn):
    def wrapps(*args, **kwargs):

    return wrapps


def transform(obj):
    name , filepath, fullpath, _ = obj
    context = {key: value for key, value in (plugin(obj) for plugin in plugins)}

    return name, filepath, fullpath, render(context)