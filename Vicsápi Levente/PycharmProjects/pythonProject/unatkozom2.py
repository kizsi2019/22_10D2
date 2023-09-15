import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 600
SPEED = 10
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bird_surf = pygame.image.load('3.3/img/bird1.png').convert_alpha()
bird_surf2 = pygame.image.load('3.3/img/bird2.png').convert_alpha()
bird_surf3 = pygame.image.load('3.3/img/bird3.png').convert_alpha()
bird_surf4 = pygame.image.load('3.3/img/bird4.png').convert_alpha()

bird_surf_b = pygame.image.load('3.3/img/bird1back.png').convert_alpha()
bird_surf_b2 = pygame.image.load('3.3/img/bird2back.png').convert_alpha()
bird_surf_b3 = pygame.image.load('3.3/img/bird3back.png').convert_alpha()
bird_surf_b4 = pygame.image.load('3.3/img/bird4back.png').convert_alpha()

GAME_FONT = pygame.font.SysFont('arial', 150)
dosa_surf = GAME_FONT.render('INTERNETKÁBEL', True, (0, 0, 0))
dosa_rect = dosa_surf.get_rect(midtop=(WIDTH / 2, 40))

bird_rect = bird_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

bird_fw = [bird_surf, bird_surf2, bird_surf3, bird_surf4]
bird_b = [bird_surf_b, bird_surf_b2, bird_surf_b3, bird_surf_b4]

counter = 0
index = 0
running = True
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

    if index > len(bird_b) - 1:
        index = 0

    screen.fill((255, 255, 255))
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

    if not forward:
        screen.blit(bird_b[index], bird_rect)

    screen.blit(dosa_surf, dosa_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
