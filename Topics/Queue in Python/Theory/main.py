#  You can experiment here, it won’t be checked
other_list = [1, 2, 3]
# new_list = [x if x > 0 for x in other_list]
# new_list = [x for x in other_list if x == 0]
new_list = [x if x > 0 else -100 for x in other_list]
