a1 = open('animals.txt', 'r')
a2 = open('animals_new.txt', 'w')
for line in a1:
    a2.write(line.replace('\n', ' '))
a1.close()
a2.close()
