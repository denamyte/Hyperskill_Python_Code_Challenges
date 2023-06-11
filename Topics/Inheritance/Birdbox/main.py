class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __str__(self):
        return f"Hi, I'm an undefined bird named {self.name}"


class Pigeon(Bird):
    def __str__(self):
        return f"Hi, I'm a pigeon bird named {self.name}"


class Sparrow(Bird):
    def __str__(self):
        return f"Hi, I'm a sparrow bird named {self.name}"

