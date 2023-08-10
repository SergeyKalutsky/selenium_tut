from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# Подавить output предупреждений на консоль
options.add_argument('log-level=3')
options.add_argument('--disable-dev-shm-usage')
# Скачать chromedriver и создать 
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                            options=options)

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
