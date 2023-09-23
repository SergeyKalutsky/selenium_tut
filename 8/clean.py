import os
from random import sample
from PIL import Image
import hashlib

images_path = 'not_hot_dogs'
files = sample(os.listdir(images_path), 628)
hashes = []
size = (564, 564)
resized_folder = images_path + f'_resized{size[0]}x{size[1]}'
if not os.path.exists(resized_folder):
    os.mkdir(resized_folder)

for filename in files:
    with open(f'{images_path}/{filename}', 'rb') as f:
        hash = hashlib.md5(f.read()).hexdigest()
    if hash in hashes:
        print(filename, 'Файл уже существует. Удаляем')
        os.remove(f'{images_path}/{filename}')
        continue
    hashes.append(hash)

for filename in files:
    if filename.split('.')[-1] not in ('jpg', 'png', 'jpeg'):
        print('Игнорируем')
        continue
    if not os.path.exists(f'{resized_folder}/{filename}'):
        try:
            img = Image.open(f'{images_path}/{filename}')
        except FileNotFoundError:
            print('Не смог найти файл')
        img = img.resize(size)
        try:
            img.save(f'{resized_folder}/{filename}')
            print(
                f'Файл сохранен с размером {size[0]}x{size[1]}: {resized_folder}/{filename}')
        except ValueError:
            print(f'Расширение не существует: {resized_folder}/{filename}')
