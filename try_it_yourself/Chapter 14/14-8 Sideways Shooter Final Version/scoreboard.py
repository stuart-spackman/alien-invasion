import pygame.font
from pygame.sprite import Group

from rocket import Rocket


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ss_game):
        """Initialize scorekeeping attributes."""
        self.ss_game = ss_game
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats

        # Font settings for scoring information.

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 33)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_rockets()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color
        )

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 5

    def show_score(self):
        """Draw scores, levels, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.rockets.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score: {high_score:,}"
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color
        )

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            self.prep_level()

    def prep_level(self):
        """Turn the current level into a rendered image."""
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color
        )

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 5

    def prep_rockets(self):
        """Show how many ships are left."""
        self.rockets = Group()
        scale_factor = 0.5  # shrink to 20%
        for rocket_number in range(self.stats.rockets_left):
            rocket = Rocket(self.ss_game)
            w, h = rocket.image.get_size()
            rocket.image = pygame.transform.scale(
                rocket.image, (int(w * scale_factor), int(h * scale_factor))
            )
            rocket.rect = rocket.image.get_rect(topleft=rocket.rect.topleft)
            rocket.rect.x = rocket_number * rocket.rect.width
            rocket.rect.y = self.screen_rect.height - rocket.rect.height
            self.rockets.add(rocket)
