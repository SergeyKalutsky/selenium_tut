import requests
from bs4 import BeautifulSoup


res = requests.get('https://ru.wikipedia.org/wiki/Python')
soup = BeautifulSoup(res.text, features="lxml")
table = soup.find_all('table', class_='wikitable')[0]
trs = table.find_all('tr')
for tr in trs:
    tds = tr.find_all('td')
    row = []
    for td in tds:
        row.append(td.text.strip())
    print(row)