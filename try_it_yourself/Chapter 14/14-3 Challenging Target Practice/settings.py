class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Bullet settings.
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.misses_limit = 2

        # Rectangle settings.
        self.rectangle_speed = 3.0
        self.rectangle_width = 30
        self.rectangle_height = 200
        self.rectangle_color = (0, 0, 0)
        self.rectangle_direction = 1

        # How quickly the game speeds up.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3.0
        self.bullet_speed = 9.0
        self.rectangle_speed = 2.0

        # rectangle_direction of 1 represents down; -1 represents up.
        self.rectangle_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.rectangle_speed *= self.speedup_scale
