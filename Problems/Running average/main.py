def running_average(lst):
    return sum(lst) / len(lst)


digits = [int(c) for c in input()]
averages = [running_average(digits[i:i + 2]) for i in range(len(digits) - 1)]
print(averages)
