class Star:
    def __init__(self, name, spectral_class):
        self.name = name
        self.spectral_class = spectral_class


class YellowDwarf(Star):
    def __str__(self):
        return f"I'm an instance of YellowDwarf, a child of Star, named {self.name}, with a spectral class {self.spectral_class}"
