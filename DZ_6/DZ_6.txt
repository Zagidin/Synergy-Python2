# Импортируем библиотеку 
import pygame 

# Начала создания окна обязательно нужно указать
pygame.init()

# Задаём название для окна
pygame.display.set_caption("Pygame-знакомство")

# Задаём размеры для окна
window = pygame.display.set_mode((640, 540))

# Загружаем нашего персонажа
persona_dino = pygame.image.load('DZ_6/DinoZagi.png')

# Его положение в нашем окне
dino_x, dino_y = 100, 100

# Создаём цикл, чтоб окно не закрывалось
ranning = True
while ranning:
    for event in pygame.event.get():
        # Отслеживаем кнопку выхода
        if event.type == pygame.QUIT:
            ranning = False

    # Очистка экрана (Обязательно) 255x3 это белый цвет
    window.fill((255, 255, 255))

    # Выводим на экран нашего персонажа
    window.blit(persona_dino, (dino_x, dino_y))

    # Обновляем наше окно
    pygame.display.flip()

# конец цикла для init обязательно нужно указать
pygame.quit()
