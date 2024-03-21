# Просто открыть
from PIL import Image
img = Image.open("assets/img1.jpg")
print(img.size,)
print(img.format)
print(img.mode)
print(img.info)
print(img.getbbox())