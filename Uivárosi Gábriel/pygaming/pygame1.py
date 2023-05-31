import pygame
Game_Running = True
BLUE = 0, 0 ,255
WHITE = 255, 255, 255
WIDTH = 1000
HEIGHT = 700
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rec_pos_x = 100
res_pos_y = 120
Go_UP = False
GO_DOWN = False
Go_Left = False
Go_Rigth = False
clock = pygame.time.Clock()
conter = 0
bird_index =  0
coin_surf = pygame.image.load('img/Coin.png').convert_alpha()
coin_rec = coin_surf.get_rect(center=(WIDTH - 100, HEIGHT / 2))
while Game_Running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:

                Go_Left = True
            if event.key == pygame.K_a:

                Go_Rigth = True
            if event.key == pygame.K_w:

                Go_UP = True
            if event.key == pygame.K_s:

                GO_DOWN = True
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:

                    Go_Left = False
                if event.key == pygame.K_a:

                    Go_Rigth = False
                if event.key == pygame.K_w:

                    Go_UP = False
                if event.key == pygame.K_s:

                    GO_DOWN = False
    if Go_UP:
        res_pos_y -= 10
    if GO_DOWN:
        res_pos_y += 10
    if Go_Left:

        rec_pos_x += 10
    if Go_Rigth:
        rec_pos_x -= 10
    screen.fill(WHITE)
    bird1 = pygame.image.load('img/PNG/frame-1.png').convert_alpha()
    bird2 = pygame.image.load('img/PNG/frame-2.png').convert_alpha()
    bird3 = pygame.image.load('img/PNG/frame-3.png').convert_alpha()
    bird4 = pygame.image.load('img/PNG/frame-4.png').convert_alpha()
    player_Bird = [bird1, bird2, bird3, bird4]
    conter += 1
    if conter % 3 == 0:
        bird_index += 1
    if bird_index >= 3:
        bird_index = 0
    screen.blit(coin_surf, coin_rec)
    rect = pygame.Rect( rec_pos_x, res_pos_y, 10, 10,)
    screen.blit(player_Bird[bird_index], rect)
    clock.tick(60)
    pygame.display.update()
pygame.quit