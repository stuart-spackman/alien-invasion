import pygame
import sys

from raindrop import Raindrop
from settings import Settings


class Raindrops:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode((1200, 800))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.raindrops = pygame.sprite.Group()
        self._create_raindrops()
        self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self._update_raindrops()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)
        pygame.display.flip()

    def _check_egdes(self):
        pass

    def _create_raindrops(self):
        raindrop = Raindrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size
        current_x, current_y = raindrop_width, raindrop_height
        while current_x < (self.settings.screen_width - 2 * raindrop_width):
            while current_y < (self.settings.screen_height - 2 * raindrop_height):
                self._create_raindrop(current_x, current_y)
                current_y += 2 * raindrop_height
            current_y = raindrop_height
            current_x += 2 * raindrop_width

    def _update_raindrops(self):
        self.raindrops.update()
        for raindrop in self.raindrops.copy():
            if raindrop.rect.bottom >= self.settings.screen_height:
                self.raindrops.remove(raindrop)

    def _create_raindrop(self, x_position, y_position):
        new_raindrop = Raindrop(self)
        new_raindrop.y = y_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.raindrops.add(new_raindrop)


if __name__ == "__main__":
    rdg = Raindrops()
    rdg.run_game()
