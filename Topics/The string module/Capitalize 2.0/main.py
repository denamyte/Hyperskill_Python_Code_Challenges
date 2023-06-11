import string

inp = (input(), input())
seps = ('\n', ' ')
for i, s in zip(inp, seps):
    print(string.capwords(i, s))
