import pygam

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('colors')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(100845700)
    pygame.draw.circle(screen, blue, (300, 150), 20, 5)
    pygame.display.update()

pygame.quit()