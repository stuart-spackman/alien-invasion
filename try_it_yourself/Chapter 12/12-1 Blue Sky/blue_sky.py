import pygame
import sys


class BlueSky:

    def __init__(self):
        # initialize the game
        pygame.init()

        # initialize the screen
        self.screen = pygame.display.set_mode((1200, 800))
        self.bg_color = (135, 206, 235)

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            pygame.display.flip()


if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()
