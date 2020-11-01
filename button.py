import pygame as py
import random

import settings

class Button:
    def __init__(self, text, action, shape, pos, colour=py.Color("black"), back_colour=py.Color("white"), back_img=None):
        self.colour = colour
        self.back_colour = back_colour
        self.surface = py.Surface(shape)
        self.surface.fill(back_colour)

        if back_img is not None:
            print(back_img)
            img = py.image.load(back_img)
            img = py.transform.scale(img, shape).convert()
            img.set_alpha(60)
            self.surface.blit(img, (0, 0))

        py.draw.rect(self.surface, colour, self.surface.get_rect(), 3)
        self.text = settings.text_surface(text, surf_shape=shape, size=max(shape)-4)
        self.surface.blit(self.text, (0, 0))
        self.action = action
        self.position = pos

    def click(self, pos):
        if self.surface.get_rect().move(self.position).collidepoint(pos):
            return self.action()

    def draw(self, display):
        display.blit(self.surface, self.position)


class CustomButton(Button):
    def action(self):
        self.reversed = not self.reversed
        colour = py.Color("white") if self.reversed else py.Color("gray")
        self.surface.fill(colour)
        py.draw.rect(self.surface, self.colour, self.surface.get_rect(), 3)
        self.surface.blit(self.text, (0, 0))

    def click(self, pos):
        if self.surface.get_rect().move(self.position).collidepoint(pos):
            self.action()

    def __init__(self, text, shape, pos, colour=py.Color("blue"), back_colour=py.Color("gray")):
        self.colour = colour
        self.back_colour = back_colour
        self.surface = py.Surface(shape)
        self.surface.fill(back_colour)
        py.draw.rect(self.surface, colour, self.surface.get_rect(), 3)
        self.text = settings.text_surface(text, surf_shape=shape, size=max(shape)-4)
        self.surface.blit(self.text, (0, 0))
        self.position = pos
        self.reversed = False
        
