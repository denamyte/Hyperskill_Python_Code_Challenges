class Puppy:
    n_puppies = 0  # number of created puppies

    def __new__(cls, *args, **kwargs):
        if cls.n_puppies < 10:
            cls.n_puppies += 1
            return object.__new__(cls)
        return None

    def __init__(self, n: int):
        self.n = n

    def __repr__(self):
        return f'{Puppy.__name__}({self.n})'


for i in range(15):
    print(Puppy(i))
