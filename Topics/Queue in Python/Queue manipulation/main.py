from collections import deque

queue = deque()
n = int(input())
for _ in range(n):
    cmd = input()
    if cmd.startswith('D') and len(queue) > 0:
        queue.pop()
    else:
        queue.appendleft(cmd.split(' ')[1])

while len(queue) > 0:
    print(queue.pop())
