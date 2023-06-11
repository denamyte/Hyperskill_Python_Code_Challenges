def even(n):
    for x in range(n):
        yield x * 2


for i in even(int(input())):
    print(i)
