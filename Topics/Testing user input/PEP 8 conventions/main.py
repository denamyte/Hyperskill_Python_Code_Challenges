def check_name(name):
    print("Never use the characters 'l', 'O', or 'I' as single-character variable names"
          if name in 'lOI'
          else 'It is a common variable'
          if str.islower(name)
          else 'It is a constant'
          if str.isupper(name)
          else "You shouldn't use mixedCase")


# while True:
#     check_name(input())
