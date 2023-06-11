from typing import List


def input_nums() -> List[int]:
    return [int(s) for s in input().split()]


def range_sum(numbers: List[int], start, end):
    return sum(x for x in numbers if start <= x <= end)


print(range_sum(input_nums(), *input_nums()))
