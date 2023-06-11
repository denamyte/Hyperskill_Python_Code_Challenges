import re


match = re.match('(Value|Name|Type)Error', input())
print(match and match.group(1))
