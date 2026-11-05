import pygame
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, COLOR_NEON_CYAN

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = 5
        self.speed_y = 5

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x <= 0 or self.x >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.y <= 0:
            self.speed_y = -self.speed_y
        elif self.y >= SCREEN_HEIGHT:
            # Fin del juego
            print('Game Over')
            pygame.quit()
            exit()

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_NEON_CYAN, (self.x, self.y), self.radius)

    def bounce(self, direction):
        if direction == 'x':
            self.speed_x = -self.speed_x
        elif direction == 'y':
            self.speed_y = -self.speed_y