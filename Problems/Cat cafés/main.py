# it seems it works without mentioning MEOW: it's enough to check the list length!
name, cats = '', 0
while True:
    lst = input().split()
    if len(lst) == 1:
        break
    [n, c] = lst
    if int(c) > cats:
        name, cats = n, int(c)
print(name)
