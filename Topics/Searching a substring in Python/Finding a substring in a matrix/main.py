from typing import List


def input_matrix() -> List[str]:
    return [input() for _ in range(int(input().split(' ')[0]))]


def contains(text: List[str], pattern: List[str]) -> bool:
    for i in range(len(text) - len(pattern) + 1):
        ind = text[i].find(pattern[0])
        if ind > -1:
            found = True
            for j in range(1, len(pattern)):
                if ind != text[i + j].find(pattern[j], ind):
                    found = False
                    break
            if found:
                return True
    return False


ar1, ar2 = input_matrix(), input_matrix()
print(contains(ar1, ar2))
