import re

p = re.compile(r'\+(?P<c>\d)[ -]?(?P<a>\d{3})[ -]?(?P<n>\d{3}(?:[ -]?\d{2}){2})')
m = p.match(input())
print('No match' if not m else f'''\
Full number: {m.group()}
Country code: {m.group("c")}
Area code: {m.group("a")}
Number: {m.group("n")}''')
