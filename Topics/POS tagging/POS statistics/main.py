from collections import Counter

from nltk.tokenize import word_tokenize
from nltk import pos_tag

tokens = word_tokenize(input())
print(Counter(x[1] for x in pos_tag(tokens)).most_common(1)[0][0])
