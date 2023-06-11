import math

b, b_a, c_a = 7, 35, 105
c = b * math.sin(math.radians(c_a)) / math.sin(math.radians(b_a))
print(round(c, 1))
