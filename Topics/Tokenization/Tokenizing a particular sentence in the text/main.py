from nltk import sent_tokenize, regexp_tokenize

sentence, i = input(), int(input())
print(regexp_tokenize(sent_tokenize(sentence)[i], "[A-z']+"))
