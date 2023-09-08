import pygame

width, height = 640, 480
blue = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.draw.rect(screen, blue, ([10, 20, 100, 50]))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()