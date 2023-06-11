# our class Ship
class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def sail(self, destination):
        return "The {} has sailed for {}!".format(self.name, destination)


black_pearl = Ship("Black Pearl", 800)
print(black_pearl.sail(input()))