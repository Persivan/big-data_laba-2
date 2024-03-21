from PIL import Image

# Смотрим цвет пикселя
# img = Image.open("assets/img1.jpg")
# obj = img.load()
# print(obj[25, 45])
# obj[25, 45] = (255, 0, 0)
# img.show()

# Получите и измените цвет пиксела методами gel() и putpixel()
img = Image.open("assets/img1.jpg")
print(img.getpixel((25, 45)))
img.putpixel((25, 45), (0, 0, 255))
print(img.getpixel((25, 45)))
img.show()