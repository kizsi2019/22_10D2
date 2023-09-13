import pygame
import random



pygame.init()
WIDTH = 1280
HEIGHT = 600
WHITE = (255, 255, 255)
BALLOON_SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Balloons in crosshair')
SPEED = 5

bg_surf = pygame.image.load('4.1/img/sky.png').convert_alpha()
bg_surf = pygame.transform.scale(bg_surf, (WIDTH, HEIGHT))
bg_rect = bg_surf.get_rect(bottomleft=(0, HEIGHT))

balloon_surf = pygame.image.load('3.2/img/balloon.png').convert_alpha()
balloons_rect = []
balloons_timer = pygame.USEREVENT + 1
pygame.time.set_timer(balloons_timer, 1000)

crossshair_surf = pygame.image.load('3.3/img/crosshair.png').convert_alpha()
crossshair_surf = pygame.transform.rotozoom(crossshair_surf, 0, 0.7)
crossshair_rect = crossshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))




clock = pygame.time.Clock()

running = True
bird_forward = True
counter = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crossshair_rect = crossshair_surf.get_rect(center=event.pos)
        if event.type == balloons_timer:
            balloons_rect.append(balloon_surf.get_rect(center=(random.randint(50, HEIGHT - 50), HEIGHT + 50)))

    screen.blit(bg_surf, bg_rect)

    for index, balloon_rect in enumerate(balloons_rect):
        balloons_rect[index].top -= BALLOON_SPEED
        move_y = random.randint(0, 3)
        if move_y == 0:
            balloons_rect[index].left -= 2
        else:
            balloons_rect[index].left += 2



        screen.blit(balloon_surf, balloon_rect)


    screen.blit(crossshair_surf, crossshair_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
