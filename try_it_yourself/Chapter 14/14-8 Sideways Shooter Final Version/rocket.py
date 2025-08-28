import pygame
from pygame.sprite import Sprite


class Rocket(Sprite):
    """A class to manage the rocket."""

    def __init__(self, ss_game):
        super().__init__()
        """Initialize the ship and get its starting position"""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()
        self.image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(self.image, (133, 133))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.height:
            self.y += self.settings.rocket_speed
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_rocket(self):
        """Center the rocket on the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
