def merge_sort(ar):
    ar_len = len(ar)
    half_range = 1
    while half_range < ar_len:
        left_i = 0
        right_i = min(ar_len, half_range * 2)
        while left_i + half_range < ar_len:
            merge(ar, left_i, left_i + half_range, right_i)
            left_i = right_i
            right_i = min(ar_len, right_i + half_range * 2)
        half_range *= 2


def merge(ar, left_i, mid_i, right_i):
    i = left_i
    j = mid_i
    m_ar = []

    while i < mid_i and j < right_i:
        if ar[i] > ar[j]:
            m_ar.append(ar[i])
            i += 1
        else:
            m_ar.append(ar[j])
            j += 1

    m_ar.extend(ar[i:mid_i])
    m_ar.extend(ar[j:right_i])
    ar[left_i:right_i] = m_ar


lst = [int(s) for s in input().split(' ')]
merge_sort(lst)
print(str(lst)[1:-1].replace(', ', ' '))
