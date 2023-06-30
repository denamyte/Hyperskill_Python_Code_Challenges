from typing import List

from nltk import word_tokenize
import numpy as np
import pandas as pd


def make_dict(tokens: List[str]) -> List[str]:
    set_ = set()
    filtered = []
    for t in tokens:
        if t not in set_:
            filtered.append(t)
            set_.add(t)
    return filtered


def fill_mtx(tokens: List[str], dic: List[str]) -> np.ndarray:
    matrix = np.zeros([len(tokens), len(dic)], dtype=int)
    for i, t in enumerate(tokens):
        matrix[i, dic.index(t)] = 1
    return matrix


tokens = word_tokenize(input())
print(tokens)
dic = make_dict(tokens)
matrix = fill_mtx(tokens, dic)
print(matrix)
records = pd.DataFrame.from_records(matrix)
print(records)
print()
# for row in matrix:
#     # for num in row:
print('\n'.join(' '.join(f'{n}' for n in row) for row in matrix))
        # print(num, ' ', end='')
# print(records)
