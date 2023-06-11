def kth(numbers, target, k, missed=0):
    i = -1 if target not in numbers else numbers.index(target)
    return -1 if i == -1 \
        else missed + i if k == 1 \
        else kth(numbers[i + 1:], target, k - 1, i + 1 + missed)


print(kth(input().split(), input(), int(input())))
