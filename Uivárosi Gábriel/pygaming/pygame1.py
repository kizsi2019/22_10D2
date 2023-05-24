import pygame
Game_Running = True
BLUE = 0, 0 ,255
WHITE = 255, 255, 255
pygame.init()
screen = pygame.display.set_mode((800, 500))
rec_pos_x = 100
res_pos_y = 120
Go_UP = False
GO_DOWN = False
Go_Left = False
Go_Rigth = False
clock = pygame.time.Clock()
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

    rect = pygame.Rect(rec_pos_x, res_pos_y, 50, 50,)
    pygame.draw.rect(screen, BLUE, rect )
    clock.tick(60)
    pygame.display.update()