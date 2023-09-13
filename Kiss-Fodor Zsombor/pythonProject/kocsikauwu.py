import pygame

WIDTH = 1500
HEIGHT = 800
SPEEDX = 0
SPEEDY = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird = pygame.image.load('img/vzgvm9l5ejh91.jpg').convert_alpha()
bird_x = 120
bird_y = HEIGHT - 150

nishiki_place = bird.get_rect(center=(bird_x, bird_y))
screen.blit(bird, nishiki_place)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and bird_rect.right <= WIDTH:
        bird_x += SPEEDX
        bird_y += SPEEDY
    elif keys[pygame.K_UP] and bird_rect.left >= 0:
        bird_x += SPEEDX
        bird_y -= SPEEDY
    elif keys[pygame.K_LEFT]:
        SPEEDX -= 1
    elif keys[pygame.K_RIGHT]:
        SPEEDX += 1


    screen.fill((140, 137, 246))
    bird_rect = bird.get_rect(center=(bird_x, bird_y))
    screen.blit(bird, bird_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
