class RightTriangle:
    @staticmethod
    def is_right(hyp: int, leg_1: int, leg_2: int):
        return hyp ** 2 == leg_1 ** 2 + leg_2 ** 2

    def __init__(self, hyp: int, leg_1: int, leg_2: int):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        self.area = leg_1 * leg_2 / 2


# triangle from the input
inp = [int(x) for x in input().split()]

print('Not right' if not RightTriangle.is_right(*inp) else f'{round(RightTriangle(*inp).area, 1)}')
