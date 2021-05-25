from collections import Counter

_ = [print(k, v) for k, v in Counter(input().lower().split()).items()]
