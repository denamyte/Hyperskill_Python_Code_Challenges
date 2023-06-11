# Let's try to solve this in general...
from typing import Any, List, Union

_any = Union[str, List[Any]]


def make_nested_lists(index: int, arg: _any) -> _any:
    return make_nested_lists(index - 1, [arg]) if index else arg


number_of_inputs = 3
result = [make_nested_lists(i, input()) for i in range(number_of_inputs)]
print(result)
