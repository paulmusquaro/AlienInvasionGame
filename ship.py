import pygame

class Ship:
    """A class for controlling a ship."""

    def __init__(self, ai_game, scale_factor=0.05, offset=0.02):
        """Initialize the ship and set its initial position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load a ship image
        self.original_image = pygame.image.load('images/starship_1.bmp')

        # Scale the image
        original_size = self.original_image.get_size()
        new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
        self.image = pygame.transform.scale(self.original_image, new_size)

        # Get new rect after resizing
        self.rect = self.image.get_rect()

        # Place ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Move the ship up by 1% of the screen height
        self.rect.y -= int(self.screen_rect.height * offset)

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement indicators.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the current position of the ship based on the motion indicators."""
        # Update the value of ship.x, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect object with self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship in its current location."""
        self.screen.blit(self.image, self.rect)
