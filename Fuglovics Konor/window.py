import pygame

width, height = 640, 480
blue = (0, 0, 255)
black = (0, 0, 0)


pygame.init()
screen = pygame.display.set_mode((width, height))


run = True
while run:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.circle(screen, (128, 128, 128), (x, y), 1)

    pygame.display.update()

pygame.quit()