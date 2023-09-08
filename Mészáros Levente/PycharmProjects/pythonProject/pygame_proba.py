import pygame

pygame.init()

WIDTH = 1280
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
