class GameStats:
    """Track statistics for Target Practice."""

    def __init__(self, tp_game):
        """Initialize statistics."""
        self.settings = tp_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.misses_left = self.settings.misses_limit
        self.hits = 0
