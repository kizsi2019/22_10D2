import pygame

import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tennis Game")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles
paddle_width = 10
paddle_height = 60
paddle_speed = 5
paddle1_pos = screen_height // 2 - paddle_height // 2
paddle2_pos = screen_height // 2 - paddle_height // 2

# Set up the ball
ball_radius = 10
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed_x = 3 * random.choice([-1, 1])
ball_speed_y = 3 * random.choice([-1, 1])

# Set up the score
score1 = 0
score2 = 0
font = pygame.font.Font(None, 50)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and paddle2_pos > 0:
        paddle2_pos -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_pos < screen_height - paddle_height:
        paddle2_pos += paddle_speed
    if keys[pygame.K_w] and paddle1_pos > 0:
        paddle1_pos -= paddle_speed
    if keys[pygame.K_s] and paddle1_pos < screen_height - paddle_height:
        paddle1_pos += paddle_speed

    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with paddles
    if ball_x <= paddle_width and paddle1_pos <= ball_y <= paddle1_pos + paddle_height:
        ball_speed_x = abs(ball_speed_x)
    if ball_x >= screen_width - paddle_width - ball_radius and paddle2_pos <= ball_y <= paddle2_pos + paddle_height:
        ball_speed_x = -abs(ball_speed_x)

    # Ball collision with walls
    if ball_y <= 0 or ball_y >= screen_height - ball_radius:
        ball_speed_y = -ball_speed_y

    # Ball out of bounds
    if ball_x < 0:
        score2 += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x = 3 * random.choice([-1, 1])
        ball_speed_y = 3 * random.choice([-1, 1])
    elif ball_x > screen_width:
        score1 += 1
        ball_x = screen_width // 2
        ball_y = screen_height // 2
        ball_speed_x = 3 * random.choice([-1, 1])
        ball_speed_y = 3 * random.choice([-1, 1])

    # Load the background image
    background_image = pygame.image.load("image.jpg")

    # Draw the paddle
    pygame.draw.rect(screen, WHITE, (0, paddle1_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (screen_width - paddle_width, paddle2_pos, paddle_width, paddle_height))

    # Draw the ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), ball_radius)
    # Draw the score
    score_text = font.render(str(score1) + " : " + str(score2), True, WHITE)
    screen.blit(score_text, (screen_width // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)
