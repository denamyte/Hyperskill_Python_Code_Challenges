from nltk.stem import LancasterStemmer

stemmer = LancasterStemmer()
print(*(stemmer.stem(token) for token in input().split()), sep='\n')
