class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Screen settings.

        self.ship_speed = 1.5
        # Ship settings.

        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Bullet settings.

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        # Alien settings.
        # Fleet_direction of 1 represents moving right; -1 represents left.
