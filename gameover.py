import pygame as py

import settings
import screen
import button

class GameOver(screen.Screen) :
    def __init__(self):
        super().__init__()
        text_size = settings.BLOCK_SIZE * 5
        pos = int((settings.DISPLAY_SIZE - text_size)/2)
        self.surface.blit(settings.text_surface("GameOver", surf_shape=(text_size, text_size), size=text_size, bold=True), (pos, pos))
        but = button.Button((100, 50), "Click", lambda: print("here"), (100, 100))
        self.objects.append(but)