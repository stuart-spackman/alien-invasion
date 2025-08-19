import pygame


class Rectangle:
    """A class to manage the rectangle that gets used for target practice."""

    def __init__(self, tp_game):
        """Create a rectangle object in the upper right corner of the screen."""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = tp_game.screen.get_rect()
        self.color = self.settings.rectangle_color

        # Create a rectangle rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.rectangle_width, self.settings.rectangle_height
        )
        self.rect.y = self.settings.rectangle_width
        self.rect.x = self.screen_rect.width - 2 * self.settings.rectangle_width

        # Store the retangle's position as a float.
        self.y = float(self.rect.y)

    def check_edges(self):
        return (
            self.rect.top < self.settings.rectangle_width
            or self.rect.bottom
            > self.screen_rect.height - self.settings.rectangle_width
        )

    def update(self):
        """Move the rectangle down the screen."""
        # Update the exact position of the rectangle.
        self.y += self.settings.rectangle_direction * self.settings.rectangle_speed
        self.rect.y = self.y
        if self.check_edges():
            self.settings.rectangle_direction *= -1

    def draw_rectangle(self):
        """Draw the rectangle to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

    def reposition_rectangle(self):
        """Reposition the rectangle in the top right corner of the screen."""
        self.rect.y = self.settings.rectangle_width
        self.y = float(self.rect.y)
