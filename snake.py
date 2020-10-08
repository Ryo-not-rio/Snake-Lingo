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
        if self.position[0] < 0:
            self.position[0] = settings.NUM_ROWS_COLUMNS-1
        if self.position[0] >= settings.NUM_ROWS_COLUMNS:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = settings.NUM_ROWS_COLUMNS-1
        if self.position[1] >= settings.NUM_ROWS_COLUMNS:
            self.position[1] = 0


    def change_directions(self, direction):
        if direction is not None:
            direction_str = ['up', 'down', 'left', 'right']
            direction_arr = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            new_vel = direction_arr[direction_str.index(direction)]
            if (np.multiply(np.array(new_vel), np.array(self.vel)) == np.array((0, 0))).all():
                self.vel = new_vel


    def draw(self, display):
        display.blit(self.head_surface, settings.grid_to_pos(self.position))