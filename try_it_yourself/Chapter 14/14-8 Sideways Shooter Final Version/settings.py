class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Rocket settings.
        self.rocket_limit = 3

        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings.
        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_shift_distance = 33

        # How quickly the game speeds up.
        self.speedup_scale = 2.0

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, difficulty=1):
        """Initialize settings that change throughout the game."""
        self.rocket_speed = 6.0 * difficulty
        self.bullet_speed = 10.0 * difficulty
        self.alien_speed = 2.0 * difficulty

        # fleet_direction of 1 represents down; -1 represents up.
        self.fleet_direction = 1

        # Score settings.
        self.alien_points = 50 * difficulty

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
