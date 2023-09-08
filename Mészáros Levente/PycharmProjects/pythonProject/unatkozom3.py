import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 600
SPEED = 13
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bird_surf1 = pygame.image.load('3.2/img/bird1.png').convert_alpha()
bird_surf2 = pygame.image.load('3.2/img/bird2.png').convert_alpha()
bird_surf3 = pygame.image.load('3.2/img/bird3.png').convert_alpha()
bird_surf4 = pygame.image.load('3.2/img/bird4.png').convert_alpha()

bird_b_1 = pygame.image.load('3.2/img/bird1back.png').convert_alpha()
bird_b_2 = pygame.image.load('3.2/img/bird2back.png').convert_alpha()
bird_b_3 = pygame.image.load('3.2/img/bird3back.png').convert_alpha()
bird_b_4 = pygame.image.load('3.2/img/bird4back.png').convert_alpha()

bird_rect = bird_surf1.get_rect(center=(WIDTH / 2, HEIGHT / 2))

bird_fw = [bird_surf1, bird_surf2, bird_surf3, bird_surf4]
bird_b = [bird_b_1, bird_b_2, bird_b_3, bird_b_4]

running = True
index = 0
counter = 0
forward = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    counter += 1
    if counter % 7 == 0:
        index += 1

    if index > len(bird_fw) - 1:
        index = 0

    screen.fill('white')

    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT] and bird_rect.right < WIDTH:
        bird_rect.right += SPEED
        forward = True

    elif key[pygame.K_LEFT] and bird_rect.left > 0:
        bird_rect.left -= SPEED
        forward = False

    if key[pygame.K_UP] and bird_rect.top > 0:
        bird_rect.top -= SPEED

    elif key[pygame.K_DOWN] and bird_rect.bottom < HEIGHT:
        bird_rect.bottom += SPEED

    if forward:
        screen.blit(bird_fw[index], bird_rect)

    else:
        screen.blit(bird_b[index], bird_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
