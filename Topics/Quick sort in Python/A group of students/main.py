from typing import Dict, List

dic: Dict[int, List[str]] = {}

count = int(input())
for _ in range(count):
    inp = input().split(' ')
    name = inp[0]
    age = int(inp[1])
    if age in dic:
        dic[age].append(name)
    else:
        dic[age] = [name]

for key in sorted(dic.keys()):
    for val in sorted(dic[key]):
        print(val)
