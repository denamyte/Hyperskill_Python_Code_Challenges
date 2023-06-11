s = input()
counter = 0
for ch in s:
    counter += 1 if ch == '(' else -1 if ch == ')' else 0
    if counter < 0:
        break
print('ERROR' if counter else 'OK')
