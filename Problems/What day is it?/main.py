shifted = int(input()) + 10.5
print('Monday' if shifted < 0 else 'Tuesday' if shifted < 24 else 'Wednesday')
