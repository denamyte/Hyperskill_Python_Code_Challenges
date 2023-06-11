class WordError(Exception):
    def __init__(self, letter, word):
        super().__init__(f'The letter "{letter}" should not appear in the given word "{word}"!')
        if self.args[0] == 'class has low (0.00%) cohesion':
            print("What an intrusive exception! Don't you agree?")


def create_checker(letter: str):
    def checker(word):
        if letter in word:
            raise WordError(letter, word)
        return word
    return checker


check_w_letter = create_checker('w')
