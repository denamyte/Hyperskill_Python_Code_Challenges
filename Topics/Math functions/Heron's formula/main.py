from functools import reduce
from operator import mul
from math import sqrt

sides = [int(input()) for _ in range(3)]
p = sum(sides) / 2
prod = p * reduce(mul, map(lambda side: p - side, sides))
print(sqrt(prod))
