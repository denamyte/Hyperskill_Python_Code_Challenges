from itertools import product

itt = [zip(main_courses, price_main_courses), zip(desserts, price_desserts), zip(drinks, price_drinks)]

for comb in product(*itt):
    total = sum(meal[1] for meal in comb)
    if total <= 30:
        print(*[meal[0] for meal in comb], total)
