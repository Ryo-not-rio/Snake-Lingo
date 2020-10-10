import pygame as py

import settings
import screen
import button

class GameOver(screen.Screen) :
    def __init__(self):
        super().__init__(alpha=20)
        text_size = settings.BLOCK_SIZE * 5
        x_pos = int((settings.DISPLAY_SIZE - text_size)/2)
        self.surface.blit(settings.text_surface("GameOver", surf_shape=(text_size, int(text_size/2)), size=text_size, bold=True), (x_pos, 100))

        but_shape = (settings.BLOCK_SIZE * 2, settings.BLOCK_SIZE)
        but = button.Button("Play Again!", lambda: False, but_shape, (int((settings.DISPLAY_SIZE - but_shape[0])/2), 400))
        self.objects.append(but)