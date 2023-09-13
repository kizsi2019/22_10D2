import pygame
from settings import screen_width, screen_height, level_map
from aaaa import Level

#alap cuccok
#initelfossás valami aaa
pygame.init()
#ablak méret
height= 1550
width= 800
screen = pygame.display.set_mode((height, width))
#ablak név
pygame.display.set_caption('KURVA')


clock = pygame.time.Clock()

level = Level(level_map, screen)
#háttér
bg = pygame.image.load('img/morbin.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    level.run()

    pygame.display.update()
    clock.tick(60)

pygame.quit()

