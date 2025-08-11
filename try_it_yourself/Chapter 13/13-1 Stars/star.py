import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, star_game):
        super().__init__()
        self.screen = star_game.screen
        self.image = pygame.image.load("images/star.bmp")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
