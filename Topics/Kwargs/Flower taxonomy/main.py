iris = {}
names = ('species', 'petal_length', 'petal_width')


def add_iris(*args, **kwargs):
    iris[args[0]] = {**dict(zip(names, args[1:])),
                     **kwargs}
