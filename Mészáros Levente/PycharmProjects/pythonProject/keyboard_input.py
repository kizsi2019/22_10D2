import pygame

WIDTH = 1280
HEIGHT = 620
SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_fw_1 = pygame.image.load('2.3/img/bird1.png').convert_alpha()
bird_fw_2 = pygame.image.load('2.4/bird2.png').convert_alpha()
bird_fw_3 = pygame.image.load('2.4/bird3.png').convert_alpha()
bird_fw_4 = pygame.image.load('2.4/bird4.png').convert_alpha()
birds_fw = [bird_fw_1, bird_fw_2, bird_fw_3, bird_fw_4]
bird_b_1 = pygame.image.load('2.3/img/bird1back.png').convert_alpha()
bird_b_2 = pygame.image.load('2.4/bird2back.png').convert_alpha()
bird_b_3 = pygame.image.load('2.4/bird3back.png').convert_alpha()
bird_b_4 = pygame.image.load('2.4/bird4back.png').convert_alpha()
birds_b = [bird_b_1, bird_b_2, bird_b_3, bird_b_4]
score_font = pygame.font.SysFont('arial', 60)



bird_x = WIDTH / 2
bird_y = HEIGHT / 2
bird_index = 0

counter = 0
forward = True
running = True
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score += 1



    score_text = score_font.render('score: ' + str(score), True, (0, 0, 0))
    score_rect = score_text.get_rect(topleft=(10, 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and bird_rect.right <= WIDTH:
        forward = True
        bird_x += SPEED
    elif keys[pygame.K_LEFT] and bird_rect.left >= 0:
        forward = False
        bird_x -= SPEED

    if keys[pygame.K_UP] and bird_rect.top >= 0:
        bird_y -= SPEED
    elif keys[pygame.K_DOWN] and bird_rect.bottom <= HEIGHT:
        bird_y += SPEED





    screen.fill((140, 137, 246))

    counter += 1
    if counter % 7 == 0:
        bird_index += 1
    if bird_index > len(birds_fw) - 1:
        bird_index = 0

    if forward:
        bird_rect = birds_fw[bird_index].get_rect(center=(bird_x, bird_y))
        screen.blit(birds_fw[bird_index], bird_rect)
    else:
        bird_rect = birds_b[bird_index].get_rect(center=(bird_x, bird_y))
        screen.blit(birds_b[bird_index], bird_rect)

    screen.blit(score_text, score_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
