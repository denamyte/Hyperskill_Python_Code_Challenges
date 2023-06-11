from typing import Iterator


def count(numbers: Iterator[int], target: int) -> int:
    return sum(x == target for x in numbers)


print(count(map(int, input().split()), int(input())))
