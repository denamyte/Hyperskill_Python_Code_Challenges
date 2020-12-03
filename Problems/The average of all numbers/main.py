from math import floor, ceil


def input_num(round_fun):
    return round_fun(int(input()) / 3) * 3


print((input_num(ceil) + input_num(floor)) / 2)
