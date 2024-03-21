import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Открываем изображение
img = Image.open("assets/img1.jpg")

# Преобразуем изображение в массив numpy
im_array = np.asarray(img)

# Строим гистограмму
plt.hist(im_array.ravel(), bins=256, range=(0, 255), fc='k', ec='k')
plt.show()