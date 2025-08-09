import pygame
import sys

from rocket import Rocket


class RocketGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket Game")

        self.rocket = Rocket(self)

    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True
                if event.key == pygame.K_LEFT:
                    self.rocket.moving_left = True
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.rocket.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.rocket.moving_down = False
                if event.key == pygame.K_LEFT:
                    self.rocket.moving_left = False
                if event.key == pygame.K_RIGHT:
                    self.rocket.moving_right = False

    def _update_screen(self):
        self.screen.fill("gray")
        self.rocket.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    rc = RocketGame()
    rc.run_game()
