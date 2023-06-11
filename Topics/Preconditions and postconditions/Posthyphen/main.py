import re

print(re.search(r'(?<=-)\w+', input()).group())
