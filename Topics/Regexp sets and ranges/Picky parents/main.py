import re

pattern = '[B-N][aeiou]'
if re.match(pattern, input()):
    print('Suitable!')
