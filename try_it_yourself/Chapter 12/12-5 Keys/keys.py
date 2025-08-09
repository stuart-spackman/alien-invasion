import pygame
import sys


class Keys:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 300))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Keys")

        self.text = ""
        # use a system font
        self.font = pygame.font.SysFont("Arial", 66)
        # render the text to surface
        self.text_surface = self.font.render("testing", True, "red")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    event_key = pygame.key.name(event.key)
                    self.text_surface = self.font.render(event_key, True, "red")

            self.screen.fill("black")
            self.screen.blit(self.text_surface, (300, 150))
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    k = Keys()
    k.run_game()
