class User:
    def __init__(self, *data):
        self.name, self.surname, self.age, self.country = data

    def user_information(self):
        print(f'{self.name} {self.surname} is {self.age} years old and lives in {self.country}.')


User(*(input() for _ in range(4))).user_information()
