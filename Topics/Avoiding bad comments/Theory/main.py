#  You can experiment here, it won’t be checked


names = ['Kate', 'Alexander', 'Oscar', 'Mary']

with open('names.txt', 'w', encoding='utf-8') as names_file:
    names_file.writelines(n + '\n' for n in names)
    names_file.writelines(n for n in names)
    # for name in names:
        # names_file.write(name + '\n')
        # names_file.write(name)


