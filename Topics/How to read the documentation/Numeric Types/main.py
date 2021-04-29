import math


def some_calculate(a, b):
    print(int(math.fabs((a % b) - math.pow(b, a))))
