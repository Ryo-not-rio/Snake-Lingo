import pygame as py

import settings
import screen
import button

class GameOver(screen.Screen) :
    def __init__(self, stats_collector):
        super().__init__(alpha=20)
        text_size = settings.BLOCK_SIZE * 5
        x_pos = int((settings.DISPLAY_SIZE[0] - text_size)/2)
        self.surface.blit(settings.text_surface("GameOver", surf_shape=(text_size, int(text_size/4)), size=text_size, bold=True), (x_pos, 10))
        self.stats_collector = stats_collector

        but_shape = (settings.BLOCK_SIZE * 2, settings.BLOCK_SIZE)
        but = button.Button("Play Again!", lambda: True, but_shape, (int((settings.DISPLAY_SIZE[0] - but_shape[0])/2), 600))
        self.objects.append(but)

    def draw(self, display):
        surf_shape = (700, 400)

        pos = (int((settings.DISPLAY_SIZE[0]-surf_shape[0])/2), 180)
        text_size = settings.BLOCK_SIZE * 4
        x_pos = int((settings.DISPLAY_SIZE[0] - text_size)/2)
        learnt_count = self.stats_collector.get_count("learnt")
        self.surface.blit(settings.text_surface("You learned {} words!!".format(learnt_count),
                                                surf_shape=(text_size, int(text_size/3)), 
                                                size=text_size, bold=True,
                                                colour=py.Color('darkorange')),
                                                (x_pos, 80))
        self.surface.blit(self.stats_collector.get_surf(shape=surf_shape), pos)
        super().draw(display)