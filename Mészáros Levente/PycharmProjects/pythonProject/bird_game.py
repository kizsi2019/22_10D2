import pygame

pygame.init()
WIDTH = 1280
HEIGHT = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SPEED = 5
score_font = pygame.font.SysFont('calibri', 30)
bird_surf = pygame.image.load('2.3/img/bird1.png').convert_alpha()
bird_surf_2 = pygame.image.load('2.4/bird2.png').convert_alpha()
bird_surf_3 = pygame.image.load('2.4/bird3.png').convert_alpha()
bird_surf_4 = pygame.image.load('2.4/bird4.png').convert_alpha()

bird_fw = [bird_surf, bird_surf_2, bird_surf_3, bird_surf_4]

bird_b_1 = pygame.image.load('2.3/img/bird1back.png').convert_alpha()
bird_b_2 = pygame.image.load('2.4/bird2back.png').convert_alpha()
bird_b_3 = pygame.image.load('2.4/bird3back.png').convert_alpha()
bird_b_4 = pygame.image.load('2.4/bird4back.png').convert_alpha()

balloon_surf = pygame.image.load('3.2/img/balloon.png').convert_alpha()
balloon_rect = balloon_surf.get_rect(center=(WIDTH - 50, HEIGHT / 2))

bird_bw = [bird_b_1, bird_b_2, bird_b_3, bird_b_4]

bird_index = 0

bird_x = 0
bird_y = HEIGHT / 2


clock = pygame.time.Clock()






running = True
bird_forward = True
collision = False
counter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)

    counter += 1
    if counter % 7 == 0:
        bird_index += 1

    if bird_index > len(bird_fw) - 1:
        bird_index = 0



    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and bird_rect.right < WIDTH:
        bird_forward = True
        bird_x += SPEED

    elif keys[pygame.K_LEFT] and bird_rect.left > 0:
        bird_forward = False
        bird_x -= SPEED

    if keys[pygame.K_UP] and bird_rect.top > 0:
        bird_y -= SPEED

    elif keys[pygame.K_DOWN] and bird_rect.bottom < HEIGHT:
        bird_y += SPEED


    if bird_forward:
        bird_surf = pygame.image.load('2.3/img/bird1.png').convert_alpha()
        bird_rect = bird_surf.get_rect(midleft=(bird_x, bird_y))
        screen.blit(bird_fw[bird_index], bird_rect)

    if not bird_forward:
        bird_b_1 = pygame.image.load('2.3/img/bird1back.png').convert_alpha()
        bird_rect = bird_b_1.get_rect(midleft=(bird_x, bird_y))
        screen.blit(bird_bw[bird_index], bird_rect)

    if balloon_rect.colliderect(bird_rect):
        collision = True

    if not collision:
        screen.blit(balloon_surf, balloon_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
