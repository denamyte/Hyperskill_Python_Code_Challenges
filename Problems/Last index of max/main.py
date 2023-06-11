from typing import List


def last_indexof_max(numbers: List[int]):
    max_i = 0
    for i in range(1, len(numbers)):
        if numbers[i] >= numbers[max_i]:
            max_i = i
    return max_i
