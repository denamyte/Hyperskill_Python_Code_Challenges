from typing import List


def search(numbers: List[str], target: str) -> int:
    for index in range(len(numbers) - 1, -1, -1):
        if numbers[index] == target:
            return index
    return -1


print(search(input().split(), input()))
