def has_prefix(w, p):
    return len(w) >= len(p) and all(c1 == c2 for c1, c2 in zip(w, p))
    # return w.startswith(p)


prefix = input()
words = input().split()

for word in words:
    if has_prefix(word, prefix):
        print(word)
