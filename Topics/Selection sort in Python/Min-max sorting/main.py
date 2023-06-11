def condition(x, y, gt):
    return x > y if gt else x < y


def min_max_sort(elements):
    gt = 1
    for i in range(len(elements) - 1):
        index = i
        gt = (gt + 1) & 1

        for j in range(i + 1, len(elements)):
            if condition(elements[j], elements[index], gt):
                index = j

        # elements[index], elements[i] = elements[i], elements[index]
        # The above line causes 3 code style errors. So, I rewrote it into the following:
        temp = elements[index]
        elements[index] = elements[i]
        elements[i] = temp  # At last, there are no errors -> facepalm.jpg...
        # Yet "Possibly misspelt word" - You wrote this, no? Are you kidding me?
        # So, "misspelled", OK, thank you, The Great Grading System!


ar = list(map(int, input().split()))
min_max_sort(ar)
print(*ar)
