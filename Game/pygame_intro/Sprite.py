
import pygame

# Sprite base class
class Sprite:
    def __init__(self, x, y, image_path, size=50):
        self.x = x
        self.y = y
        self.size = size
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (self.size, self.size))
        self.image = self.original_image
        self.flipped = False

    def flip(self, flip_x):
        if flip_x != self.flipped:
            self.image = pygame.transform.flip(self.original_image, True, False) if flip_x else self.original_image
            self.flipped = flip_x

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

