import pygame

pygame.init()

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("ZmeiKa")

icon_game = pygame.image.load('DZ_9/icon/icon.png').convert_alpha()
pygame.display.set_icon(icon_game)

running = True
while running:



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
