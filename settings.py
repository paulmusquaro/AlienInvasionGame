class Settings:
    """Class for storing all game settings."""

    def __init__(self):
        """Initialize game settings."""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (11, 11, 69)
        self.ship_speed = 1.5

        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3