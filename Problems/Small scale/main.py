nums = []
while True:
    s = input()
    if s == '.':
        break
    nums.append(float(s))
print(min(nums))
