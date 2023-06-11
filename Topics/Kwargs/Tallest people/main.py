def tallest_people(**people: int):
    height = max(people.values())
    names = [k for k, v in people.items() if v == height]
    for name in sorted(names):
        print(f'{name} : {height}')
