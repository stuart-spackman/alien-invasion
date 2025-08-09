import pygame


class Rocket:
    def __init__(self, rocket_game):
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()

        self.image = pygame.image.load("images/rocket.bmp")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 13
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 13
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 13
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= 13

    def blitme(self):
        self.screen.blit(self.image, self.rect)
