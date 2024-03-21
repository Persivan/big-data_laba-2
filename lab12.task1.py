def explore(self, image):
    """
    Входной параметр:
    image - исследуемое изображение
    Выход:
    image - изображение с контурами пор
    area_c - отношение площади всех пор ко всей площади
    изображения (пористость)
    len(bad_conrours) - количество 'плохих' пор
    """
    image = np.copy(image)
    # дополнительная обработка шумов
    blured = cv2.GaussianBlur(image, (5, 5), 0)
    # конвертация BGR формата в формат HSV
    hsv = cv2.cvtColor(blured, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0, 0, 0])

    upper_black = np.array([120, 120, 120])
    # определяем маску для обнаружения контуров пор.
    # будут выделены поры в заданном диапозоне
    mask = cv2.inRange(hsv, lower_black, upper_black)
    # получаем массив конутров
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    good_contours = []
    bad_contours = []
    area_c = 0
    # находим поры, не превышающие нормативную площадь
    for contour in contours:
        # также подсчитываем общую площадь пор
        area_c += cv2.contourArea(contour)
        if self.mat_area - self.mat_area_std <= cv2.contourArea(contour) <= self.mat_area + self.mat_area_std:
            good_contours.append(contour)
        else:
            bad_contours.append(contour)
    area_c = area_c / (image.shape[0] * image.shape[1])
    # выделяем 'хорошие' поры зеленым цветом
    cv2.drawContours(image, good_contours, -1, (0, 255, 0), 3)
    # выделяем 'плохие' поры красным цветом
    cv2.drawContours(image, bad_contours, -1, (255, 0, 0), 3)
    return image, area_c, len(bad_contours)
