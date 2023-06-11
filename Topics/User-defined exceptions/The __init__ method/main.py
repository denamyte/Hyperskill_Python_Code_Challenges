# class NotWordError(Exception):
#     def __init__(self, word):
#         self.message = word + " is not a word, sorry!"
#         super().__init__(self.message)


def check_word(word: str):
    if '0' in word:
        raise NotWordError(word)
    return word


def error_handling(word):
    try:
        print(check_word(word))
    except NotWordError as e:
        print(e)


# error_handling('clear_word')
# error_handling('dirty_0_word')
