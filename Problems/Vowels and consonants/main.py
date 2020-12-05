vowels = 'aeiou'
gibberish = input()
for char in gibberish:
    if not char.isalpha():
        break
    print('vowel' if char in vowels else 'consonant')
