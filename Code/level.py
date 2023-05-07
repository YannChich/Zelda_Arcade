import pygame

class Level:
    def __init__(self):

        # adjust the display surface
        self.display_surface = pygame.display.get_surface()

        # Setup and creation of 2 group : the visible element and the obstacles elements
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def run(self):

        # update and draw the game
        pass