from nltk.stem import WordNetLemmatizer

lemma, word = WordNetLemmatizer(), input()
print(*(lemma.lemmatize(word, pos=pos) for pos in 'nav'), sep='\n')
