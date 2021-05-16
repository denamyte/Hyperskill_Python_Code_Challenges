# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

children = [int(input()) for _ in range(int(input()))]
kindergarten = dict.fromkeys(groups)
kindergarten.update(zip(groups, children))

print(kindergarten)
