def squares(num):
    i = 1
    while i <= num:
        yield i * i
        i += 1


for x in squares(int(input())):
    print(x)
