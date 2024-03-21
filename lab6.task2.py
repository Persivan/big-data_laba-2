from PIL import Image

# Загрузите изображение, создайте его уменьшенную, а затем вставьте ее в
# исходное изображение, причем вокруг вставленного изображения отобразите
# рамку красного цвета.
# img = Image.open("assets/img1.jpg")
# img2 = img.resize((200, 150))
# print(img2.size)
# img.paste((255, 0, 0), (9, 9, 211, 161))
# img.paste(img2, (10,10))
# img.show()

# Выведите белую полупрозрачную горизонтальную полосу высотой 100
# пикселов. Для этого выполните:
# img = Image.open("assets/img1.jpg")
# white = Image.new("RGB", (img.size[0], 100), (255, 255, 255))
# mask = Image.new("L", (img.size[0], 100), 64)
# img.paste(white, (0, 0), mask)
# img.show()

# Копируйте и вставьте повернутую часть изображения
img = Image.open("assets/img1.jpg")
box = (100, 100, 400, 400)
region = img.crop(box)
region = region.transpose(Image.ROTATE_180)
img.paste(region, box)
img.show()
