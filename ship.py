import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """
        Initialize the ship and set its starting position.
        Taking in ai_game gives Ship access to all the game resources.
        """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        # Load the ship image and get its rect.

        self.rect.midbottom = self.screen_rect.midbottom
        # Start each new ship at the bottom of the screen.

        self.x = float(self.rect.x)
        # Store a float for the ship's exact horizontal position.

        self.moving_right = False
        self.moving_left = False
        # Movement flag; start with a ship that isn't moving.

    def update(self):
        """
        Update the ship's position based on the movement flag.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
            # Increase the ship's x value, not the rect.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            # Decrease the ship's x value, not the rect.

        self.rect.x = self.x
        # Update the rect object from self.x.

    def blitme(self):
        """
        Draw the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
