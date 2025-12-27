import pygame
import sys
import os

pygame.init()

# ==============================
# Создаем окно в полноэкранном режиме.
# (0, 0) означает: взять текущее разрешение экрана автоматически
# ==============================

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Просмотр изображений")

# Получаем ширину и высоту экрана
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

# ==============================
# Загружаем список изображений из папки emotions
# ==============================

IMAGE_FOLDER = "emotions"

images = [
    os.path.join(IMAGE_FOLDER, file)
    for file in os.listdir(IMAGE_FOLDER)
    if file.lower().endswith((".png", ".jpg", ".jpeg"))
]

# Проверка: если изображений нет — завершаем программу
if not images:
    print("В папке images нет изображений")
    pygame.quit()
    sys.exit()

current_index = 0

# ==============================
# МЕТОДИЧЕСКИЙ КОММЕНТАРИЙ
# Функция загрузки изображения:
# - загружает картинку
# - масштабирует под размер экрана
# ==============================

def load_image(index):
    image = pygame.image.load(images[index])
    image = pygame.transform.scale(image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    return image

current_image = load_image(current_index)

clock = pygame.time.Clock()
running = True

# ==============================
# МЕТОДИЧЕСКИЙ КОММЕНТАРИЙ
# Главный цикл программы:
# работает до тех пор, пока running == True
# ==============================

while running:
    clock.tick(60)  # Ограничение FPS (60 кадров в секунду)

    for event in pygame.event.get():

        # ==============================
        # Закрытие окна
        # ==============================
        if event.type == pygame.QUIT:
            running = False

        # ==============================
        # Обработка нажатий клавиш
        # ==============================
        if event.type == pygame.KEYDOWN:

            # ESC — выход из программы
            if event.key == pygame.K_ESCAPE:
                running = False

            # Стрелка вправо — следующая картинка
            if event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(images)
                current_image = load_image(current_index)

            # Стрелка влево — предыдущая картинка
            if event.key == pygame.K_LEFT:
                current_index = (current_index - 1) % len(images)
                current_image = load_image(current_index)

    # ==============================
    # Отрисовка изображения
    # ==============================
    screen.blit(current_image, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
