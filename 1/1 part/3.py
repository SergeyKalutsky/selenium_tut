from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# Подавить output предупреждений на консоль
options.add_argument('log-level=3')
options.add_argument('--disable-dev-shm-usage')
# Скачать chromedriver и создать 
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),
                            options=options)

urls = [
    'https://www.google.com/',
    'https://www.youtube.com/',
    'https://www.python.org/',
    'https://learn.javascript.ru/',
    'https://algorithmicschool.com/'
    # И так далее до 10 сайтов
]
for url in urls:
    driver.get(url)
    print(f'Успешно зашли на сайт: {url}')
    # Важно делать паузу между запросами
    sleep(3)
