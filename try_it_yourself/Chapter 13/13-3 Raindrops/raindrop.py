import pygame

from pygame.sprite import Sprite


class Raindrop(Sprite):
    def __init__(self, rd_game):
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings
        self.image = pygame.image.load("images/raindrop.bmp")
        self.image = pygame.transform.scale(self.image, (66, 66))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y

    def change_directions(self):
        pass
