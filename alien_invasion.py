import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        self.bullets = pygame.sprite.Group()
        # We can store the ship's bullets in a group.

        self.aliens = pygame.sprite.Group()
        # We can store the aliens in a group.

        self._create_fleet()
        # We need to populate a fleet of aliens to the screen.

    def run_game(self):
        """Start the main loop for the game."""

        while True:
            self._check_events()
            # We need to check for keyboard and mouse events.

            self.ship.update()
            # Update the ship's position after checking for keyboard events.

            self._update_bullets()
            # We need to track the bullets the ship has fired.
            # And delete them when they leave the screen.

            self._update_aliens()
            # We need the aliens to move back and forth across the screen.
            # And drop down after hitting the screen's edge.

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Creates a new bullet and adds it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update positions of bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        # Create an alien and keep adding aliens until there's no room left.
        # The spacing between the aliens is one alien width and one alien height.

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height
            # Finished a row.
            # Reset the x value and increment the y value.

        self.aliens.add(alien)

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
