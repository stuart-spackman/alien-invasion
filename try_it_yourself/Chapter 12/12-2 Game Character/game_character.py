import pygame
import sys

from character import Character
from settings import Settings


class GameCharacter:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Game Character")

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.character = Character(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.screen_bg_color)
            self.character.blitme()
            pygame.display.flip()
            self.clock.tick(60)

    def update_screen(self):
        pass


if __name__ == "__main__":
    gc = GameCharacter()
    gc.run_game()
