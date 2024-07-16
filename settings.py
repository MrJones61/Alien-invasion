class Settings:
    """A class to store all the settings for alien invasion"""
    def __init__(self):
        """Initialize the game setting."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50,150,215)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 0

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 10
        # Alien setting
        
        self.alien_speed = 1.0
        self.fleet_drop_speed = 20
        # -1 and  1 represent left and right fleet direction respectively.
        self.fleet_direction = -1