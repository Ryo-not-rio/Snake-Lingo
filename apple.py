import pygame as py
import random

import settings

class Apple:
    def __init__(self, text, snake):
        self.surface = settings.text_surface(text)
        self.position = (random.randint(0, settings.NUM_ROWS_COLUMNS-1), random.randint(0, settings.NUM_ROWS_COLUMNS-1))
        while snake.collide(self.position):
            self.position = (random.randint(0, settings.NUM_ROWS_COLUMNS-1), random.randint(0, settings.NUM_ROWS_COLUMNS-1))


    def draw(self, display):
        display.blit(self.surface, settings.grid_to_pos(self.position))