import pygame as py
import numpy as np
import os
import pyttsx3
import threading
import random

import settings
import words


tts = pyttsx3.init()


head_imgs = [settings.load_img("snake_head{}.png".format(n), (settings.BLOCK_SIZE, settings.BLOCK_SIZE)) for n in range(1, 8)]
body_img = py.image.load(os.path.join("images", "snake_body.png"))
body_img = py.transform.scale(body_img, (settings.BLOCK_SIZE, settings.BLOCK_SIZE))

class SnakeBod:
    def __init__(self, text, position, rotation, velocity, img=None, bold=False, text_size=settings.BLOCK_SIZE):
        self.img = img
        self.text = text
        self.text_size = text_size
        self.bold = bold
        self.create_surface()
        if img in head_imgs:
            self.change_img()
        self.rotation = rotation
        self.position = position
        self.prev_pos = position
        self.pixel_position = settings.grid_to_pos(self.position)
        self.pixel_wait = 0
        self.vel = velocity

    def create_surface(self):
        self.original_surface = py.Surface((settings.BLOCK_SIZE, settings.BLOCK_SIZE), py.SRCALPHA)
        if self.img is not None:
            self.img = self.img.convert_alpha()
            self.original_surface.blit(self.img, (0, 0))
        
        try:
            self.original_surface.blit(settings.text_surface(self.text, size=self.text_size, bold=self.bold), (0, 0))
        except py.error:
            pass

    def collide(self, pos):
        return self.position == list(pos)

    def change_text(self, text):
        self.text = text
        self.create_surface()

    def change_img(self):
        self.img = random.choice(head_imgs)
        self.create_surface()
        timer = threading.Timer(1, self.change_img)
        timer.start()

    def draw(self, display):
        display.blit(py.transform.rotate(self.original_surface, self.rotation), [int(c) for c in self.pixel_position])

class Snake():
    def __init__(self, text, grid):
        self.grid = grid
        initial_pos = (5, 5)
        self.bodies = [SnakeBod(text, initial_pos, 0, (0, 0), img=head_imgs[0], bold=True)]
        self.grid[initial_pos[0]][initial_pos[1]] = True
        self.head = self.bodies[0]
        self.waited = False
        self.rotations = []

    def length(self):
        return len(self.bodies)

    def move(self):
        for i in range(0, len(self.bodies)-1):
            index = len(self.bodies)-1-i
            bod = self.bodies[index]

            if i==0:
                self.grid[bod.position[0]][bod.position[1]] = False

            
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
                
        ### Moving head ###
        if len(self.bodies) == 1:
            self.grid[self.head.position[0]][self.head.position[1]] = False
        self.head.position = list(np.array(self.head.position) + np.array(self.head.vel))

        ### Check if gameover ###        
        if self.head.position[0] < 0 or \
            self.head.position[0] >= settings.NUM_COLUMNS or \
            self.head.position[1] < 0 or \
            self.head.position[1] >= settings.NUM_ROWS:
            return True

        if self.grid[self.head.position[0]][self.head.position[1]]:
            return True
        ############################
        
        self.grid[self.head.position[0]][self.head.position[1]] = True
        return False

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

    def eat(self, text, correct):
        tail = self.bodies[-1]
        pos = tail.position[:]
        if correct:
            self.bodies.append(SnakeBod(text, pos, tail.rotation, tail.vel[:], img=body_img, text_size=int(settings.BLOCK_SIZE*0.7)))
            self.grid[pos[0]][pos[1]] = correct
        else:
            if len(self.bodies) > 1:
                del self.bodies[-1]
                self.grid[pos[0]][pos[1]] = correct

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
