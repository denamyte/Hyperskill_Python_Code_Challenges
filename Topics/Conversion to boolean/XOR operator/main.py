def xor(a, b):
    return False if a and b or not a and not b \
        else a or b


# print(xor(0, 0))  # False
# print(xor(1, 2))  # False
# print(xor(1, 0))  # 1
# print(xor(0, 2))  # 2
