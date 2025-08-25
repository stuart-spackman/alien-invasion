class GameStats:
    """Track statistics for Sideways Shooter."""

    def __init__(self, ss_game):

        self.settings = ss_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.rockets_left = self.settings.rocket_limit
