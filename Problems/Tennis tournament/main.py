number_of_inputs = int(input())
inputs = [input().split() for _ in range(number_of_inputs)]
winners = [inp[0] for inp in inputs if inp[1] == 'win']
print(f'{winners}\n{len(winners)}')
