from PIL import Image
from pylab import *

# Откройте в картинку, выведите ее на экран и напишите программу,
# выводящую координаты трех кликнутых на картинке точек:
im = array(Image.open("assets/img1.jpg"))
imshow(im)
print("Please click 3 points")
x = ginput(3)
print("you clicked:", x)
