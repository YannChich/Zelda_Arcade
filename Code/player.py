import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -26)
        self.direction = pygame.math.Vector2()  # default x=0 y=0
        self.speed = 5
        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        # This if is to update the movement in diagonal
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()  # normalize the vector to the one

        self.hitbox.x += self.direction.x * speed  # rect.center change the position of the player
        self.collision('horizontal')  # checking the collision
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center  # updating the new center of the object Rect (player)

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # pressing right
                        self.hitbox.right = sprite.hitbox.left  # if we got a collision with an obstacle , the player
                        # going back up
                    if self.direction.x < 0:  # pressing left
                        self.hitbox.left = sprite.hitbox.right  # same as ligne 41
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # pressing down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # pressing up
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)
