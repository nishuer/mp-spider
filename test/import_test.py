import importlib


_source = importlib.import_module('app.source.%s_source' % 'sohu')
source = getattr(_source, 'history')

print(source[0])