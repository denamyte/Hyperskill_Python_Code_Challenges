from collections.abc import Hashable

objects_dict = {}
for o in objects:
    if isinstance(o, Hashable):
        objects_dict[o] = hash(o)
