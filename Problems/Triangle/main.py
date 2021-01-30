height = int(input())
width = 2 * height - 1
for level in range(height):
    print(('#' * (1 + 2 * level)).center(width, ' '))
