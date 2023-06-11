planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file = open('planets.txt', 'w')
file.writelines((x + y for x, y in zip(planets, '\n' * len(planets))))
file.close()
