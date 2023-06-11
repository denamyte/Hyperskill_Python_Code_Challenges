def tagged(func):
    def wrapper(string):
        result = func(string)
        return f'<title>{result}</title>'
    return wrapper


# @tagged
# def from_input(user_input):
#     string = user_input.strip()
#     return string


# print(from_input('  A title string   '))
