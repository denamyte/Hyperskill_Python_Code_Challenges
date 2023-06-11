def choose_median(lst, start, middle, end):
    a, b, c = lst[start], lst[middle], lst[end]
    return start if b <= a <= c or c <= a <= b else \
        middle if a <= b <= c or c <= b <= a else \
        end


def partition(lst, pivot, start, end):
    swap(lst, start, pivot)
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            swap(lst, i, j)

    swap(lst, start, j)
    return j


def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def test():
    ar = [int(x) for x in input().split(' ')]
    ar_l = len(ar)
    mid = ar_l // 2 - (0 if (ar_l & 1) else 1)
    p = choose_median(ar, 0, mid, ar_l - 1)
    print(p)
    partition(ar, p, 0, ar_l - 1)
    print(' '.join(map(str, ar)))


test()
