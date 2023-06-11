# The following line creates a dictionary from the input. Do not modify it, please
d = json.loads(input())

print('min:', min(d, key=d.get))
print('max:', max(d, key=d.get))
