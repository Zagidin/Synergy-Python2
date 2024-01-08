import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))
pygame.display.set_caption("ZmeiKaZag")

icon_game = pygame.image.load('DZ_9/icon/icon.png').convert_alpha()
pygame.display.set_icon(icon_game)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()