nums = []
while True:
    s = input()
    if s == '.':
        break
    nums.append(int(s))
print(sum(nums) / len(nums))
