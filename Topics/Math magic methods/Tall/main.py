class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __iadd__(self, delta):
        self.height += delta
        return self

    def __isub__(self, delta):
        return self.__iadd__(-delta)
