animals = {
    6769: 'sheep',
    3848: 'cow',
    1296: 'pig',
    678: 'goat',
    23: 'chicken'
}
money = int(input())


def get_animal():
    for key in animals:
        if money >= key:
            count = money // key
            animal = animals[key]
            return '{} {}'.format(count, animal if animal == 'sheep' or count == 1 else animal + 's')
    return 'None'


print(get_animal())
