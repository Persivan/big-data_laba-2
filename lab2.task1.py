# Просто открыть
# from PIL import Image
# img = Image.open("assets/img1.jpg")
# img.show()


# Открыть в бинарном режиме
# img = Image.open("assets/img1.jpg")
# img = img.convert("L")
# img.show()


# Вместо указания пути к файлу можно передать файловый объект, открытый в бинарном режиме
# Открываем файл в бинарном режиме
# f = open("assets/img1.jpg", "rb")
# # Передаем объект файла
# img = Image.open(f)
# # выводим переданное изображение на экран:
# img.show()
# f.close() # Закрываем файл


# Загрузка изображения из строки. Модуль BytesIO
# f = open("assets/img1.jpg", "rb")
# # Сохраните изображение в переменной:
# i = f.read()
# f.close() # Закрываем файл
# # Подключаем модуль BytesIO:
# try:
#     from BytesIO import BytesIO ## for Python 2
# except ImportError:
#     from io import BytesIO ## for Python 3
# from PIL import Image
#
# # Передаем объект:
# img = Image.open(BytesIO(i))
# # выводим изображение на экран:
# img.show()