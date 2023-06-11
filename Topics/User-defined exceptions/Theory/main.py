class DateDelimiterError(Exception):
    def __str__(self):
        return "You should use the '/' sign as a delimiter."


data = input()
if '/' not in data:
    raise DateDelimiterError
else:
    print(data)
