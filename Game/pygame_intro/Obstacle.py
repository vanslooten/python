import pygame

class Obstacle:
    def __init__(self, x, y, width, height, color=(200, 0, 0)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
