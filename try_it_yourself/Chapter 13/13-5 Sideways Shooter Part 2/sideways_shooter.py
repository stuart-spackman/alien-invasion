import pygame
import sys

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien


class SidewaysShooter:
    """Overall class to manange game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        full_alien = pygame.image.load("images/alien.bmp").convert_alpha()
        trim_rect = full_alien.get_bounding_rect(min_alpha=1)
        self.alien_image = full_alien.subsurface(trim_rect).copy()
        self.alien_image = pygame.transform.scale(self.alien_image, (100, 66))
        # Auto-trim transparent white space.
        # Create an image to lend to the Alien class.

        pygame.display.set_caption("Sideways Shooter")
        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

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
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_bullet(self):
        """Create new bullets and add it the the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            # Destroy existing bullets and create a new fleet.

    def _create_fleet(self):
        """Create a fleet of aliens."""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.width, alien.rect.height
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien height.

        current_x, current_y = (
            self.settings.screen_width - 2 * alien_width,
            alien_height,
        )
        while current_x > 3 * alien_width:
            while current_y < (self.settings.screen_height - 2 * alien_height):
                self._create_alien(current_x, current_y)
                current_y += 2 * alien_height
            current_y = alien_height
            current_x -= 2 * alien_width

    def _create_alien(self, x_position, y_postition):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.y = y_postition
        new_alien.rect.y = y_postition
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Check if any aliens in the fleet have hit an edge and respond appropriately."""
        for alien in self.aliens:
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_shift_distance
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance and run the game."""
    ss = SidewaysShooter()
    ss.run_game()
