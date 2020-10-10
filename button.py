import pygame as py

import settings

class Button():
    def __init__(self, shape, text, action, pos):
        self.surface = py.Surface(shape)
        self.surface.fill(py.Color('white'))
        py.draw.rect(self.surface, py.Color('black'), self.surface.get_rect(), 3)
        self.text = settings.text_surface(text, surf_shape=shape, size=min(shape))
        self.surface.blit(self.text, (0, 0))
        self.action = action
        self.position = pos

    def click(self, pos):
        if self.surface.get_rect().move(self.position).collidepoint(pos):
            self.action()

    def draw(self, display):
        display.blit(self.surface, self.position)
