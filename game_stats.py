import sys
from pathlib import Path

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Load high score from file
        self.high_score = self._load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        self.big_level = 1

    def _load_high_score(self):
        """Load the high score from a file."""
        # Determine the correct path
        if getattr(sys, 'frozen', False):
            # If the application is frozen (packaged by PyInstaller)
            base_path = Path(sys._MEIPASS)
        else:
            # If running in development mode
            base_path = Path(__file__).parent

        file_path = base_path / "last high score.txt"

        try:
            with open(file_path, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            # If the file doesn't exist, return 0 as the default high score
            return 0