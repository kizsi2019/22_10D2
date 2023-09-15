import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
ballon_surf = pygame.image.load('3.2/img/balloon.png').convert_alpha()
ballons_rect = []
for _ in range(5):
    ballon_rect = ballon_surf.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)))
    ballons_rect.append(ballon_rect)

score_font = pygame.font.SysFont('arial', 30)



running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                score += 1

            if event.key == pygame.K_DOWN and score > 0:
                score -= 1

    screen.fill(WHITE)

    score_surf = score_font.render('Pontszám: ' + str(score), True, (0, 0, 0))
    score_rect = score_surf.get_rect(topleft=(10, 10))

    for index, ballon_rect in enumerate(ballons_rect):
        screen.blit(ballon_surf, ballon_rect)

    screen.blit(score_surf, score_rect)
    pygame.display.update()

pygame.quit()
