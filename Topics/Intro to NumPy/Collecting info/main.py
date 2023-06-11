import numpy as np


def collect_info(a):
    return f'Shape: {a.shape}; ' \
           f'dimensions: {a.ndim}; ' \
           f'length: {len(a)}; ' \
           f'size: {a.size}'
