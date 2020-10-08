import pygame as py
import numpy as np

import settings


class SnakeBod:
    def __init__(self, text, position, rotation, velocity):
        self.original_surface = settings.text_surface(text)
        self.rotation = rotation
        self.position = position
        self.vel = velocity

    def collide(self, pos):
        return self.position == pos

    def draw(self, display):
        display.blit(py.transform.rotate(self.original_surface, self.rotation), settings.grid_to_pos(self.position))


class Snake():
    def __init__(self):
        self.bodies = [SnakeBod("Hello", (9, 9), 0, (0, 0))]
        self.head = self.bodies[0]
        self.changed = False
    
    def move(self):
        for i in range(0, len(self.bodies)-1):
            index = len(self.bodies)-1-i
            bod = self.bodies[index]
            prev = self.bodies[index-1]
            bod.position = prev.position[:]
            bod.vel = prev.vel[:]
            
            if not self.changed or prev != self.head:
                bod.rotation = prev.rotation
            else:
                self.changed = False
        
        self.head.position = list(np.array(self.head.position) + np.array(self.head.vel))
        if self.head.position[0] < 0:
            self.head.position[0] = settings.NUM_ROWS_COLUMNS-1
        if self.head.position[0] >= settings.NUM_ROWS_COLUMNS:
            self.head.position[0] = 0
        if self.head.position[1] < 0:
            self.head.position[1] = settings.NUM_ROWS_COLUMNS-1
        if self.head.position[1] >= settings.NUM_ROWS_COLUMNS:
            self.head.position[1] = 0

    def change_directions(self, direction):
        if direction is not None:
            direction_arr = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
            ind = direction_arr.index(direction)
            new_vel = direction_arr[ind]
            if (np.multiply(np.array(new_vel), np.array(self.head.vel)) == np.array((0, 0))).all():
                self.head.vel = new_vel
                self.head.rotation = -90*(ind % 4)
                self.changed = True

    def eat(self):
        tail = self.bodies[-1]
        self.bodies.append(SnakeBod("-", tail.position[:], tail.rotation, tail.vel[:]))

    def collide(self, pos):
        collided = False
        for bod in self.bodies:
            collided = collided and bod.collide(pos)
        return collided

    def draw(self, display):
        for b in self.bodies:
            b.draw(display)
