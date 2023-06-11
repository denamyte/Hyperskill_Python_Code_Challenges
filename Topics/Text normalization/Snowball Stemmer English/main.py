from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer('english')
print(*(stemmer.stem(token) for token in input().split()), sep='\n')
