BOUNDS = (120, 137)


def check(x):
    print(x if BOUNDS[0] < x < BOUNDS[1] else "That's a bad present!")
