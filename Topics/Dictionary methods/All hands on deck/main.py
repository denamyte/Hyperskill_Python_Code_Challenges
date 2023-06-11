# Sorry, there is no need in a dictionary here
faced_cards = ['Jack', 'Queen', 'King', 'Ace']
print(sum(map(lambda x: 11 + faced_cards.index(x) if x in faced_cards else int(x), (input() for _ in range(6)))) / 6)
