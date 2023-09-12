from bs4 import BeautifulSoup


with open('aneks.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), features='lxml')

aneks_list = []
posts = soup.find_all('div', class_='post noSidePadding')
for post in posts[:-2]:
    if post.div:
        aneks_list.append(post.div.text.strip())
