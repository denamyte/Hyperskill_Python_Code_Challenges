from collections import deque

# please don't change the following line
candy_bag = deque(input().split())

for _ in range(int(input())):
    command = input()
    if command == 'TAKE':
        print(candy_bag.pop() if len(candy_bag) else 'We are out of candies :(')
    else:
        candy_bag.append(command[4:])
