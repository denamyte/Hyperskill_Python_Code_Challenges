class Movie:
    def __init__(self, title: str, director: str, year: int):
        self.title = title
        self.director = director
        self.year = year


titanic = Movie('Titanic', 'James Cameron', 1997)
star_wars = Movie('Star Wars', 'George Lucas', 1977)
fight_club = Movie('Fight Club', 'David Fincher', 1999)
