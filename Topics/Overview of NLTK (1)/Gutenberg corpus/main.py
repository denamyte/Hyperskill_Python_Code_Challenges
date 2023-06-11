from nltk.corpus import gutenberg


sentences = gutenberg.sents("whitman-leaves.txt")
print(sentences[int(input())])
