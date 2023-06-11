from collections import Counter

print(*[f'{num} {buy}' for buy, num in
        Counter(input().split()).items()],
      sep='\n')
