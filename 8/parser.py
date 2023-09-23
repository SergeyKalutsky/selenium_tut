import uuid
import shutil
import requests
import mimetypes
import urllib.parse
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

def download_image(src, folder):
    r = requests.get(src, stream=True)
    if r.status_code == 200:
        mime_type = r.headers['content-type']
        ext = mimetypes.guess_extension(mime_type)
        fname = f'{folder}/{uuid.uuid4()}{ext}'
        with open(fname, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)  


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
searches = ['покушать', 'космос', 'абстракция']

for search in searches:
    q = urllib.parse.quote_plus(search)
    url = f'https://www.bing.com/images/search?q={q}&form=RESTAB&first=1'
    driver.get(url)
    sleep(3)
    a_tags = driver.find_elements('xpath', '//div[@class="imgpt"]//a[@href]')
    for a_tag in a_tags:
        href = a_tag.get_attribute('href')
        if 'images/search?' in href:
            if 'www.bing.com' not in href:
                driver.get('https://www.bing.com' + href) 
            else:
                driver.get(href) 
            break
    sleep(3)
    for i in range(100):
        img_xpath = '//div[@role="main"]//img[@tabindex]'
        img = driver.find_element('xpath', img_xpath)
        src = img.get_attribute('src')
        try:
            download_image(src, 'not_hot_dogs')
        except Exception as e:
            print(e)
        sleep(1)
        # Если нет кнопки далее, значит фото закончились
        try:
            next_image_button = driver.find_element('xpath', '//*[@id="navr"]/span')
        except NoSuchElementException:
            break
        next_image_button.click()
        sleep(3)
        print('=================================================')
        print(f'На картике № {i+1} {search}')
        print('=================================================')
    