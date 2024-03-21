from PIL import Image

# Осуществите вращение изображения
# img = Image.open("assets/img1.jpg")
# print(img.size)
# img2 = img.rotate(90)
# print(img2.size)
# img3 = img.rotate(45, Image.NEAREST)
# print(img3.size)
# img4 = img.rotate(45, expand=True)
# print(img4.size)

img = Image.open("assets/img1.jpg")
img2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img2.show()
img3 = img.transpose(Image.FLIP_TOP_BOTTOM)
img3.show()


