import pygame

pygame.init()

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("ZmeiKa")

icon_game = pygame.image.load('DZ_9/icon/icon.png').convert_alpha()
pygame.display.set_icon(icon_game)

img_fon = pygame.image.load('DZ_9/img_fon/fon.png').convert_alpha()

apple = pygame.image.load('DZ_9/images/aple.png').convert_alpha()

running = True
while running:

    window.blit(img_fon, (0, 0))

    window.blit(apple, (330, 200))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
