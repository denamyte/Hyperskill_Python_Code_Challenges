def print_info(func):
    def wrapper(*args):
        print("The arguments of the function are:", *args)
        return func(*args)

    return wrapper


@print_info
def addition(*args):
    return sum(args)


# print(addition(*list(map(int, input().split()))))
