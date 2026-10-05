# Simple game loop using Pygame
# install pygame using: pip install pygame
# if you installed it in the global environment, you can run this script on a commamd line using: python game_v1.py

import pygame
from Player_v1 import Player

# Define a color using RGB (Red=255, Green=255, Blue=0 -> Yellow)
YELLOW = (255, 255, 0)
BLUE = (36, 122, 127)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create player object
player = Player(375, 275)

# Game loop
running = True
while running:
    screen.fill(BLUE) # Draw background

    # input:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:  # Check if ESC is pressed
        running = False

    # update:
    player.move(keys)
    
    # draw:
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
