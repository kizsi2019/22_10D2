import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Kígyó játék")

background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

food_img = pygame.image.load("food.png")
food_img = pygame.transform.scale(food_img, (20, 20))

pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.set_volume(0.5)  # Állítsd a hangerőt itt (0.0 - 1.0 között)

mute_icon = pygame.image.load("mute_icon.png")
mute_icon = pygame.transform.scale(mute_icon, (20, 20))

clock = pygame.time.Clock()

snake_block_size = 20
snake_speed = 10

font_style = pygame.font.SysFont(None, 30)
score_font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x, y, snake_block_size, snake_block_size])

def display_message(msg, color, y_offset=0):
    message = font_style.render(msg, True, color)
    screen.blit(message, (screen_width / 2 - message.get_width() / 2, screen_height / 2 - message.get_height() / 2 + y_offset))

def game_menu():
    menu_running = True

    while menu_running:
        screen.blit(background_img, (0, 0))
        display_message("Snake Játék", (255, 255, 255))

        button_width = 200
        button_height = 50
        button_x = (screen_width - button_width) / 2
        button_y = (screen_height - button_height) / 2

        pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_width, button_height))
        display_message("Játék megkezdése", (255, 255, 255))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x <= mouse_x <= button_x + button_width and button_y <= mouse_y <= button_y + button_height:
                    pygame.mixer.music.play(-1)  # Hanglejátszás indítása
                    game_loop()


def game_loop():
    game_over = False
    game_pause = False
    is_muted = False

    x = screen_width / 2
    y = screen_height / 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, screen_width - snake_block_size) / snake_block_size) * snake_block_size
    food_y = round(random.randrange(0, screen_height - snake_block_size) / snake_block_size) * snake_block_size

    score = 0
    level = 1

    while not game_over:
        while game_pause:
            screen.blit(background_img, (0, 0))
            display_message("Szünet", (255, 0, 0), y_offset=-50)
            display_message("Folytatás - Space", (255, 255, 255))
            display_message("Kilépés - ESC", (255, 255, 255), y_offset=50)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    game_over = True
                    game_pause = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_pause = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        game_over = True
                        game_pause = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block_size
                    x_change = 0
                elif event.key == pygame.K_ESCAPE:
                    game_pause = True

        x += x_change
        y += y_change

        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_over = True

        screen.blit(background_img, (0, 0))
        screen.blit(food_img, (food_x, food_y))

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(snake_list)

        score_text = score_font.render("Pontszám: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        level_text = score_font.render("Szint: " + str(level), True, (255, 255, 255))
        screen.blit(level_text, (screen_width - level_text.get_width() - 10, 10))

        if is_muted:
            screen.blit(mute_icon, (10, screen_height - mute_icon.get_height() - 10))

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_block_size) / snake_block_size) * snake_block_size
            food_y = round(random.randrange(0, screen_height - snake_block_size) / snake_block_size) * snake_block_size
            snake_length += 1
            score += 1

            if score % 10 == 0:
                level += 1

        clock.tick(10)

    pygame.quit()


game_menu()
