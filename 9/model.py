# pip install torch torchvision --user
# pip install opencv-python --user
# pip install numpy --user
import cv2
import numpy as np
from torchvision.models import resnet50, ResNet50_Weights
import torch
import torch.nn as nn

model = resnet50(weights=ResNet50_Weights.DEFAULT)

# Нам нужно заменить последний слой, потому что у нас всего два класса
model.fc = nn.Sequential(
    nn.Linear(2048, 1, bias=True),
    nn.Sigmoid()
)
# Читаем модель и переводим её на CPU(потому что на обычном компе)
model.load_state_dict(torch.load(
    'best_model.pth', map_location=torch.device('cpu')))
model.eval()


def read_img(path):
    # Читаем, конвертируем и нормализуем изображение
    device = torch.device('cpu')
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (564, 564))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32)
    img /= 255.
    img = img[..., np.newaxis]
    img = torch.from_numpy(img).permute(3, 2, 0, 1)
    img.to(device)
    return img


def classify(img_path):
    img = read_img(img_path)
    with torch.no_grad():
        percentage = round(model(img).item(), 4)
        if percentage >= 0.5:
            return 'Не хотдог'
        return 'Хотдог'


filename = 'not_hot_dog.jpeg'
result = classify(filename)
print(result)
