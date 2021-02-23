from collections import deque

stack = deque()
for _ in range(int(input())):
    cmd = input()
    if cmd.startswith('POP'):
        stack.pop()
    else:
        stack.append(int(cmd.split(' ')[1]))

for _ in range(len(stack)):
    print(stack.pop())
