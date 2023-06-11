def min_pos_search(ar, value):
    lo, hi = 0, len(ar) - 1,
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if ar[mid] <= value:
            hi = mid
        else:
            lo = mid + 1
    return hi if ar[hi] == value else -1


input_list = list(map(int, input().split()))
v = int(input())
print(min_pos_search(input_list, v))
