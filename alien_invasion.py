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

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # We assign a display window to self.screen so it'll be available to all methods in the class.
        # This is also called a surface.
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        # self.bg_color = (230, 230, 230)

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        running = True
        while running:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                # This function returns a list of events that have taken place since the last time
                # the function was called.
                # if event.type == pygame.QUIT:
                # sys.exit()
                self._check_events()

            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.bg_color)
            # self.screen.fill(self.settings.bg_color)
            # This acts on a surface and takes only one argument.
            # self.ship.blitme()

            # Make the most recently drawn screen visible.
            # pygame.display.flip()

            self._update_screen()
            self.clock.tick(60)  # loop runs 60 times per second

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
