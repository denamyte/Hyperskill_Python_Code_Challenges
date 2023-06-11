import operator

s = sorted(books.items(), key=lambda i: i[1])
print(s[0][0], s[-1][0], sep='\n')