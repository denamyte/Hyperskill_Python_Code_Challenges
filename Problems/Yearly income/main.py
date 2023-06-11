with open('salary.txt', 'r') as s, open('salary_year.txt', 'w') as sy:
    for line in s:
        sy.write(f'{int(line) * 12}\n')
