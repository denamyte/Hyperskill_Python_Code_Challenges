from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

tokens = word_tokenize(str(input()).lower())
tagged = pos_tag(tokens)
print([word for word, tag in tagged if tag.startswith('V')])
