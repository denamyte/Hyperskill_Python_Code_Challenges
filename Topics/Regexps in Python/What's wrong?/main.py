import re

w1 = input()
w2 = input()
print(len(w1) * 2 if re.match(w1, w2) else 'no matching')
