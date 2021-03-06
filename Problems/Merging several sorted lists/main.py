from typing import List


def multi_merge(lists: List[List[int]]) -> List[int]:
    total_len = sum(len(lst) for lst in lists)
    merged = []
    indices = [0] * len(lists)

    for _ in range(total_len):
        list_i = list_index_with_smallest_number(indices, lists)
        merged.append(lists[list_i][indices[list_i]])
        indices[list_i] += 1

    return merged


def list_index_with_smallest_number(indices: List[int], lists: List[List[int]]) -> int:
    smallest_value = None
    smallest_index = -1
    stop = len(indices)
    for i in range(stop):
        if indices[i] >= len(lists[i]):
            continue
        val = lists[i][indices[i]]
        if smallest_value is None or val < smallest_value:
            smallest_value = val
            smallest_index = i

    return smallest_index


input_lists = [[int(x) for x in input().split(' ')] for i in range(int(input()))]
merged_list = multi_merge(input_lists)
print(' '.join(map(str, merged_list)))
