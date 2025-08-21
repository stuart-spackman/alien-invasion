class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Screen settings.

        self.ship_limit = 3
        # Ship settings.

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Bullet settings.

        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # Alien settings.

        self.speedup_scale = 1.1
        # How quickly the game speeds up.

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, difficulty=1):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5 * difficulty
        self.bullet_speed = 2.5 * difficulty
        self.alien_speed = 1.0 * difficulty

        self.fleet_direction = 1
        # Fleet_direction of 1 represents moving right; -1 represents left.

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
