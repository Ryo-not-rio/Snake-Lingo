import pygame as py

import settings
import screen

class GameOver(screen.Screen) :
    def __init__(self):
        super().__init__()
        text_size = settings.BLOCK_SIZE * 5
        pos = int((settings.DISPLAY_SIZE - text_size)/2)
        self.objects.append((settings.text_surface("GameOver", surf_size=text_size, size=text_size, bold=True), (pos, pos)))