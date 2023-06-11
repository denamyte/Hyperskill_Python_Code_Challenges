def object_with_beautiful_identity():
    for i in range(10_000):
        if (id(i) - 888) % 1000 == 0:
            return i
    return None
