import pygame

def init_game():
    pygame.init()
    pygame.display.set_mode((800, 600))
    return {"status": "initialized", "screen_size": (800, 600)}