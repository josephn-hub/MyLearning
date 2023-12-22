import functools

list_name = ['J', 'O', 'S', 'E', 'P', 'H']

name = functools.reduce(lambda x, y: x + y, list_name)
print(name)