class NegativeSumError(Exception):
    def __init__(self):
        super().__init__("The sum is negative!")


def sum_with_exceptions(a, b):
    result = a + b
    if result < 0:
        raise NegativeSumError
    return result
