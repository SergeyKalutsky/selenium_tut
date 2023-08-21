from time import sleep
from selenium import webdriver

visited_urls = []

# Скачать chromedriver и создать
driver = webdriver.Chrome()
url = 'https://learn.algoritmika.org/login'
driver.get(url)
login = 'evalex'
password = '1804'
sleep(3)
# Заполняем поле логина
login_input = driver.find_element('xpath', '//input[@data-qa-id="login-input"]')
login_input.send_keys(login)
sleep(1)
# Нажимаем кнопку далее
button = driver.find_element('xpath', '//button[@data-qa-id="submit-auth-button"]')
button.click()
sleep(1)
# Вводим пароль
password_input = driver.find_element('xpath', '//input[@data-qa-id="password-input"]')
password_input.send_keys(password)
sleep(1)
button = driver.find_element('xpath', '//button[@data-qa-id="submit-auth-button"]')
button.click()
sleep(3)
# Переходим на зал славы
tab_menu = driver.find_element('xpath', '//a[@data-qa-header-link="community"]')
tab_menu.click()
sleep(1)
# Переходи на раздел популярные
tab_menu = driver.find_element('xpath', '//a[@href="/community?category=best"]')
tab_menu.click()
sleep(5)
# Получаем все элементы с проектами
project_cards = driver.find_elements('xpath', '//div[@data-qa-id="project-card-v3"]')
for project_card in project_cards:
    # В каждом элементе мы находим внутриние элементы, автор, название и статистику
    # Для того, чтобы xpath искал внутри элемента мы добавляем . в начале
    author = project_card.find_element('xpath', './/a[contains(@class,"styles__Author")]')
    title = project_card.find_element('xpath', './/a[@data-qa-project-card-title="true"]')
    stats = project_card.find_element('xpath', './/div[contains(@class, "styles__StatsRow")]')
    stats = stats.text.split('\n')
    print(title.text, author.text, stats, sep=' | ')