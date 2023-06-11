# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

family = {}
family.update(first_family)
family.update(second_family)
print(family)
