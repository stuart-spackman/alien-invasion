import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage assets and game behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""

        pygame.init()
        # This initializes background settings that Pygame needs to function properly.

        self.clock = pygame.time.Clock()
        # Games should run at the same speed on all systems.

        self.settings = Settings()
        # We need a settings class to call on that has constants.

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # We assign a display window to self.screen so it'll be available to all methods in the class.

        pygame.display.set_caption("Alien Invasion")
        # A caption can be displayed in the window.

        self.ship = Ship(self)
        # The game needs a ship to display.

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events()
            # We need to check for keyboard and mouse events.

            self.ship.update()
            # Update the ship's position after checking for keyboard events.

            self._update_screen()
            # We need to update the screen with images.

            self.clock.tick(60)
            # The game loop runs 60 times per second.

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Responds to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
