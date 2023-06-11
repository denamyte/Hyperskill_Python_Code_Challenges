class Music:
    ...


class Rock(Music):
    ...


class Pop(Music):
    ...


class PopRock(Rock, Pop):
    ...


class Indie(Music):
    ...


class IndiePopRock(Indie, PopRock):
    ...


print(IndiePopRock.mro())
