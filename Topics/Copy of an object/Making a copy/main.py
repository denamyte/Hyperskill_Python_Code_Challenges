import copy


def my_copy(obj, copy_mode):
    return copy.copy(obj) if copy_mode == 'shallow copy' else copy.deepcopy(obj)
