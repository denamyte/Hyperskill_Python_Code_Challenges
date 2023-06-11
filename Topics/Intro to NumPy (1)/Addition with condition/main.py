import numpy as np

def custom_sum(a, b):
    return [
        lambda: np.add(a, b),
        lambda: 'One argument is a list',
        lambda: 'Both arguments are lists, not arrays',
    ][isinstance(a, list) + isinstance(b, list)]()
