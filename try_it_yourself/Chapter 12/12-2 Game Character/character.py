import pygame


class Character:

    def __init__(self, gc_game):
        self.screen = gc_game.screen
        self.screen_rect = gc_game.screen.get_rect()
        self.settings = gc_game.settings

        self.image = pygame.image.load("images/wolf.bmp").convert_alpha()
        # load image with transparency

        self.image = pygame.transform.scale(self.image, (100, 100))
        # scale the transparent image

        colored_bg = pygame.Surface((100, 100)).convert()
        colored_bg.fill(self.settings.char_bg_color)
        # create a background surface and fill with desired color

        colored_bg.blit(self.image, (0, 0))
        self.image = colored_bg
        # blit the transparent image onto the colored background

        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
