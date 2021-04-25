def heading(caption: str, level=1):
    level = 1 if level < 1 else level if level < 6 else 6
    return f'{"#" * level} {caption}'
