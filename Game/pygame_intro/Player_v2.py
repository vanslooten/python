
import pygame
from Sprite import Sprite

# Player class inherits from Sprite
class Player(Sprite):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path, size=50)
        self.speed = 5
        self.vx = 0
        self.vy = 0
        self.bounce_frames = 0
        self.bounce_decay = 0.85  # velocity decay per frame after bounce
        self.bounce_duration = 10  # frames to keep bouncing

    def move(self, keys, obstacles, window_width=800, window_height=600):
        # If not bouncing, set velocity from keys
        if self.bounce_frames == 0:
            vx, vy = 0, 0
            if keys[pygame.K_LEFT]:
                vx = -self.speed
            if keys[pygame.K_RIGHT]:
                vx = self.speed
            if keys[pygame.K_UP]:
                vy = -self.speed
            if keys[pygame.K_DOWN]:
                vy = self.speed
            self.vx = vx
            self.vy = vy
            # Flip sprite if moving left or right
            if vx < 0:
                self.flip(True)
            elif vx > 0:
                self.flip(False)
        else:
            # Continue bouncing, decay velocity
            self.vx *= self.bounce_decay
            self.vy *= self.bounce_decay
            self.bounce_frames -= 1
            # Stop bouncing if velocity is very low
            if abs(self.vx) < 0.5 and abs(self.vy) < 0.5:
                self.vx = 0
                self.vy = 0
                self.bounce_frames = 0

        # Save old position
        old_x, old_y = self.x, self.y

        # Try to move in x direction
        self.x += self.vx
        player_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        for obs in obstacles:
            if player_rect.colliderect(obs.rect):
                # Bounce X
                if self.vx > 0:
                    self.x = obs.rect.left - self.size
                elif self.vx < 0:
                    self.x = obs.rect.right
                self.vx = -self.vx
                self.bounce_frames = self.bounce_duration
                player_rect = pygame.Rect(self.x, self.y, self.size, self.size)

        # Wall bounce X
        if self.x < 0:
            self.x = 0
            self.vx = -self.vx
            self.bounce_frames = self.bounce_duration
        elif self.x + self.size > window_width:
            self.x = window_width - self.size
            self.vx = -self.vx
            self.bounce_frames = self.bounce_duration

        # Try to move in y direction
        self.y += self.vy
        player_rect = pygame.Rect(self.x, self.y, self.size, self.size)
        for obs in obstacles:
            if player_rect.colliderect(obs.rect):
                # Bounce Y
                if self.vy > 0:
                    self.y = obs.rect.top - self.size
                elif self.vy < 0:
                    self.y = obs.rect.bottom
                self.vy = -self.vy
                self.bounce_frames = self.bounce_duration
                player_rect = pygame.Rect(self.x, self.y, self.size, self.size)

        # Wall bounce Y
        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
            self.bounce_frames = self.bounce_duration
        elif self.y + self.size > window_height:
            self.y = window_height - self.size
            self.vy = -self.vy
            self.bounce_frames = self.bounce_duration
