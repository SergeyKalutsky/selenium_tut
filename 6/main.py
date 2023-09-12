import pickle
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver


data = [['короткие', 'https://vse-shutochki.ru/korotkie-anekdoty'], 
        ['про евреев', 'https://vse-shutochki.ru/anekdoty-pro/evrei'], 
        ['про Вовочку', 'https://vse-shutochki.ru/anekdoty-pro/vovochka'], 
        ['про русских', 'https://vse-shutochki.ru/anekdoty-pro/russkie'], 
        ['про Штирлица', 'https://vse-shutochki.ru/anekdoty-pro/shtirlic'], 
        ['про мужика', 'https://vse-shutochki.ru/anekdoty-pro/muzhik'], 
        ['про Чебурашку', 'https://vse-shutochki.ru/anekdoty-pro/чебурашка'], 
        ['про медведя', 'https://vse-shutochki.ru/anekdoty-pro/medved'], 
        ['про немцев', 'https://vse-shutochki.ru/anekdoty-pro/nemcy'], 
        ['про Чапаева', 'https://vse-shutochki.ru/anekdoty-pro/chapaev'], 
        ['про русского и немца', 'https://vse-shutochki.ru/anekdoty-pro/russkiy-nemec'], 
        ['про жену', 'https://vse-shutochki.ru/anekdoty-pro/жена']]


def parse_page(soup):
    aneks_list = []
    posts = soup.find_all('div', class_='post noSidePadding')
    for post in posts[:-2]:
        if post.div:
            aneks_list.append(post.div.text.strip())
    return aneks_list

def cook_soup(driver):
    return BeautifulSoup(driver.page_source, features="lxml")

driver = webdriver.Chrome()
url = 'https://vse-shutochki.ru/anekdoty'
aneks = {}
for category, url in data:
    driver.get(url)
    sleep(3)
    soup = cook_soup(driver)
    aneks[category] = parse_page(soup)

with open('aneks.pickle', 'wb') as f:
    pickle.dump(aneks, f)

    