data = [0]


def running_sum(s: str) -> int:
    data[0] += int(s)
    return data[0]


print([running_sum(c) for c in input()])
