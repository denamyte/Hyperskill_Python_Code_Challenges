# work with a list from this variable
def divide(n: int):
    if n < 5:
        less_than_5.append(n)
    elif n > 5:
        greater_than_5.append(n)


less_than_5, greater_than_5 = [], []
for c in input():
    divide(int(c))
print(less_than_5)
print(greater_than_5)
