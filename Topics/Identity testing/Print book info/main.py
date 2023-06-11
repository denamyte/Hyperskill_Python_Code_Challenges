def print_book_info(title, author=None, year=None):
    print(f'"{title}"{was_written(author, year)}{by_author(author)}{in_year(year)}')


def was_written(author: str, year: int):
    return ' was written' if author or year else ''


def by_author(author: str):
    return ' by ' + author if author else ''


def in_year(year: int):
    return f' in {year}' if year is not None else ''
