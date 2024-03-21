from PIL import Image

# # Копию
# # Открываем изображение
# img = Image.open("assets/img1.jpg")
# # Создаем копию:
# img2 = img.copy()
# # Просматриваем копию:
# img2.show()

# # Уменьшенную версию
# # Открываем изображение
# img = Image.open("assets/img1.jpg")
# print(img.size)
# img.thumbnail((400, 300))
# print(img.size)


# Уменьшенную версию
# Открываем изображение
img = Image.open("assets/img1.jpg")
newSize = (400, 400)
imgnr = img.resize(newSize)
imgnr.show()
