# find vocabulary by "voc"
from typing import List

import numpy as np
from nltk import word_tokenize

text = str(input())

def bag_of_words(voc: List[str], text):
    array = np.zeros(len(voc)) # len(voc) stands for the size of the vocabulary

    # code here below
    tokens = word_tokenize(text.lower())
    for i in range(len(array)):
        array[i] = tokens.count(voc[i])

    return array


print(bag_of_words(voc, text))
