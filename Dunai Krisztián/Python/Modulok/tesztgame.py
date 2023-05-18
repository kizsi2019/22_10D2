import pygame
from pygame.locals import *

# Ablak méretei
WIDTH = 640
HEIGHT = 480

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Játékosok adatai
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 60
PLAYER_SPEED = 5

# Labda adatai
BALL_RADIUS = 10
BALL_X_SPEED = 3
BALL_Y_SPEED = 3

# Pygame inicializálása
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong")

clock = pygame.time.Clock()

# Játékosok létrehozása
player1 = pygame.Rect(50, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)
player2 = pygame.Rect(WIDTH - 50 - PLAYER_WIDTH, HEIGHT // 2 - PLAYER_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)

# Labda létrehozása
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
ball_x_speed = BALL_X_SPEED
ball_y_speed = BALL_Y_SPEED

# Játék ciklus
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Játékosok mozgatása
    if keys[K_w] and player1.top > 0:
        player1.y -= PLAYER_SPEED
    if keys[K_s] and player1.bottom < HEIGHT:
        player1.y += PLAYER_SPEED
    if keys[K_UP] and player2.top > 0:
        player2.y -= PLAYER_SPEED
    if keys[K_DOWN] and player2.bottom < HEIGHT:
        player2.y += PLAYER_SPEED

    # Labda mozgatása
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    # Labda ütközés a falakkal
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_y_speed *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_x_speed *= -1

    # Labda ütközés a játékosokkal
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_x_speed *= -1

    # Háttér törlése
    screen.fill(BLACK)

    # Játékosok kirajzolása
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)

    # Labda kirajzolása
    pygame.draw.ellipse(screen, WHITE, ball)

    # Ablak frissítése
    pygame.display.flip()
    clock.tick(60)

# Pygame leállítása
pygame.quit()