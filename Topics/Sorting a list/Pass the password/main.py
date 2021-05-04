# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

for pwd in sorted(passwords, key=len):
    print(pwd, len(pwd))
