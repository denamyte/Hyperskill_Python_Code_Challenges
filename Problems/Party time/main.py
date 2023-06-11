guests = []
while True:
    guest = input()
    if guest == '.':
        break
    guests.append(guest)
print(f'{guests}\n{len(guests)}')
