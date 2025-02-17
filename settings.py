class Settings:
    """A class to store all the settings for alien invasion"""
    def __init__(self):
        """Initialize the game's static settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50,150,215)

        # Ship settings
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed = 2
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (230, 0, 0)
        self.bullets_allowed = 10
        
        # Alien setting
        self.fleet_drop_speed = 20
        
        # How quickly the game speed's up.
        self.speedup_scale = 1.1
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """ Initialize the setting that change throught the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        
        # fleet drn of 1 represents right and -1 represents left.
        self.fleet_direction = 1
        #Scoring
        self.alien_points = 50
            
            
    def increase_speed(self):
        """ Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        
        
            
            
            
    
            