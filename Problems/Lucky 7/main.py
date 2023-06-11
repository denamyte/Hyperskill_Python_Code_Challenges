nums = [int(input()) for _ in range(int(input()))]
nums = filter(lambda x: x % 7 == 0, nums)
nums = map(lambda x: x * x, nums)
for i in nums:
    print(i)

print(nums, '\n')
