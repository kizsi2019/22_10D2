import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pontrendszeres Játék")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

score = 0

clock = pygame.time.Clock()
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos[0] = x

    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += 10
        else:
            enemy_list.pop(idx)
            score += 1

    if len(enemy_list) < 3:
        x = random.randint(0, WIDTH-enemy_size)
        y = 0
        enemy_list.append([x, y])


    pygame.draw.ellipse(window, RED, (player_pos[0], player_pos[1], player_size, player_size))

    for enemy_pos in enemy_list:
        pygame.draw.rect(window, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    font = pygame.font.Font(None, 36)
    text = font.render("Pontszám: " + str(score), True, RED)
    window.blit(text, (20, 20))

    for enemy_pos in enemy_list:
        if enemy_pos[1] >= player_pos[1] and enemy_pos[1] <= player_pos[1] + player_size:
            if enemy_pos[0] >= player_pos[0] and enemy_pos[0] <= player_pos[0] + player_size or \
                    player_pos[0] >= enemy_pos[0] and player_pos[0] <= enemy_pos[0] + enemy_size:
                game_over = False

    pygame.display.update()

    clock.tick(60)

pygame.quit()
