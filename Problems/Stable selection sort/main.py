from typing import List


def stable_selection_sort(names: List[str]):
    length = len(names)
    for i in range(length - 1):
        index = i

        for j in range(i + 1, length):
            if len(names[j]) < len(names[index]):
                index = j

        if i != index:
            names.insert(i, names.pop(index))


ar = [input() for _ in range(int(input()))]
stable_selection_sort(ar)
print('\n'.join(ar))
