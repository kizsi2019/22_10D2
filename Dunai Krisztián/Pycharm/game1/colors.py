import pygame

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)
  
pygame.init()
screen = pygame.display.set_mode((640, 240))
background = GRAY
  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
screen.fill(background)
  
pygame.draw.rect(screen, BLUE, (10, 20, 100, 50))
pygame.draw.rect(screen, BLUE, (120, 20, 100, 50), 5, 10)
pygame.draw.ellipse(screen, RED, (10, 90, 100, 50))
pygame.draw.polygon(screen, GREEN, [(120, 90), (120, 190), (200, 150)])
pygame.draw.circle(screen, BLACK, (300, 100), 20)

pygame.display.update()áááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááááá
pygame.quit()
