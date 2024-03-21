from PIL import Image

# # Создание нового изображения.
# img = Image.new("RGB", (100, 100))
# img.show()
#
# img = Image.new("RGB", (100, 100), (255, 0, 0))
# img.show()
#
# img = Image.new("RGB", (100, 100), "green")
# img.show()
#
# img = Image.new("RGB", (100, 100), "#f00")
# img.show()
#
# img = Image.new("RGB", (100, 100), "white")
# img.show() # Белый квадрат
#
# # Создайте серый квадрат.
# img = Image.new("RGB", (320, 240), "silver")
# img.show() # Серый квадрат

# # 7. Создайте цветной прямоугольник.
# img = Image.new("RGB", (320, 240), "rgb(205,100,200)")
# img.show() # цветной прямоугольник

# # 8. Создайте цветной прямоугольник (Каналы в процентах).
# img = Image.new("RGB", (320, 240), "rgb(10%,100%,40%)")
# img.show() # цветной прямоугольник. Каналы в процентах

# # 9. Создайте цветной прямоугольник заданного цвета. Затем поменяйте этот цвет.
# img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
# img.show() # сиреневый прямоугольник
# for x in range(640):
#  for y in range(480):
#    img.putpixel((x,y),(0,160,0))
# img.save("okno.png", "PNG")
# img.show() # зеленый прямоугольник

# 10. Создайте прямоугольник заданного цвета (функциональная раскраска).
img = Image.new("RGB", (640, 480), "rgb(205,100,200)")
img.show() # сиреневый прямоугольник
for x in range(640):
 for y in range(480):
   img.putpixel((x,y),(int(x/3),int((x+y)/6),int(y/3)))
img.save("okno.png", "PNG")
img.show() # прямоугольник с функциональной раскраской











