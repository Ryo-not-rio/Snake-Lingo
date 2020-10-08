import pygame as py
import numpy as np

import settings

class Snake:
    def __init__(self):
        self.head_surface = settings.text_surface("hello")
        self.position = (9, 9)
        self.vel = (0, 0)
        radius = int(settings.BLOCK_SIZE/2)

    def move(self):
        self.position = list(np.array(self.position) + np.array(self.vel))

    def draw(self, display):
        display.blit(self.head_surface, settings.grid_to_pos(self.position))