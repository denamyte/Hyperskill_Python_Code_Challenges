sums = open('sums.txt')
for line in sums:
    print(sum((int(x) for x in line.split(' '))))
sums.close()
