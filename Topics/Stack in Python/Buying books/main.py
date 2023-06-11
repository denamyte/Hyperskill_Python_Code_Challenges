def action():
    full = input()
    if len(full) == 4:
        shelf.append(stack.pop())
    else:
        stack.append(full[4:])


shelf = []
stack = []
for _ in range(int(input())):
    action()
print('\n'.join(shelf))
