import pygame

pygame.init()
WIDHT = 1366
HEIGHT = 768

screen = pygame.display.set_mode((WIDHT, HEIGHT))
text_font = pygame.font.SysFont('arial', 70)
pygame.display.set_caption('Konor szimulátor')
text_surf = text_font.render('SHUT THE FUCK UP NIGGA!!!', True, (0, 0, 0))
text_rect = text_surf.get_rect(center=(WIDHT / 2, HEIGHT / 2))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('white')
    screen.blit(text_surf, text_rect)
    pygame.display.update()

pygame.quit()
