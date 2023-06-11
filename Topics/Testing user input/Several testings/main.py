def check(raw):
    print('It is not a number!'
          if not str.isdigit(raw)
          else raw
          if int(raw) >= 202
          else 'There are less than 202 apples! You cheated me!')
