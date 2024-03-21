from PIL import Image

# Сборка изображения из известных каналов изображения.
img = Image.open("assets/img1.jpg")
R, G, B = img.split()
img2 = Image.merge("RGB", (R, G, B))
print(img2.mode)
img2.show()

