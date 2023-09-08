import pygame
import random
import shelve
High_score = 0
High_score_Test = 0
pygame.mixer.init()
Dead_sound = pygame.mixer.Sound("sound/Gameover.wav")
bgmusic = pygame.mixer.music.load("sound/Music.mp3")
Not_exited = True
while Not_exited:
    pygame.mixer.music.play(-1)
    coin_conter = 0
    coin_toch = True
    pygame.mixer.stop()
    Game_Running = True   
    BLUE = 0, 0 ,255
    WHITE = 255, 255, 255
    WIDTH = 1000
    HEIGHT = 700
    Font_Color = 0, 0, 0
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    default_entity_size = (100, 100)
    rec_pos_x = 100
    res_pos_y = 120
    Go_UP = False
    GO_DOWN = False
    Go_Left = False
    Go_Rigth = False
    points = 0
    clock = pygame.time.Clock()
    background_size = (1000, 1000)
    Font = pygame.font.Font(None, 60)
    Points_surf = Font.render("PONTOK", True, Font_Color)
    Points_rec = Points_surf.get_rect(center=(WIDTH - 250, HEIGHT - 650))
    Enemy_x = 600
    Enemy_y = 600
    Enemy_index = 0

    player_in_menu = False
    conter = 0
    bird_index =  0
    bloon_position_x = 100
    bloon_position_y = 100
    coin_surf = pygame.image.load('img/Coin.png').convert_alpha()
    coin_surf = pygame.transform.scale(coin_surf, default_entity_size)
    coin_rec = coin_surf.get_rect(center=(WIDTH - bloon_position_x, HEIGHT - bloon_position_y))
    
    
    while Game_Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_Running = False
                Not_exited = False
                player_in_menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:

                    Go_Left = True
                if event.key == pygame.K_d:

                    Go_Rigth = True
                if event.key == pygame.K_w:

                    Go_UP = True
                if event.key == pygame.K_s:

                    GO_DOWN = True
            if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:

                        Go_Left = False
                    if event.key == pygame.K_d:

                        Go_Rigth = False
                    if event.key == pygame.K_w:

                        Go_UP = False
                    if event.key == pygame.K_s:

                        GO_DOWN = False
        if Go_UP and rect.top > 0:
            res_pos_y -= 10
        if GO_DOWN and rect.bottom < HEIGHT:
            res_pos_y += 10
        if Go_Left and rect.left > 0:
            rec_pos_x -= 10
        if Go_Rigth and rect.right < WIDTH:
            rec_pos_x += 10
        
        background_image = pygame.image.load('img/clouds.png').convert_alpha()
        background_image = pygame.transform.scale(background_image, background_size)
        background_rect = background_image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        coin_rec = coin_surf.get_rect(center=(WIDTH - bloon_position_x, HEIGHT - bloon_position_y))
        screen.blit(background_image, background_rect)
        bird1 = pygame.image.load('img/PNG/frame-1.png').convert_alpha()
        bird1 = pygame.transform.scale(bird1, default_entity_size)
        bird2 = pygame.image.load('img/PNG/frame-2.png').convert_alpha()
        bird2 = pygame.transform.scale(bird2, default_entity_size)
        bird3 = pygame.image.load('img/PNG/frame-3.png').convert_alpha()
        bird3 = pygame.transform.scale(bird3, default_entity_size)
        bird4 = pygame.image.load('img/PNG/frame-4.png').convert_alpha()
        bird4 = pygame.transform.scale(bird4, default_entity_size)
        player_Bird = [bird1, bird2, bird3, bird4]
        conter += 1
        if conter % 3 == 0:
            bird_index += 1
            Enemy_index += 1
        if bird_index >= 3:
            bird_index = 0
            Enemy_index = 0
        Enemy1 = pygame.image.load('img/Enemy/MrCubeHead_red_1.png')
        Enemy1 = pygame.transform.scale(Enemy1, default_entity_size)
        Enemy2 = pygame.image.load('img/Enemy/MrCubeHead_red_2.png')
        Enemy2 = pygame.transform.scale(Enemy2, default_entity_size)
        Enemy3 = pygame.image.load('img/Enemy/MrCubeHead_red_3.png')
        Enemy3 = pygame.transform.scale(Enemy3, default_entity_size)
        Enemy4 = pygame.image.load('img/Enemy/MrCubeHead_red_4.png')
        Enemy4 = pygame.transform.scale(Enemy4, default_entity_size)
        Enemy_surf = [Enemy1, Enemy2, Enemy3, Enemy4]
        Pontnumber_surf = Font.render(str(points), True, Font_Color)
        Pontnumber_rec = Pontnumber_surf.get_rect(center=(WIDTH - 100, HEIGHT - 650))
        screen.blit(coin_surf, coin_rec)
        screen.blit(Points_surf, Points_rec)
        screen.blit(Pontnumber_surf, Pontnumber_rec)
        if coin_conter > 0:
            coin_conter -= 1
        if coin_conter == 0:
            coin_toch = True    
        Enemy_rect = pygame.Rect(Enemy_x ,Enemy_y, 100 ,100)
        screen.blit(Enemy_surf[Enemy_index], Enemy_rect)
        rect = pygame.Rect(rec_pos_x, res_pos_y, 100, 100,)
        screen.blit(player_Bird[bird_index], rect)
        if coin_rec.colliderect(rect) and coin_toch == True:
            bloon_position_x = random.randint(100, 900)
            bloon_position_y = random.randint(100, 600)
            points += 1
            print(points)
            coin_sound = pygame.mixer.Sound("sound/coin5.wav")
            coin_sound.play()
            coin_toch = False
            coin_conter = 10
        if rec_pos_x > Enemy_x:
            Enemy_x += 2
        elif Enemy_x > rec_pos_x:
            Enemy_x -= 2
        if res_pos_y > Enemy_y:
            Enemy_y += 2
        elif Enemy_y > res_pos_y:
            Enemy_y -= 2
        if rect.colliderect(Enemy_rect):
            player_in_menu = True
            Game_Running = False
            d = shelve.open('score.txt')
            High_score_Test = d['High_score']
            if points > High_score_Test:
                d['High_score'] = points
            High_score = d['High_score']    
            d.close()
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            Dead_sound.play()

        clock.tick(60)
        pygame.display.update()
    while player_in_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_Running = False
                Not_exited = False
                player_in_menu = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    player_in_menu = False

                    Game_Running = True
        Menu_surf = Font.render("Meghaltál LOL :)", True, Font_Color)
        Menu_rec = Menu_surf.get_rect(center=(WIDTH - 500, HEIGHT - 400))
        High_score_surf = Font.render("Legmagasabb Elért Pontszám:"  , True, Font_Color)
        High_score_rec = High_score_surf.get_rect(center=(WIDTH - 500, HEIGHT - 500))
        High_scoreNumber_surf = Font.render(str(High_score), True, Font_Color)
        High_scoreNumber_rec = High_scoreNumber_surf.get_rect(center=(WIDTH - 150, HEIGHT - 500))
        Tip_surf = Font.render(" Nyomj 'Space' Gombot Az Ujrakezdéshez", True, Font_Color)
        Tip_rec = Tip_surf.get_rect(center=(WIDTH - 500, HEIGHT - 300))
        screen.blit(High_score_surf, High_score_rec)
        screen.blit(Menu_surf, Menu_rec)
        screen.blit(Tip_surf ,Tip_rec)
        screen.blit(High_scoreNumber_surf, High_scoreNumber_rec)
        clock.tick(60)
        pygame.display.update()
        print("MENÓ")


pygame.quit