from typing import List


def search(ar: List[str], target: str, a: int, b: int) -> int:
    for i in range(a, b):
        if ar[i] == target:
            return i
    return -1


print(search(input().split(), input(), *map(int, input().split())))
