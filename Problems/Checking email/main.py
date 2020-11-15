def check_email(email: str):
    return ' ' not in email and '@' in email and '@.' not in email and '.' in email[email.find('@'):]
# print(check_email(input()))
