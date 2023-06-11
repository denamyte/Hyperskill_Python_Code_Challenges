from nltk.tokenize import regexp_tokenize

s, i = input(), int(input())
print(regexp_tokenize(s, '[A-z]+')[i])
