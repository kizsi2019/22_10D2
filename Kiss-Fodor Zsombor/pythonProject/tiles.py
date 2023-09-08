import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))


class TerrainTile(Tile):
    def __init__(self, size, x, y, terrain_type):
        super().__init__(size, x, y)
        self.image = pygame.image.load('img/b').convert_alpha()
