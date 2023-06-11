from collections import deque

queue = deque()
passed = []
actions = {'READY': lambda name: queue.appendleft(name),
           'EXTRA': lambda _: queue.appendleft(queue.pop()),
           'PASSED': lambda _: passed.append(queue.pop())}
n = int(input())
for _ in range(n):
    cmd = input().split(' ')
    actions[cmd[0]](None if len(cmd) == 1 else cmd[1])

print('\n'.join(passed))
