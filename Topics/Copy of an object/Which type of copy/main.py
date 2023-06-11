import copy


def detect_copy():
    obj = [[1, 2]]
    copy_obj = copying_machine(obj)
    return f"{'shallow' if id(obj[0]) == id(copy_obj[0]) else 'deep'} copy"
