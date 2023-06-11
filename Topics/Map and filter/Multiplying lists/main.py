from operator import mul


def my_product(list_1, list_2):
    return list(map(mul, list_1, list_2))
