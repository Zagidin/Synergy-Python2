import pygame

pygame.init()

screen = pygame.display.set_mode((700, 550))
pygame.display.set_caption("Игра Змейка")
# Иконка для окна
icon = pygame.image.load('DZ_7/images/ico.png')
pygame.display.set_icon(icon)

square = pygame.Surface((50, 50))
square.fill('Blue')

myfont = pygame.font.Font('тут фонт', 40)
text_surface = myfont.rander('ZagaPride', True, 'Blak')

flag = True
while flag:

    # Цвет фона из color_picker
    screen.fill((181, 158, 155))

    screen.blit(square, (300, 12))

    pygame.draw.circle(square, 'Red', (0, 1), 5)

    screen.blit(text_surface, (400, 500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_q:
        #         fill = (155, 155, 155)
        #         screen.fill(fill)
        
    # Обновление окна
    pygame.display.update()

pygame.quit()