import pygame

pygame.init()
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
BG_COLOR = (140, 137, 246)
clock = pygame.time.Clock()
BIRD_SPEED = 5
rect = pygame.Rect(50, 60, 200, 80)
bird_surf = pygame.image.load('img/bird1.png').convert_alpha()
bird_x = 0
bird_y = 200


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BG_COLOR)
    if bird_x < WIDTH-120:
        bird_x += BIRD_SPEED
    screen.blit(bird_surf, (bird_x, bird_y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()