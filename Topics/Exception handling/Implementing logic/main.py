data = input()
print(f'Welcome to our party, {data}'
      if len(data.split()) == 2
      else 'You need to enter exactly 2 words. Try again!')
