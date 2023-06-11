import re

print(re.split('<START>', re.split('<END>', input())[0])[1])
