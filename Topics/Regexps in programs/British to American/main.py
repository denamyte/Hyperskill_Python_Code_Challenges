import re

print(re.sub(r'(?<=\w)ou(?=\w)', 'o', input()))
