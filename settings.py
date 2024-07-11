class Settings:
    """A class to store all the settings for alien invasion"""
    def __init__(self):
        """Initialize the game setting."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50,50,50)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)