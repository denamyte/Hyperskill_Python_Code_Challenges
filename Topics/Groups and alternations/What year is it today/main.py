import re


match = re.match(r'(\d\d?[/.]){2}(\d{4})', input())
print(match and match.group(2))
