info = input().split(', ')
name, age, city, *miscellaneous = info
print(f'''\
name: {name}
age: {age}
city: {city}
miscellaneous: {' '.join(miscellaneous)}''')
