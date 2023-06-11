num_list = []
while len(num_list) == 0 or sum(num_list) != 0:
    num_list.append(int(input()))
print(sum(num ** 2 for num in num_list))
