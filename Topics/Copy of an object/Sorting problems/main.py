def check(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            return False
    return True


# where copying takes place
arr = [int(i) for i in input().split()]

if check(arr):
    print('sorted')
else:
    print('not sorted')