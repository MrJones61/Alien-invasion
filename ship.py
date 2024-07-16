import pygame
class Ship:
    """A class to manage the ship."""
    def __init__(self,ai_game):
        """Initialize the ship and set its position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings


        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/spaceship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom centre of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left  = False


    def update(self):
        """Update the ship position based on movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object from self.x
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    def blitme(self):
        """Draw the ship and its current location."""
        self.screen.blit(self.image,self.rect)