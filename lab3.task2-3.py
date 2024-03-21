import fileinput

from PIL import Image

# Преобразуйте изображение из режима RGB в RGBA, используя split() и merge
# img = Image.open("assets/img1.jpg")
# print(img.mode)
# R, G, B = img.split()
# mask = Image.new("L", img.size, 128)
# img2 = Image.merge("RGBA", (R, G, B, mask))
# print(img2.mode)
# img2.show()

# Преобразуйте изображение из режима RGB в RGBA, используя convert()
# img = Image.open("assets/img1.jpg")
# print(img.mode)
# img2 = img.convert("RGBA")
# print(img2.mode)
# img2.show()

# Преобразуйте изображение RGB в формат P, указав смешивание цветов и адаптивную палитру в 128 цветов.
# img = Image.open("assets/img1.jpg")
# print(img.mode)
# img2 = img.convert("P", None, Image.FLOYDSTEINBERG, Image.ADAPTIVE, 128)
# print(img2.mode)
# img2.show()

# Сохраняем (не проверил, работает ли)
# img2.save("assets/img2.png") # Сохраняем
# img2.save("assets/img2.bmp", "BMP") # Сохраняем
# f = open("assets/img1.jpg", "wb")
# img.save(f, format="BMP")
# f.close()
