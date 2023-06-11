import re

word = input()
print(bool(re.search(r'\bthe\b', word)))
