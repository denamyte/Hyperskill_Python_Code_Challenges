import string as s
from typing import List
from enum import Enum


class States(Enum):
    SPACE = 1
    ONE_HASH = 2
    SKIP_TO_SPACE = 3
    LETTER_IN_HASH = 4


def search_hashes(sentence: str) -> List[str]:
    hash_words: List[str] = []
    hash_word = ''
    state = States.SPACE
    for symbol in sentence:
        if state == States.SPACE:
            if symbol == '#':
                state = States.ONE_HASH
            elif symbol != ' ':
                state = States.SKIP_TO_SPACE
        elif state == States.ONE_HASH:
            if is_letter(symbol):
                state = States.LETTER_IN_HASH
                hash_word = symbol
            else:
                state = States.SKIP_TO_SPACE
        elif state == States.SKIP_TO_SPACE:
            if symbol == ' ':
                state = States.SPACE
        elif state == States.LETTER_IN_HASH:
            if is_letter(symbol):
                hash_word += symbol
            else:
                if symbol in '.,!? ':
                    hash_words.append(hash_word)
                    if symbol == ' ':
                        state = States.SPACE
                    else:
                        state = States.SKIP_TO_SPACE
                else:
                    state = States.SKIP_TO_SPACE
                hash_word = ''
    if len(hash_word):
        hash_words.append(hash_word)
    return hash_words


def is_letter(symbol):
    return symbol in s.ascii_lowercase or symbol in s.ascii_uppercase


hashtags = search_hashes(input())
print(*hashtags, sep='\n')
