import pygame as py
import settings

class Snake:
    def __init__(self):
        self.head_surface = py.Surface((settings.BLOCK_SIZE, settings.BLOCK_SIZE), py.SRCALPHA)
        self.position = (9, 9)
        radius = int(settings.BLOCK_SIZE/2)
        py.draw.circle(self.head_surface, (255, 255, 255), (radius, radius), radius)

    def draw(self, display):
        display.blit(self.head_surface, settings.grid_to_pos(self.position))