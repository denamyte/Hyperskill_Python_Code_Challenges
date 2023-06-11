import itertools as it

for n in range(1, 4):
    for comb in it.combinations(flower_names, n):
        print(comb)
