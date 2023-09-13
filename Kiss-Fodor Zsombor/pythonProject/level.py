import pygame
from settings import tile_size
from tiles import TerrainTile


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.terrain_tiles = pygame.sprite.Group()
        self.setup_level(level_data)

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, tile_type in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if tile_type != ' ':
                    tile = TerrainTile(tile_size, x, y, tile_type)
                    self.terrain_tiles.add(tile)

    def run(self):
        self.terrain_tiles.draw(self.display_surface)

