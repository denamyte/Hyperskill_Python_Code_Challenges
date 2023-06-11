# please do not modify the following code
interest_rates = [float(x) for x in input().split(',')]
years = [int(x) for x in input().split(',')]
loan_principals = [int(x) for x in input().split(',')]

for i, y, l in zip(interest_rates, years, loan_principals):
    print(int(i * y * l))
