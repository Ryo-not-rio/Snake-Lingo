import pygame as py
import random
import os

import settings

img = py.image.load(os.path.join("images", "apple.png"))
img = py.transform.scale(img, (settings.BLOCK_SIZE, settings.BLOCK_SIZE))
# img = img.convert()
# display.blit(img, position)
correct_img = py.image.load(os.path.join("images", "apple_correct.png"))
correct_img = py.transform.scale(correct_img, (settings.BLOCK_SIZE, settings.BLOCK_SIZE))

class Apple:
    def __init__(self, text, grid):
        self.text = text
        self.surface = img.convert_alpha()
        self.surface.blit(settings.text_surface(text), (0, 0))
        self.position = (random.randint(0, settings.NUM_COLUMNS-1), random.randint(0, settings.NUM_ROWS-1))
        while grid[self.position[0]][self.position[1]]:
            self.position = (random.randint(0, settings.NUM_COLUMNS-1), random.randint(0, settings.NUM_ROWS-1))


    def draw(self, display):
        # display.blit(self.img, settings.grid_to_pos(self.position))
        display.blit(self.surface, settings.grid_to_pos(self.position))

    
    def change_img(self):
        self.surface = correct_img.convert_alpha()
        self.surface.blit(settings.text_surface(self.text), (0, 0))