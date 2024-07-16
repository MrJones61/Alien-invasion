class GameStats:
    """ Track the statistics for alien invasion"""
    def __init__(self,ai_game):
        """ Initialize the statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start alien invasion in an inactive state
        self.game_active = False

    def reset_stats(self):
        """ Initialize the statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        