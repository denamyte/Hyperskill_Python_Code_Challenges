from functools import reduce


def final_deposit_amount(*interest, amount=1000):
    return round(reduce(lambda x, y: x * (1 + y / 100), interest, amount), 2)
