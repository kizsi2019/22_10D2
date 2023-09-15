import pygame
import time

pygame.init()
time_start = time.time()


WIDTH, HEIGHT = 1280, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bird_surface_1 = pygame.image.load('2.3/img/bird1.png')
bird_surface_2 = pygame.image.load('2.4/bird2.png')
bird_surface_3 = pygame.image.load('2.4/bird3.png')
bird_surface_4 = pygame.image.load('2.4/bird4.png')
bird_surf = [bird_surface_1, bird_surface_2, bird_surface_3, bird_surface_4]

bird_index = 0

clock = pygame.time.Clock()
bird_rect = bird_surf[bird_index].get_rect(midleft=(0, HEIGHT / 2))
bird_speed = 5
bird_forward = True
font_color = (255, 255, 255)


game_font_1 = pygame.font.SysFont('arial', 60)
game_font_2 = pygame.font.SysFont('Calibri', 60)
text_surf = game_font_1.render('Game', True, font_color)
text_rect = text_surf.get_rect(topleft=(10, 5))




counter = 0
running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            score += 1

    game_time = str(int(time.time() - time_start))
    time_surf = game_font_1.render('Sec: ' + game_time, True, font_color)
    time_rect = time_surf.get_rect(topright=(WIDTH - 10, 0))

    score_surf = game_font_2.render('Score: ' + str(score), True, font_color)
    score_rect = score_surf.get_rect(topleft=(10, 180))

    screen.fill((140, 137, 246))
    screen.blit(score_surf, score_rect)
    screen.blit(time_surf, time_rect)
    screen.blit(text_surf, text_rect)

    counter += 1
    if counter % 7 == 0:
        bird_index += 1


    if bird_index > len(bird_surf) - 1:
        bird_index = 0

    if bird_rect.right < WIDTH and bird_forward:
        bird_rect.left += bird_speed

    screen.blit(bird_surf[bird_index], bird_rect)
    pygame.display.update()
    clock.tick(60)


pygame.quit()