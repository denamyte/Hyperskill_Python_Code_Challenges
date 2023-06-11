class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    @classmethod
    def from_string(cls, raw: str):
        return cls(*raw.split(':'))

    @property
    def time(self):
        return '{}:{}'.format(self.hour, self.minute)

    def __str__(self):
        return '{}:{}'.format(self.hour, self.minute)
