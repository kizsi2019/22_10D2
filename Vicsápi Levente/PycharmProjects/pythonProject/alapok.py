import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

background_color = WHITE

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Mygame')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                background_color = RED

            elif event.key == pygame.K_w:
                background_color = WHITE

            elif event.key == pygame.K_g:
                background_color = GREEN

    screen.fill(background_color)
    pygame.draw.circle(screen, BLACK, (300, 150), 50, 2)
    pygame.draw.rect(screen, RED, (10, 20, 100, 50), 5)
    pygame.draw.ellipse(screen, GREEN, (50, 50, 200, 75), 8)
    pygame.draw.polygon(screen, RED, [(120, 90), (120, 190), (200, 190)])
    pygame.display.update()

pygame.quit()