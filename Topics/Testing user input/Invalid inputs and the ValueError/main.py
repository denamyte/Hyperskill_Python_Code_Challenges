def check():
    raw = input()
    expected = False
    try:
        expected = 25 <= int(raw) <= 37
    except ValueError:
        pass
    print(raw if expected else 'Correct the error!')
