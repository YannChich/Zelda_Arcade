import pygame
from settings import *


class Decor(pygame.sprite.Sprite):
    def __init__(self, pos,groups,sprite_type,surface=pygame.Surface((DECORSIZE,DECORSIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        self.image = pygame.image.load('../graphics/test/rock (1).png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)  # change the size of a Rect.
