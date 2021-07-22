def binary_count(target, left, right):
    count = 0
    while left <= right:
        middle = (left + right) // 2
        if middle == target:
            return count + 1
        elif target < middle:
            right = middle - 1
        else:
            left = middle + 1
        count += 1


x = int(input())
lx, rx = (int(n) for n in input().split())
print(binary_count(x, lx, rx))
