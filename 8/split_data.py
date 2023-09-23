import os
import shutil
from random import sample

if not os.path.exists('train'):
    os.mkdir('train')
    
if not os.path.exists('test'):
    os.mkdir('test')

i = 0
folder = 'hot_dogs_resized564x564'
for file in os.listdir(folder):
    ext = file.split('.')[-1]
    shutil.move(f'{folder}/{file}', f'train/hd_{i}.{ext}')
    i += 1

folder = 'not_hot_dogs_resized564x564'
for file in os.listdir(folder):
    ext = file.split('.')[-1]
    shutil.move(f'{folder}/{file}', f'train/nhd_{i}.{ext}')
    i += 1
    
files = os.listdir('train')
test = sample(files, int(len(files)*0.1))

for file in test:
    shutil.move(f'train/{file}', f'test/{file}')
    