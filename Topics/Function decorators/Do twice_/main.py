def do_twice(function):
    def fn(*args):
        return function(*args), function(*args)

    return fn
