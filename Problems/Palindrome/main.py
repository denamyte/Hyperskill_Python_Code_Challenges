word = input()
print("Palindrome" if word == ''.join(reversed(word)) else "Not palindrome")