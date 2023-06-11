from typing import List, Tuple


def partition(lst: List[int], start: int, end: int) -> Tuple[int, int]:
    left_inc, right_ex = start, start + 1
    pivot = lst[start]
    i = start + 1
    while i <= end:
        if lst[i] > pivot:
            i += 1
        elif lst[i] < pivot:
            lst[left_inc], lst[i] = lst[i], lst[left_inc]
            left_inc += 1
        else:  # lst[i] == pivot
            lst[right_ex], lst[i] = lst[i], lst[right_ex]
            right_ex += 1
            i += 1
    return left_inc, right_ex - 1


lst_inp = list(map(int, input().split()))
left, right = partition(lst_inp, 0, len(lst_inp) - 1)
print(left, right)
print(*lst_inp)
