from typing import List


def filter_target(arr: List[str], target: str) -> str:
    res = [str(k) for k, v in enumerate(arr) if v == target]
    return ' '.join(res) if res else 'not found'


print(filter_target(input().split(), input()))
