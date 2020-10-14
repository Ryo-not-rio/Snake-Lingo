import pygame as py

import screen
import button
import words
import settings

class MainMenu(screen.Screen):
    def __init__(self):
        super().__init__()
        languages = words.lang_dict

        title_shape = (600, 100)
        title_surf = settings.text_surface("Snake thing", title_shape, size=title_shape[0], bold=True)
        self.surface.blit(title_surf, (int((settings.DISPLAY_SIZE[0] - title_shape[0])/2), 70))

        self.objects = []

        button_shape = (150, 60)
        num_cols = 5
        full_button_width = settings.DISPLAY_SIZE[0]/num_cols
        button_x_padding = (full_button_width - button_shape[0])

        for i, lang in enumerate(languages.keys()):
            button_x = button_x_padding/2 + (i%num_cols)*(button_shape[0]+button_x_padding)
            button_y = 300 + (button_shape[1]+8)*(i // num_cols)
            self.objects.append(button.Button(lang, lambda lang=lang: lang, button_shape, (button_x, button_y)))
