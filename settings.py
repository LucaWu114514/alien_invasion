from random import randint
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1700
        self.screen_height = 900
        self.bg_color = (255, 255, 255)

        # Ship settings.
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.8
        self.bullet_width = 5
        self.bullet_height = 18
        self.bullet_color = (245, 0, 0)
        self.bullets_allowed = 3

        # Alien settings.
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.ships_left = 3

        self.bestbullet_speed = 10
        self.bestbullet_width = 50
        self.bestbullet_height = 20
        self.bestbullets_allowed = 1
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.8
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


        self.alien_points = int(self.alien_points * self.score_scale)

