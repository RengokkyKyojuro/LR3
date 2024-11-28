import cv2
import numpy as np


# Функция для обработки клика мыши
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Получаем размер батча
        batch_size = int(input("Введите размер батча (30-80): "))

        # Проверяем допустимость размера батча
        if batch_size < 30 or batch_size > 80:
            print("Недопустимый размер батча. Пожалуйста, введите значение от 30 до 80.")
            return

        # Определяем границы батча
        half_size = batch_size // 2
        x_start = max(x - half_size, 0)
        x_end = min(x + half_size, img.shape[1])
        y_start = max(y - half_size, 0)
        y_end = min(y + half_size, img.shape[0])

        # Извлекаем батч
        batch = img[y_start:y_end, x_start:x_end]

        # Вычисляем среднюю интенсивность по каналам
        mean_intensity = cv2.mean(batch)

        # Выводим координаты и среднюю интенсивность
        print(f"Координаты точки: ({x}, {y})")
        print(f"Средняя интенсивность батча: B={mean_intensity[0]}, G={mean_intensity[1]}, R={mean_intensity[2]}")

        # Отображаем координаты на изображении
        cv2.putText(img, f"({x}, {y})", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow(winname1, img)


if __name__ == "__main__":
    winname1 = "ORIGINAL"
    img = cv2.imread('sky.png', cv2.IMREAD_COLOR)

    if img is None:
        print("Ошибка: Не удалось загрузить изображение. Проверьте путь к файлу.")
    else:
        cv2.namedWindow(winname1)
        cv2.moveWindow(winname1, 0, 0)
        cv2.imshow(winname1, img)

        # Устанавливаем обработчик событий для клика мыши
        cv2.setMouseCallback(winname1, click_event)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
