import requests
from bs4 import BeautifulSoup


res = requests.get('https://www.tiobe.com/tiobe-index/')
soup = BeautifulSoup(res.text, features="lxml")

table = soup.find('table', id='top20')
trs = table.find_all('tr')
for tr in trs[1:]:
    tds = tr.find_all('td')
    row = []
    for td in tds[4:]:
        row.append(td.text.strip())
    print(row)
