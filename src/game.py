import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.running = True

    def update_score(self, points):
        if points < 0:
            raise ValueError("Score cannot be negative")
        self.score += points

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def run(self):
        try:
            while self.running:
                self.handle_events()
                # Game logic here
                self.clock.tick(60)
                pygame.display.flip()
        except Exception as e:
            print(f"Error in game loop: {e}")
            self.running = False

    def get_score(self):
        return self.score