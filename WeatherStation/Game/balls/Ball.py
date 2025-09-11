import pygame
import random

class Ball:
    """
    Represents a ball that can move and bounce within a window.
    Demonstrates encapsulation and object-oriented principles.
    """
    def __init__(self, x, y, radius, color, speed):
        """
        Initialize a new Ball object.
        :param x: Initial x position
        :param y: Initial y position
        :param radius: Radius of the ball
        :param color: Color of the ball (RGB tuple)
        :param speed: Tuple (speed_x, speed_y)
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x, self.speed_y = speed

    def move(self, width, height):
        """
        Move the ball and bounce off the window edges.
        :param width: Width of the window
        :param height: Height of the window
        """
        self.x += self.speed_x
        self.y += self.speed_y
        # Bounce off the left/right edges
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.speed_x *= -1
        # Bounce off the top/bottom edges
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.speed_y *= -1

    def draw(self, surface):
        """
        Draw the ball on the given surface.
        :param surface: Pygame surface to draw on
        """
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
