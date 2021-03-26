import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p) -> float:
        sub = self - p
        return math.hypot(sub.x, sub.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
