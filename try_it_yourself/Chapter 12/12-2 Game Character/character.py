import pygame

# initialize pygame
pygame.init()

# set a default image position
DEFAULT_IMAGE_POSITION = (100, 100)

# set window size
size = (width, height) = (600, 600)
screen = pygame.display.set_mode(size)

# set the default size for the image
DEFAULT_IMAGE_SIZE = (200, 200)

# clock
clock = pygame.time.Clock()

# load image with transparency
image = pygame.image.load("images/wolf.bmp")
image = image.convert_alpha()

# scale the transparent image first
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

# create a background surface and fill with desired color
bg_color = (255, 0, 255)
colored_bg = pygame.Surface(DEFAULT_IMAGE_SIZE).convert()
colored_bg.fill(bg_color)

# blit the transparent image onto the color background
colored_bg.blit(image, (0, 0))
# now colored_bg has the image with solid background


# MAIN LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 255, 0))
    screen.blit(colored_bg, DEFAULT_IMAGE_POSITION)  # blit final image

    pygame.display.flip()
    clock.tick(30)
