import pygame as py
import random

import settings

class Apple:
    def __init__(self, snake):
        self.position = (random.randint(0, settings.NUM_ROWS_COLUMNS-1), random.randint(0, settings.NUM_ROWS_COLUMNS-1))
        while snake.collide(self.position):
            self.position = (random.randint(0, settings.NUM_ROWS_COLUMNS-1), random.randint(0, settings.NUM_ROWS_COLUMNS-1))


    def draw(self, display):
        py.draw.circle(display, py.Color('red'), [int(p + settings.BLOCK_SIZE/2) for p in settings.grid_to_pos(self.position)], int(settings.BLOCK_SIZE/2))