def check_email(email: str):
    return ' ' not in email and '@' in email and '@.' not in email and '.' in email[email.find('@'):]
# print(check_email(input()))


a_set = {'word'}
print(a_set)
a_set = {'word', 'www'}
print(a_set)
a_set.pop()
