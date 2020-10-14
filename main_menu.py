import pygame as py
from copy import deepcopy

import screen
import button
import words

class MainMenu(screen.Screen):
    def __init__(self):
        super().__init__()
        languages = words.lang_dict
        self.objects = []

        button_shape = (80, 40)
        for i, lang in enumerate(languages.keys()):
            self.objects.append(button.Button(lang, lambda lang=lang: lang, button_shape, ((i%5)*button_shape[0], 100 + 40*(i // 5))))
