from copy import copy


def solve(obj):
    return id(obj) != id(copy(obj))
