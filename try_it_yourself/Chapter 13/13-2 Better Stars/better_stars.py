import pygame
import sys

from star import Star
from random import randint


class BetterStars:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.stars = pygame.sprite.Group()
        self._create_star_fleet()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                self.screen.fill("purple")
                self.stars.draw(self.screen)
                self.clock.tick(60)
                pygame.display.flip()

    def _create_star_fleet(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        current_x, current_y = star_width, star_height
        while current_x < (self.screen_width - star_width):
            while current_y < (self.screen_height - star_height):
                self._create_star(current_x, current_y)
                current_y += 2 * star_height
            current_y = star_height
            current_x += 2 * star_width

        self.stars.draw(self.screen)

    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        rand_rot = randint(-180, 180)
        rand_x = randint(-66, 66)
        rand_y = randint(-66, 66)
        new_star.x = x_position + rand_x
        new_star.rect.x = x_position + rand_x
        new_star.rect.y = y_position + rand_y
        new_star.image = pygame.transform.rotate(new_star.image, rand_rot)
        self.stars.add(new_star)


if __name__ == "__main__":
    bsg = BetterStars()
    bsg.run_game()
