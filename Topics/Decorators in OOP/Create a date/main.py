class Date:

    def __init__(self, day, month):
        self.day = day
        self.month = month

    @property
    def date(self):
        return '{}/{}'.format(self.day, self.month)
