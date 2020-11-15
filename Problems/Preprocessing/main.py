sentence = input()
for char in ',.!?':
    sentence = sentence.replace(char, '')
print(sentence.lower())
