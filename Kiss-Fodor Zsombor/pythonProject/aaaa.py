import pygame
from kocsikauwu import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.player = pygame.sprite.GroupSingle()
        self.terrain_tiles = pygame.sprite.Group()
        self.setup_level(level_data)

    def setup_level(self, layout):
        player_sprite = Player((20, 40))
        self.player.add(player_sprite)


    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                if player.direction.y > 0:
                    player.rect.down = player.rect.up
                if player.direction.y < 0:
                    player.rect.up = player.rect.down

    def vertical_movement_collision(self):
        player = self.player.sprite


    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.terrain_tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)