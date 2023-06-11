import requests

from bs4 import BeautifulSoup


i = int(input())
url = input()

resp = requests.get(url)
soup = BeautifulSoup(resp.content, features='html.parser')
print(soup.find_all('h2')[i].text)
