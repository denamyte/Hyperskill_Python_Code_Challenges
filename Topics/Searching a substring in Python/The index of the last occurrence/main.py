def find_last(text, pattern):
    t_len, p_len = len(text), len(pattern)
    if t_len < p_len:
        return -1

    for i in range(t_len - p_len, -1, -1):
        found = True

        for j in range(p_len):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            return i

    return -1


print(find_last(input(), input()))
