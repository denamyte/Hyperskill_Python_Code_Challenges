word = input()
under = word[0].lower()
for char in word[1:]:
    if not char.islower():
        under += '_' + char.lower()
    else:
        under += char
print(under)
