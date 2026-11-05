import pygame

from src.config import COLOR_NEON_CYAN

class Brick:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.destroyed = False

    def draw(self, screen):
        if not self.destroyed:
            pygame.draw.rect(screen, COLOR_NEON_CYAN, (self.x, self.y, self.width, self.height))

    def is_destroyed(self):
        return self.destroyed

    def destroy(self):
        self.destroyed = True