def unpack(input_tuple):
    unpacked = tuple()
    for item in input_tuple:
        unpacked += (item,) if isinstance(item, str) else unpack(item)
    return unpacked
