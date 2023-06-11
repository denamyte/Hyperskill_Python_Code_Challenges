import re

template = r'... Jude'
s = input()
match = re.match(template, s)
print(match.group() if match else None)
