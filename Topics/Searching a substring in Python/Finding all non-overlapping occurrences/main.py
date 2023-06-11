def find_no_overlaps(text: str, pattern: str):
    indexes = []
    index = text.find(pattern)
    while index != -1:
        indexes.append(index)
        index = text.find(pattern, index + len(pattern))
    return indexes or [-1]


print(*find_no_overlaps(input(), input()))
