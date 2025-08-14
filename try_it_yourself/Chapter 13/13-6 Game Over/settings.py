class Settings:
    """A class to store all settings for Sideways Shooter."""

    def __init__(self):
        """Initialize the game's settings."""

        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (230, 230, 230)
        # Screen settings.

        self.rocket_speed = 13
        self.rocket_limit = 2
        # Rocket settings.

        self.bullet_speed = 6.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Bullet settings.

        self.alien_speed = 13.0
        self.fleet_shift_distance = 33
        self.fleet_direction = 1
        # Alien settings.
        # fleet_direction of 1 represents down; -1 represents up.
