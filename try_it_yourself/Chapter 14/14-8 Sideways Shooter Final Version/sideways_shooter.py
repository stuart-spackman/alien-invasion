import sys
from time import sleep
from pathlib import Path

import pygame

from settings import Settings
from rocket import Rocket
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class SidewaysShooter:
    """Overall class to manange game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Uncomment this for moving to fullscreen mode.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # Create an image to lend to the Alien class.
        self._prep_alien_image()

        pygame.display.set_caption("Sideways Shooter")

        # Create an instance to store game statistics, and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.path = Path("all_time_high_score.json")

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Start Alien Invation in an active state.
        self.game_active = False
        self.difficulty_buttons_active = False

        # Make the play button.
        self.play_button = Button(self, "Play")

        # Make the difficulty buttons.
        self.difficulty_buttons = [
            Button(self, "Difficulty", 0),
            Button(self, "1", 1),
            Button(self, "2", 2),
            Button(self, "3", 3),
        ]

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.rocket.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.path.write_text(str(self.stats.high_score))
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.game_active and not self.difficulty_buttons_active:
                    self._check_play_button(mouse_pos)
                elif not self.game_active and self.difficulty_buttons_active:
                    self._check_difficulty_buttons(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.difficulty_buttons_active = True

    def _check_difficulty_buttons(self, mouse_pos):
        """Check for mouse events on the difficulty buttons."""
        for button in self.difficulty_buttons[1:4]:
            button_clicked = button.rect.collidepoint(mouse_pos)
            if button_clicked:
                self.difficulty_buttons_active = False
                self.game_active = True
                self._start_game(int(button.msg))

    def _start_game(self, difficulty=1):
        """Set off events needed to start a new game."""
        self.settings.initialize_dynamic_settings(difficulty)
        self.stats.reset_stats()
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_rockets()
        self.game_active = True

        # Get rid of any remaining bullets and aliens.
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.rocket.center_rocket()

        # Hide the mouse cursor and the difficulty buttons.
        pygame.mouse.set_visible(False)
        self.difficulty_buttons_active = False

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            self.path.write_text(str(self.stats.high_score))
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self.difficulty_buttons_active = True
        elif self.difficulty_buttons_active:
            if event.key == pygame.K_1:
                self._start_game(1)
            elif event.key == pygame.K_2:
                self._start_game(2)
            elif event.key == pygame.K_3:
                self._start_game(3)

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

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_rockets()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

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

        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()
            # Look for alien-ship collisions.

        self._check_aliens_side()
        # Look for aliens hitting the side of the screen.

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

    def _rocket_hit(self):
        """Respond to the rocket being hit by an alien."""
        if self.stats.rockets_left > 0:
            self.stats.rockets_left -= 1
            self.sb.prep_rockets()
            # Decrement ships left.

            self.bullets.empty()
            self.aliens.empty()
            # Get rid of any remaining bullets and aliens.

            self._create_fleet()
            self.rocket.center_rocket()
            # Create a new fleet and center the ship.

            sleep(0.5)
            # Pause.
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_side(self):
        """Check if any aliens have reached the side of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                self._rocket_hit()
                break
                # Treat this the same as if the rocket got hit.

    def _prep_alien_image(self):
        """Prepare the alien image just once to make copying it easier."""
        full_alien = pygame.image.load("images/alien.bmp").convert_alpha()
        trim_rect = full_alien.get_bounding_rect(min_alpha=1)
        self.alien_image = full_alien.subsurface(trim_rect).copy()
        self.alien_image = pygame.transform.scale(self.alien_image, (100, 66))

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active and not self.difficulty_buttons_active:
            self.play_button.draw_button()
        elif not self.game_active and self.difficulty_buttons_active:
            for button in self.difficulty_buttons:
                button.draw_button()
        pygame.display.flip()


if __name__ == "__main__":
    """Make a game instance and run the game."""
    ss = SidewaysShooter()
    ss.run_game()
