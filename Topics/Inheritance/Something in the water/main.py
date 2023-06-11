class WaterBody:
    def __init__(self, name, length):
        self.name = name  # str
        self.length = length  # int


class River(WaterBody):
    def flow(self, how: str):
        print(f"{self.name} is flowing {how}!")


SEINE_LENGTH = 777
SEINE_NAME = 'Seine'
seine = River(SEINE_NAME, SEINE_LENGTH)
