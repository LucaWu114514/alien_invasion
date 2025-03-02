from pathlib import Path

import pygame.font
from pygame.sprite import Group

from click import Ship

class Scoreboard:
    def __init__(self,ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (225,225,225)
        self.font = pygame.font.SysFont(None,48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ship()
        self.prep_big_level()

    def prep_score(self):
        rounded_score = round(self.stats.score,-1)
        score_str = f"Score{rounded_score:,}"
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = round(self.stats.high_score,-1)
        high_score_str = f"High Score{high_score:,}"
        self.high_score_image = self.font.render(high_score_str,True,
                self.text_color,self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        path = Path('last high score.txt')
        path.write_text(str(high_score))


    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.big_level_image,self.big_level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    def prep_level(self):
        level_str = str(f"Kill alien:{self.stats.level}")
        self.level_image = self.font.render(level_str,True,
                self.text_color,self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ship(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_big_level(self):

        big_level_str = str(f"Turn{self.stats.big_level}")
        self.big_level_image = self.font.render(big_level_str, True,
                self.text_color, self.settings.bg_color)
        self.big_level_rect = self.big_level_image.get_rect()
        self.big_level_rect.right = self.score_rect.right

        self.big_level_rect.top = self.score_rect.bottom + 50

