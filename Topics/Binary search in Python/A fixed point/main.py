def is_fixed_point_bs(list_) -> bool:
    lo, hi = 0, len(list_)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if list_[mid] == mid:
            return True
        if list_[mid] < mid:
            lo = mid + 1
        else:
            hi = mid
    return False


print(is_fixed_point_bs(list(map(int, input().split()))))
