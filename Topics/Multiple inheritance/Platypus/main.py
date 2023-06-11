class Animal:
    def __init__(self, name):
        self.name = name
        print("Created an Animal")


class Mammal(Animal):
    def __init__(self, name):
        print('Created a Mammal')
        super().__init__(name)
        if self.name == '':
            pass


class Reptile(Animal):
    def __init__(self, name):
        print('Created a Reptile')
        super().__init__(name)
        if self.name == '':
            pass


class Platypus(Mammal, Reptile):
    def __init__(self, name):
        print('Created a Platypus')
        super().__init__(name)
        if self.name == '':
            pass


# p = Platypus("George")
