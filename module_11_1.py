import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as ml
from PIL import Image

#  Пример работы с REQUESTS

url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url, params={'symbol': 'BTCUSDT'})
price_object = response.json()
price = float(price_object['price'])
print('_________________________________')
print(f'Цена в данный момент: {price}')
print('_________________________________')

#  Пример работы с PANDAS

data_ = pd.read_excel('data.xlsx')
print(data_)
analysis = data_.sort_values(by='Age', ascending=False)
print(analysis)
print('_________________________________')

# Пример работы с NUMPY

list_ = [1, 3, 5, 7]
sum_ = np.array(list_)
print(sum_ * 4)
print(sum_ / 2)
print('_________________________________')

#  Пример работы с MATPLOTLIB

x = np.linspace(1, 5, 25)
y1 = np.sin(x)
y2 = np.cos(x)

ml.plot(x, y1, 'r-', label='Sin')
ml.legend()
ml.title('Sin')
ml.xlabel('x')
ml.ylabel('y')

ml.plot(x, y2, 'g-', label='Cos')
ml.legend()
ml.title('Cos')
ml.xlabel('x')
ml.ylabel('y')
ml.show()

# Примеры работы с PILLOW

image = Image.open('Image.jpg')
print(image.format, image.size, image.mode)
image_ = image.rotate(50)
image_ = image_.resize((1280, 720))
image_.save('imageres.png')
