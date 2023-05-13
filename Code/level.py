import pygame
from settings import *
from decor import Decor
from player import Player
from debug import debug


class Level:
    def __init__(self):

        # Setup and creation of 2 group : the visible element and the obstacles elements
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        # Setup of the map
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * DECORSIZE
                y = row_index * DECORSIZE
                if col == 'x':
                    Decor((x, y), [self.visible_sprites, self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

    def run(self):

        # update and draw the game
        self.visible_sprites.custom_draw()
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():  # getting all the sprite
            self.display_surface.blit(sprite.image, sprite.rect)
