import pygame as py
import numpy as np

import settings

class Screen:
    def __init__(self, bg_colour=py.Color('white'), size=settings.DISPLAY_SIZE):
        self.surface = py.Surface((size, size))
        self.bg_colour = bg_colour
        self.objects = [] # Pair of (Surface, pos)

    def draw(self, display):
        self.surface.fill(self.bg_colour)
        for obj in self.objects:
            self.surface.blit(obj[0], obj[1])
        pos = ((np.array(settings.DISPLAY_SIZE) - np.array(self.surface.get_size()))/2).astype(int)
        display.blit(self.surface, list(pos))