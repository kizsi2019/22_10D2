import pygame
import random

pygame.init()
WIDTH = 1280
HEIGHT = 600
WHITE = (255, 255, 255)
GAME_TIME = 8000

screen = pygame.display.set_mode((WIDTH, HEIGHT))
crosshair_surf = pygame.image.load('4.1/img/crosshair.png').convert_alpha()
crosshair_rect = crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

bg_surf = pygame.image.load('4.1/img/sky.png').convert_alpha()
bg_surf = pygame.transform.scale(bg_surf, (WIDTH, HEIGHT))
bg_rect = bg_surf.get_rect(bottomleft=(0, HEIGHT))

score_font = pygame.font.SysFont('arial', 30)

BALLOON_SPEED = 5

title_surf = score_font.render('BALLOONS IN CROSSHAIR', True, WHITE)
title_rect = title_surf.get_rect(center=(WIDTH / 2, 200))

run_surf = score_font.render('Press space to start', True, WHITE)
run_rect = run_surf.get_rect(center=(WIDTH / 2, HEIGHT - 150))



balloon_surf = pygame.image.load('4.1/img/balloon.png').convert_alpha()
balloons_rect = []
balloons_timer = pygame.USEREVENT
pygame.time.set_timer(balloons_timer, 1000)

clock = pygame.time.Clock()
game_active = False
start_time = pygame.time.get_ticks()
score = 0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=(event.pos))

        if event.type == balloons_timer:
            balloons_rect.append(balloon_surf.get_rect(center=(random.randint(50, WIDTH - 50), HEIGHT + 50)))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        game_active = True
        score = 0
        balloons_rect = []
        start_time = pygame.time.get_ticks()

    elif keys[pygame.K_ESCAPE]:
        game_active = False


    screen.blit(bg_surf, bg_rect)
    if game_active:
        score_surf = score_font.render('score: ' + str(score), True, WHITE)
        score_rect = score_surf.get_rect(topleft=(10, 10))

        for balloon_rect in balloons_rect:
            screen.blit(balloon_surf, balloon_rect)

        for index, balloon_rect in enumerate(balloons_rect):
            if balloon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(num_buttons=3)[0]:
                del balloons_rect[index]
                score += 1

            elif balloons_rect[index].top <= -10:
                del balloons_rect[index]

            else:
                balloons_rect[index].top -= BALLOON_SPEED
                move_y = random.randint(0, 3)
                if move_y == 0:
                    balloons_rect[index].left -= 2
                else:
                    balloons_rect[index].left += 2

        time_left = int((start_time + GAME_TIME - pygame.time.get_ticks()) / 1000)
        time_left_surf = score_font.render('time left: ' + str(time_left), True, WHITE)
        time_left_rect = time_left_surf.get_rect(topright=(WIDTH - 10, 10))
        screen.blit(time_left_surf, time_left_rect)

        if time_left == 0:
            game_active = False




        screen.blit(score_surf, score_rect)
        screen.blit(crosshair_surf, crosshair_rect)

    else:
        screen.blit(title_surf, title_rect)
        screen.blit(balloon_surf, balloon_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
        screen.blit(crosshair_surf, crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
        screen.blit(run_surf, run_rect)

        if score:
            final_score_surf = score_font.render('SCORE: ' + str(score), True, WHITE)
            final_score_rect = final_score_surf.get_rect(center=(WIDTH / 2, HEIGHT - 220))
            screen.blit(final_score_surf, final_score_rect)

    pygame.display.update()
    clock.tick(60)
pygame.quit()
