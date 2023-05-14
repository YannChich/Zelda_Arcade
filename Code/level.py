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
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2  # .get_size return a tuple the [0] = width
        self.half_height = self.display_surface.get_size()[1] // 2  # ...                     the [1] = height
        self.offset = pygame.math.Vector2()

    def custom_draw(self,player):
        # move the camera to be focus on the player , also apply the offset on each sprites
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        for sprite in self.sprites():  # getting all the sprite
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)  # blit : bit block transfer draw the sprite on the
            # display and going to update to see them
