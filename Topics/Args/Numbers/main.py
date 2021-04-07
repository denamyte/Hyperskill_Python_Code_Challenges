from functools import reduce


def multiply(*ints):
    return reduce(lambda x, y: x * y, ints, 1)
