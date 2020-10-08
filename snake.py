import pygame as py
import numpy as np

import settings


class SnakeBod:
    def __init__(self, position, rotation):
        self.original_surface = settings.text_surface("hello")
        self.rotation = rotation
        self.position = position
        self.vel = (0, 0)
        self.behind = None
        self.wait = True

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
            direction_arr = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
            ind = direction_arr.index(direction)
            new_vel = direction_arr[ind]
            if (np.multiply(np.array(new_vel), np.array(self.vel)) == np.array((0, 0))).all():
                self.vel = new_vel
                self.rotation = -90*(ind % 4)

    def draw(self, display):
        display.blit(py.transform.rotate(self.original_surface, self.rotation), settings.grid_to_pos(self.position))        


class Snake(SnakeBod):
    def __init__(self):
        super().__init__((9, 9), 0)


    def eat(self):
        body = self
        while body.behind is not None:
            body = body.behind
        body.behind = Snake(body.position)

        for i, b in enumerate(self.body[1:]):
            if not b.wait:
                if i == 0:
                    new_dir = self.vel
                else:
                    new_dir = self.body[i-1].vel
                b.change_directions(self.vel)
                b.move()
            else:
                b.wait = False
        
        for b in self.body[1:]:
            b.draw(display)
