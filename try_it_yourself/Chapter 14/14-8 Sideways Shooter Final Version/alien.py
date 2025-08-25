import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ss_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        self.image = ss_game.alien_image
        self.rect = self.image.get_rect()
        # Get the alien image and set its rect attribute.

        self.rect.x = self.screen.get_width() - 2 * self.rect.width
        self.rect.y = self.rect.height
        # Start each alien near the top right of the screen.

        self.y = float(self.rect.y)
        # Store the alien's exact vertical position.

    def check_edges(self):
        """Return true if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0

    def update(self):
        """Move the alien down."""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
