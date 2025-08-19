import sys

import pygame
from pygame.sprite import Sprite

from settings import Settings
from ship import Ship
from bullet import Bullet
from rectangle import Rectangle
from game_stats import GameStats
from button import Button


class TargetPractice:
    """A game to practice shooting a rectangle on the right side of the screen."""

    def __init__(self):
        """Initialize the game and set up game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Target Practice")

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.rectangle = Rectangle(self)

        # Start Target Practice in an active state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.rectangle.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mous_pos = pygame.mouse.get_pos()
                self._check_play_button(mous_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self._start_game()

    def _start_game(self):
        """Respond to events meant to start the game."""
        self.stats.reset_stats()
        self.game_active = True

        # Get rid of any remaining bullets.
        self.bullets.empty()

        # Reposition the rectangle and center the ship.
        self.ship.center_ship()
        self.rectangle.reposition_rectangle()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.game_active:
            self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update positions of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have collided with the rectangle or disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self._rectangle_missed(bullet)
            if self.rectangle.rect.colliderect(bullet.rect):
                self._rectangle_hit(bullet)

    def _rectangle_hit(self, bullet):
        """Update the game if a bullet misses the rectangle."""
        self.bullets.remove(bullet)
        self.stats.hits += 1

    def _rectangle_missed(self, bullet):
        """Update the game if a bullet hits the rectangle."""
        if self.stats.misses_left > 0:
            self.bullets.remove(bullet)
            self.stats.misses_left -= 1
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen, and flip to new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets:
            bullet.draw_bullet()
        self.rectangle.draw_rectangle()
        self.ship.blitme()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recent screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    tp = TargetPractice()
    tp.run_game()
