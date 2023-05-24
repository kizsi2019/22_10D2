import pygame
import random

pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("jó játék")


class Player:
    def __init__(self):
        self.x = width // 2
        self.y = height - 50
        self.width = 50
        self.height = 50
        self.speed = 5

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed

    def draw(self):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))

class Enemy:
    def __init__(self):
        self.x = random.randint(0, width - 50)
        self.y = random.randint(50, 150)
        self.width = 50
        self.height = 50
        self.speed = 2

    def move(self):
        self.y += self.speed
        if self.y > height:
            self.x = random.randint(0, width - 50)
            self.y = random.randint(50, 150)

    def draw(self):
        pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))

player = Player()
enemies = [Enemy() for _ in range(10)]
clock = pygame.time.Clock()

running = True
while running:
    window.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()

    player.draw()

    for enemy in enemies:
        enemy.move()
        enemy.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
