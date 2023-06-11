def create_bounds_checker(lo: int, hi: int):
    def check(number: int):
        if lo <= number <= hi:
            return number
        raise NotInBoundsError()

    return check


def create_handler(some_checker_fn):
    def handler(number):
        try:
            print(some_checker_fn(number))
        except NotInBoundsError as e:
            print(e)

    return handler


check_integer = create_bounds_checker(45, 67)
error_handling = create_handler(check_integer)
