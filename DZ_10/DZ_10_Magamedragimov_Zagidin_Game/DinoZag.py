import pygame

pygame.init()

time_clock = pygame.time.Clock()

window = pygame.display.set_mode((1155, 650))
pygame.display.set_caption('Dino-Zagi')

icon_game = pygame.image.load('game_Dino-Zagi/dino_icon.png').convert_alpha()
pygame.display.set_icon(icon_game)

# Музыка фоновая
music_fon_game = pygame.mixer.Sound('sound_game/game_fon_sound.mp3')
music_fon_game.play()

fon_game = pygame.image.load('fon_game/game_pole.png').convert_alpha()

# Позиция дино
dino_x, dino_y = 50, 323
# Движение дино
dino_run = [
    pygame.image.load('dino_zag_player_right/dino_run1.png').convert_alpha(),
    pygame.image.load('dino_zag_player_right/dino_run2.png').convert_alpha()
]

dino_run_left = [
    pygame.image.load('dino_zag_player_left/dino_run1 (1).png').convert_alpha(),
    pygame.image.load('dino_zag_player_left/dino_run2 (1).png').convert_alpha()
]

dino_run_down = [
    pygame.image.load('dino_down/dino_down1.png').convert_alpha(),
    pygame.image.load('dino_down/dino_down2.png').convert_alpha()
]
dino_active = 0

fly_boo_x = 1157
fly_dino_boo = [
    pygame.image.load('dino_fly/fly1.png').convert_alpha(),
    pygame.image.load('dino_fly/fly2.png').convert_alpha()
]

fly_active = 0

fon_x = 0

# Дино прыжок
prig_dino = False
jump_count = 10

# Дино движение
dino_speed = 20 

#
fly_boo_spisok = []
# Таймер появления
fly_timer = pygame.USEREVENT + 1
pygame.time.set_timer(fly_timer, 2200)

running_game = True
while running_game:

    keys_pressed = pygame.key.get_pressed()
    
    # Фон игровое поле
    window.blit(fon_game, (fon_x, 0))
    window.blit(fon_game, (fon_x + 1155, 0))

    fon_x -= 10
    if fon_x == -1160:
        fon_x = 0

    # Персонаж дино   
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        window.blit(dino_run_left[dino_active], (dino_x, dino_y))
    elif keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        window.blit(dino_run_down[dino_active], (dino_x, dino_y + 30))
    else:
        window.blit(dino_run[dino_active], (dino_x, dino_y))

    if dino_active == 1:
        dino_active = 0
    else:
        dino_active += 1

    # Прыжок
    if not prig_dino:
        if keys_pressed[pygame.K_SPACE] or keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w]:
            prig_dino = True
    else:
        if jump_count >= -10:
            if jump_count > 0:
                dino_y -= (jump_count ** 2) / 2
            else:
                dino_y += (jump_count ** 2) / 2
            jump_count -= 1

        else:
            prig_dino = False
            jump_count = 10

    # Двигать
    if keys_pressed[pygame.K_RIGHT] and dino_x < 1000 or keys_pressed[pygame.K_d] and dino_x < 1000:
        dino_x += dino_speed
    elif keys_pressed[pygame.K_LEFT] and dino_x > 50 or keys_pressed[pygame.K_a] and dino_x > 50:
        dino_x -= dino_speed
    
    # Птица настройки
    if fly_active == 1:
        fly_active = 0
    else:
        fly_active += 1
    
    # Прикосновение
    dino_rect_left = dino_run_left[0].get_rect(topleft=(dino_x, dino_y))
    dino_rect_down = dino_run_left[0].get_rect(topleft=(dino_x, dino_y))
    
    if fly_boo_spisok:
        for el in fly_boo_spisok:
            window.blit(fly_dino_boo[fly_active], el)
            el.x -= 30

        if dino_rect_left.colliderect(el) or dino_rect_down.colliderect(el):
            print("ВЫ СТОЛКНУЛИСЬ!")
    

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
        if event.type == fly_timer:
            fly_boo_spisok.append(fly_dino_boo[fly_active].get_rect(topleft=(1157, 250)))

    time_clock.tick(13)

pygame.quit()
