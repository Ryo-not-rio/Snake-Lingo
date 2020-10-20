import pygame as py

import settings
import screen
import button

class Loading(screen.Screen) :
    def __init__(self):
        super().__init__(alpha=20)
        text_size = settings.BLOCK_SIZE * 6
        x_pos = int((settings.DISPLAY_SIZE[0] - text_size)/2)
        y_pos = int((settings.DISPLAY_SIZE[1] - text_size)/2)
        self.surface.blit(settings.text_surface("Loading...", surf_shape=(text_size, int(text_size/2)), size=text_size, bold=True), (x_pos, y_pos))