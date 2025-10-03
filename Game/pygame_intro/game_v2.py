# added:
# - Sprite class to Player_v2.py
# - Obstacle class
# - Smooth movement with key holds and bouncing off obstacles and walls

import pygame
import random
from Player_v2 import Player
from Obstacle import Obstacle

# define player sprite path
player_sprite = "player.png"

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a color using RGB (Red=255, Green=255, Blue=0 -> Yellow)
YELLOW = (255, 255, 0)
BLUE = (36, 122, 127)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Create random obstacles (yellow, varying sizes)
obstacles = []
num_obstacles = random.randint(3, 7)
for _ in range(num_obstacles):
    width = random.randint(40, 200)
    height = random.randint(20, 100)
    x = random.randint(0, SCREEN_WIDTH - width)
    y = random.randint(0, SCREEN_HEIGHT - height)
    obstacles.append(Obstacle(x, y, width, height, YELLOW))

# Find a player start position not overlapping any obstacle
player_size = 50
while True:
    px = random.randint(0, SCREEN_WIDTH - player_size)
    py = random.randint(0, SCREEN_HEIGHT - player_size)
    player_rect = pygame.Rect(px, py, player_size, player_size)
    if not any(player_rect.colliderect(obs.rect) for obs in obstacles):
        break
player = Player(px, py, player_sprite)

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
    player.move(keys, obstacles, window_width=SCREEN_WIDTH, window_height=SCREEN_HEIGHT)

    # draw:
    for obstacle in obstacles:
        obstacle.draw(screen)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
