def has_suffix(word, suffix):
    return word[-len(suffix):] == suffix


# Change the next line
extension = ".py"
n = int(input())

for _ in range(n):
    file = input()
    if has_suffix(file, extension):
        print(file)
