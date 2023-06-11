ints = sorted(int(num) for num in input().split())
print(ints[-1], *ints[:-1])
