from PIL import Image

# Закраска (заливка) части и всего изображения заданным цветом.
# img = Image.open("assets/img1.jpg")
# img.paste( (255, 0, 0), (0, 0, 100, 100) )
# img.show()

# Залейте все изображение зеленым цветом.
img = Image.open("assets/img1.jpg")
img.paste( (0, 128, 0), img.getbbox() )
img.show()