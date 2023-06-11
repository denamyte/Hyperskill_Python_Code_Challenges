import re

s = input()
match = re.search('^Good (morning|afternoon|evening)', s)
print(match.group() if match else 'No greeting!')
