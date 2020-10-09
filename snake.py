import pygame as py
import numpy as np

import settings


class SnakeBod:
    def __init__(self, text, position, rotation, velocity, bold=False, text_size=settings.BLOCK_SIZE):
        self.original_surface = settings.text_surface(text, size=text_size, bold=bold)
        self.text_size = text_size
        self.bold = bold
        self.rotation = rotation
        self.position = position
        self.prev_pos = position
        self.pixel_position = settings.grid_to_pos(self.position)
        self.pixel_wait = 0
        self.vel = velocity

    def collide(self, pos):
        return self.position == list(pos)

    def change_text(self, text):
        self.original_surface = settings.text_surface(text, size=self.text_size, bold=self.bold)

    def draw(self, display):
        display.blit(py.transform.rotate(self.original_surface, self.rotation), [int(c) for c in self.pixel_position])


class Snake():
    def __init__(self, text):
        self.bodies = [SnakeBod(text, (5, 5), 0, (0, 0), bold=True)]
        self.head = self.bodies[0]
        self.waited = False
        self.rotations = []
    
    def move(self):
        for i in range(0, len(self.bodies)-1):
            index = len(self.bodies)-1-i
            bod = self.bodies[index]
            bod.prev_pos = bod.position[:]
            prev = self.bodies[index-1]
            bod.position = prev.position[:]

            if prev != self.head:
                bod.rotation = prev.rotation
            elif self.rotations:
                if self.waited:
                    bod.rotation = self.rotations.pop(0)
                    if not self.rotations:
                        self.waited = False
                else:
                    self.waited = True
                
        
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
                if len(self.bodies) > 1:
                    self.rotations.append(self.head.rotation)

    def eat(self, text="|"):
        tail = self.bodies[-1]
        self.bodies.append(SnakeBod(text, tail.position[:], tail.rotation, tail.vel[:], text_size=int(settings.BLOCK_SIZE*0.7)))

    def collide(self, pos):
        collided = False
        for bod in self.bodies:
            collided = collided or bod.collide(pos)
            if collided:
                break
        return collided

    def change_text(self, text):
        self.bodies[0].change_text(text)

    def animate(self):
        pixel = settings.BLOCK_SIZE/(settings.FPS/settings.MOVES_PER_SECOND)
        for i in range(0, len(self.bodies)):
            bod = self.bodies[i]
            if bod == self.head:
                vel = bod.vel
            else:
                vel = list(np.array(bod.position) - np.array(bod.prev_pos))
            if bod == self.head or bod.pixel_wait >= settings.FPS/settings.MOVES_PER_SECOND:
                new_pos = np.array(bod.pixel_position) + np.multiply(np.array(vel), np.array((pixel, pixel)))
                if vel[0] == 0:
                    new_pos[0] = settings.BLOCK_SIZE * bod.position[0]
                if vel[1] == 0:
                    new_pos[1] = settings.BLOCK_SIZE * bod.position[1]
                bod.pixel_position = list(new_pos)
            else:
                bod.pixel_wait += 1


    def draw(self, display):
        for b in self.bodies:
            b.draw(display)
