ar = [int(x) for x in input().split(' ')]
ar = sorted(ar, reverse=True)
print(' '.join(map(str, ar)))
