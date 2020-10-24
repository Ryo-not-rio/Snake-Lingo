import pygame as py
import numpy as np
import os

py.font.init()

DISPLAY_SIZE = (1000, 800)
BLOCK_SIZE = 100
NUM_ROWS = int(DISPLAY_SIZE[1]/BLOCK_SIZE)
NUM_COLUMNS = int(DISPLAY_SIZE[0]/BLOCK_SIZE)
FONT = py.font.SysFont('arial_unicode', 140)
FONT2 = py.font.SysFont('arial_unicode_bold', 140)
MOVES_PER_SECOND = 2
FPS = 60

def grid_to_pos(grid_pos):
    return [BLOCK_SIZE*i for i in grid_pos]

def text_surface(text, surf_shape=(BLOCK_SIZE, BLOCK_SIZE), size=BLOCK_SIZE, bold=False, colour=py.Color('black')):
    text = text
    if bold:
        surface = FONT2.render(text, False, colour)
    else:
        surface = FONT.render(text, False, colour)
    surface_size = surface.get_size()
    ratio = min(np.array((size, size))/np.array(surface_size))
    new_size = np.array(surface_size) * ratio
    text_surface = py.transform.scale(surface, list(new_size.astype(int)))
    return_surface = py.Surface(surf_shape, py.SRCALPHA)
    position_in_return_surface = list(((np.array(return_surface.get_size())-np.array(text_surface.get_size()))/2).astype(int))
    return_surface.blit(text_surface, position_in_return_surface)
    return return_surface


def load_img(file, shape):
    img = py.image.load(os.path.join("images", file))
    img = py.transform.scale(img, shape)
    return img

