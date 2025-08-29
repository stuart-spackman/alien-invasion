from pathlib import Path


class GameStats:
    """Track statistics for Sideways Shooter."""

    def __init__(self, ss_game):
        """Initialize the game's statistics from the settings."""
        self.settings = ss_game.settings
        self.path = Path("all_time_high_score.json")
        self.reset_stats()

        # High score should never be reset.
        self.high_score = int(self.path.read_text())

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.rockets_left = self.settings.rocket_limit
        self.score = 0
        self.level = 1
