class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    def __add__(self, t):
        return Task('{}\n{}'.format(self.description, t.description),
                    '{}, {}'.format(self.team, t.team))
