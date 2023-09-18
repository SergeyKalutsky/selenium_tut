from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
urls = [
    'https://www.google.com/',
    'https://www.youtube.com/',
    '',
    23,
    'https://algoritmika.org/ru',
    'ftp://algoritmika.org/ru',
]

for url in urls:
    driver.get(url)
    # Важно делать паузу между запросами
    sleep(3)
