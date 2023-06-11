import re

p = input()
print('Thank you!' if re.match(r'[A-z0-9]{6,15}$', p) else 'Error!')
