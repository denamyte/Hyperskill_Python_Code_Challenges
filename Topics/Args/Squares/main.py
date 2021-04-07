from functools import reduce


def sq_sum(*args):
    return reduce(lambda acc, x: acc + x * x, args, 0)
