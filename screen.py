import pygame as py
import numpy as np

import settings
import button

class Screen:
    def __init__(self, bg_colour=py.Color('white'), size=settings.DISPLAY_SIZE, alpha=255):
        self.surface = py.Surface(size, py.SRCALPHA)
        bg_colour.a = alpha
        self.surface.fill(bg_colour)
        # self.surface.fill(bg_colour)
        self.objects = [] 

    def click(self, pos):
        for obj in self.objects:
            if isinstance(obj, button.Button):
                clicked = obj.click(pos)
                if clicked:
                    return clicked

    def draw(self, display):
        for obj in self.objects:
            obj.draw(self.surface)
        pos = ((np.array(settings.DISPLAY_SIZE) - np.array(self.surface.get_size()))/2).astype(int)
        display.blit(self.surface, list(pos))