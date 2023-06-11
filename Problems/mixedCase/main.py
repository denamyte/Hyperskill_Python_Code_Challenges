words = input().split()
words[1:] = [w.capitalize() for w in words[1:]]
print(''.join(words))
