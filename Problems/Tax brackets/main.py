print('%.2f' % (21/4))
tax_percents = {132407: 28,
                42708: 25,
                15528: 15,
                0: 0}
income = int(input())
for key in tax_percents:
    if income >= key:
        percent = tax_percents[key]
        tax = 0 if percent == 0 else round(income * percent / 100)
        print(f'The tax for {income} is {percent}%. '
              f'That is {tax} dollars!')
        break
