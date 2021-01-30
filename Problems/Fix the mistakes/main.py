prefixes = 'https://', 'http://', 'www.'
for word in input().split():
    if word.lower().startswith(prefixes):
        print(word)

" ".join()
