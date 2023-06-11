def to_upper(fn):
    def wrapper(s: str):
        return fn(s).upper()
    return wrapper
