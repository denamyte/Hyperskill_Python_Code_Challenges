def price_string(func):
    def wrapper(arg):
        result = func(arg)
        return f'£{result}'

    return wrapper  


DISCOUNT = 0.9


@price_string
def new_price(old_price) -> float:
    return old_price * DISCOUNT

# Sometimes, the desire to get rid of style errors (discovered
# by the cool modern grading system) leads to ridiculous results...
