class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings.
        self.ship_speed = 3.0

        # Bullet settings.
        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.misses_limit = 2

        # Rectangle settings.
        self.rectangle_speed = 6.0
        self.rectangle_width = 30
        self.rectangle_height = 200
        self.rectangle_color = (0, 0, 0)
        self.rectangle_direction = 1
