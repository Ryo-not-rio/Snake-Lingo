import pygame as py
import random
import os

import settings

img = py.image.load(os.path.join("images", "apple.png"))
img = py.transform.scale(img, (settings.BLOCK_SIZE, settings.BLOCK_SIZE))

class Apple:
    def __init__(self, text, grid):
        self.img = img.convert_alpha()
        self.surface = settings.text_surface(text)
        self.position = (random.randint(0, settings.NUM_ROWS_COLUMNS-1), random.randint(0, settings.NUM_ROWS_COLUMNS-1))
        while grid[self.position[0]][self.position[1]]:
            self.position = (random.randint(0, settings.NUM_ROWS_COLUMNS-1), random.randint(0, settings.NUM_ROWS_COLUMNS-1))


    def draw(self, display):
        display.blit(self.img, settings.grid_to_pos(self.position))
        display.blit(self.surface, settings.grid_to_pos(self.position))