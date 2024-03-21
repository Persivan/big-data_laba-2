from PIL import Image

# Вырезаем кусок
# img = Image.open("assets/img1.jpg")
# img2 = img.crop( [0,0, 100, 100])
# img2.load()
# print(img2.size)
# img2.show()


# Измените размеры куска изображения
img = Image.open("assets/img1.jpg")
print(img.size)
img.show()
box = (100,100,300,300)
img2 = img.crop(box)
newsize = (400, 400)
img2nr = img2.resize(newsize)
img2nr.show()