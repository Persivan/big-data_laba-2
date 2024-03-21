from PIL import Image
from pylab import *

# Рисование на изображении
im = array(Image.open("assets/img1.jpg"))
imshow(im)
x = [100, 100, 400, 400]
y = [200, 500, 200, 500]
# axis('off')

# Выбираем тип линии
# plot(x, y, 'r*')
# plot(x[:2], y[:2])
# plot(x,y)
# plot(x,y, "go-")
# plot(x,y, "ks:")

title('Plotting: "img1.jpg"')
show()

