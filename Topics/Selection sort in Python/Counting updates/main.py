def selection_sort(ar):
    length = len(ar)
    count = 0
    for i in range(length - 1):
        index = i

        for j in range(i + 1, length):
            if ar[j] < ar[index]:
                count += 1
                index = j

        ar[i], ar[index] = ar[index], ar[i]

    return count


n = int(input())
updates = [selection_sort(list(map(int, input().split()))) for _ in range(n)]
max_count = max(updates)
print(updates.index(max_count), max_count)
