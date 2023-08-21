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
sleep(10)