import pygame as py
import numpy as np

py.font.init()

DISPLAY_SIZE = 800
NUM_ROWS_COLUMNS = 8
BLOCK_SIZE = int(DISPLAY_SIZE/NUM_ROWS_COLUMNS)
FONT = py.font.SysFont('arial', 140)
MOVES_PER_SECOND = 2.5

def grid_to_pos(grid_pos):
    return [BLOCK_SIZE*i for i in grid_pos]

def text_surface(text, size=BLOCK_SIZE):
    surface = FONT.render(text, False, py.Color('black'))
    surface_size = surface.get_size()
    ratio = min(np.array((size, size))/np.array(surface_size))
    new_size = np.array(surface_size) * ratio
    text_surface = py.transform.scale(surface, list(new_size.astype(int)))
    return_surface = py.Surface((size, size), py.SRCALPHA)
    position_in_return_surface = list(((np.array(return_surface.get_size())-np.array(text_surface.get_size()))/2).astype(int))
    return_surface.blit(text_surface, position_in_return_surface)
    return return_surface

