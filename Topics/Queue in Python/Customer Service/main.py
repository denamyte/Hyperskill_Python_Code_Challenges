from collections import deque

q = deque()
n = int(input())
for _ in range(n):
    query = input()
    if query == 'SOLVED' and len(q) > 0:
        q.pop()
    else:
        q.appendleft(query.split(' ')[1])
while len(q) > 0:
    print(q.pop())
