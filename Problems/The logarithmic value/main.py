from math import log, e

a, b = (int(input()) for _ in range(2))
print(round(log(a, b if b > 1 else e), 2))
