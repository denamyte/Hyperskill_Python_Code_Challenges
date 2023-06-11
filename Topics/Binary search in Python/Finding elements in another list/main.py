class SearchLists:
    def __init__(self):
        self._targets, self._elements = [list(map(int, input().split())) for _ in range(2)]
        self.indexes = [self.binary_search(target) for target in self._targets]

    def binary_search(self, target):
        left, right = 0, len(self._elements) - 1

        while left <= right:
            middle = (left + right) // 2

            if self._elements[middle] == target:
                return middle
            elif target < self._elements[middle]:
                right = middle - 1
            else:
                left = middle + 1

        return -1


print(*SearchLists().indexes)
