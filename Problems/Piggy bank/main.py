class PiggyBank:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars: int, deposit_cents: int):
        from_cents, self.cents = divmod(self.cents + deposit_cents, 100)
        self.dollars += deposit_dollars + from_cents


def test():
    for d, c in [[0, 99], [0, 88], [500, 500]]:
        bank = PiggyBank(1, 1)
        bank.add_money(d, c)
        print(f'[1, 1] + [{d}, {c}] = [{bank.dollars}, {bank.cents}]')


# test()
