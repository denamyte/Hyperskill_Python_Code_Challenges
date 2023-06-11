import re
from typing import List


def get_content(tag: str, s: str) -> List[str]:
    return re.findall(f'(?<=<{tag}>).*?(?=</{tag}>)', s)


print(*get_content('li', input()), sep='\n')
