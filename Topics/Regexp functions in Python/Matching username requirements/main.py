import re

name = input()
print('Thank you!' if re.match('[a-zA-Z]+', name) else 'Oops! The username has to start with a letter.')
