# use the function blackbox(lst) that is already defined
my_list = [1, 2, 3]
blackboxed_list = blackbox(my_list)
print('modifies' if my_list is blackboxed_list else 'new')
