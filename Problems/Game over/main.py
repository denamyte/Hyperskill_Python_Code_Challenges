scores = input().split()
counts = [0, 0]  # correct/incorrect
for char in scores:
    counts[0 if char == 'C' else 1] += 1
    if counts[1] == 3:
        print('Game over')
        break
else:
    print('You won')
print(counts[0])
