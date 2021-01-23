import re

# words = ['apple', 'pear', 'banana', 'Ananas']
prog = re.compile('^[aA]')
print([word for word in words if prog.match(word)])
