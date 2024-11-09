import pygame
from pygame import Vector3


class Player:
    def __init__(self, username, position, gender, level, health ):
        self.image = pygame.image.load('assets/images/player.png')
        self.rect = self.image.get_rect(topleft=position)
        self.velocity = 5

    def move(self, direction):
        if direction == "left":
            self.rect.x -= self.velocity
        elif direction == "right":
            self.rect.x += self.velocity
        elif direction == "up":
            self.rect.y -= self.velocity
        elif direction == "down":
            self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
