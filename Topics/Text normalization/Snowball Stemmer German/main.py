from nltk.stem.snowball import SnowballStemmer

sent = input().split()
stemmer = SnowballStemmer("german")
print(*(stemmer.stem(w) for w in sent), sep='\n')
