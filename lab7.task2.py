from PIL import Image, ImageFilter, ImageFont, ImageDraw
from pylab import *

# Контуры на изображении (один из способов).
im = array(Image.open("assets/img1.jpg").convert('L'))
figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')
show()


