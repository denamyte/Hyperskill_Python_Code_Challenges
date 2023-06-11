import re

pattern = r'^@\w+'
print(re.sub(pattern[1:], '<HANDLE>', re.sub(pattern, '<AUTHOR>', input())))
