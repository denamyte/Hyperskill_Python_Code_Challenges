from bs4 import BeautifulSoup as BeS

with open('data/dataset/input.txt') as f:
    print(*(x.get('name') for x in BeS(f.read(), 'xml').
          find_all('member')), sep=' ')
