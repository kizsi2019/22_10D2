import pygame

#Setup
width, height = 640, 480
blue = (0, 0, 255)
black = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("FixSys", 12)

#Load
img = pygame.image

#Loop
size = 1
run = True
while run:
    x, y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.circle(screen, (128, 128, 128), (x, y), size)
        if pygame.mouse.get_pressed() == (0, 1, 0):
            size = size + 1
        if pygame.mouse.get_pressed() == (0, 0, 1):
            pygame.draw.circle(screen, (0, 0, 0), (x, y), size)

    pygame.display.update()
pygame.quit()