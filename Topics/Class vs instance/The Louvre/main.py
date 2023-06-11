class Painting:
    museum = 'Louvre'

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.painter} ({self.year}) hangs in the {Painting.museum}.'


print(Painting(input(), input(), int(input())))
