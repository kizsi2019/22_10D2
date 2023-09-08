import pygame
import random
import os

# Játék beállításai
WIDTH = 800
HEIGHT = 600
FPS = 60

# Színek
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Inicializáció és ablak létrehozása
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spacewar")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')

# Betölti az összes képet a megfelelő mérettel
def load_image(file_name):
    image = pygame.image.load(file_name).convert()
    image = pygame.transform.scale(image, (50, 38))  # A képek mérete 50x38 pixel
    image.set_colorkey(WHITE)
    return image

# Háttérkép betöltése
background = pygame.image.load(os.path.join('images', 'background.jpg')).convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Az összes kép betöltése
player_img = load_image(os.path.join('images', 'urhajo.png'))
enemy_img = load_image(os.path.join('images', 'ellenseg.png'))
bullet_img = load_image(os.path.join('images', 'bullet.png'))

def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def show_menu():
    screen.blit(background, (0, 0))
    draw_text(screen, "Spacewar", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Nyomj SPACE-t a játékhoz!", 22, WIDTH / 2, HEIGHT / 2)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

def show_game_over_screen(score):
    screen.blit(background, (0, 0))
    draw_text(screen, "Játék vége", 64, WIDTH / 2, HEIGHT / 4)
    draw_text(screen, "Pontszám: " + str(score), 22, WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "SPACE a kilépéshez", 18, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 4)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 4)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

# Sprite-ok csoportjai
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(10):  # 10 ellenség inicializálása
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
start_time = pygame.time.get_ticks()

# Játékciklus
running = True
show_menu()
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    # Ellenségek megsemmisítése a lövedékkel
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
    for hit in hits:
        score += 1
        enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Játékos ütközése az ellenséggel
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        running = False

    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    draw_text(screen, "Pontszám: " + str(score), 18, WIDTH / 2, 10)

    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time) / 1000
    draw_text(screen, "Idő: {:.2f}s".format(elapsed_time), 18, WIDTH / 2, 40)

    pygame.display.flip()

show_game_over_screen(score)

pygame.quit()
