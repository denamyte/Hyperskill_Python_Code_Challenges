SUBS = {'é': 'e', 'ë': 'e', 'á': 'a', 'å': 'a', 'œ': 'oe', 'æ': 'ae'}


def normalize(name):
    return ''.join(SUBS.get(c, c) for c in name)


print(normalize(input()))
