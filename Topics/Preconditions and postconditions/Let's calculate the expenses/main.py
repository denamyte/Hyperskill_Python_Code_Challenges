import re

res = re.finditer(r'(?<=\$)\d+', input())
total = sum(int(x.group()) for x in res)
print(f'This week you have spent: {total} dollars')
