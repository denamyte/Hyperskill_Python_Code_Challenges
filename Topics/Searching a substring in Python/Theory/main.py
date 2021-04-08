#  You can experiment here, it won’t be checked

count = 0


def contains(text, pattern):
    global count

    for i in range(len(text) - len(pattern) + 1):
        found = True

        for j in range(len(pattern)):
            count += 1
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return True

    return False


contains('acacabad', 'cab')
print(count)