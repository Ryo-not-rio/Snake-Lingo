import pygame as py
import os

import screen
import button
import words
import settings

back_arrows_img = py.image.load(os.path.join("images", "back_arrows.png"))


class MainMenu(screen.Screen):
    def __init__(self):
        self.back_arrows_img = py.transform.scale(back_arrows_img, settings.DISPLAY_SIZE).convert()

        super().__init__(alpha=30)

        title_shape = (600, 100)
        title_surf = settings.text_surface("Snake-lingo", title_shape, size=title_shape[0], bold=True, colour=py.Color("darkgreen"))
        self.surface.blit(title_surf, (int((settings.DISPLAY_SIZE[0] - title_shape[0])/2), 70))

        shape = (150, 60)
        x = (settings.DISPLAY_SIZE[0] - shape[0])/2
        custom = button.CustomButton("Reverse", shape, (x, 170))
        self.objects.append(custom)


        languages = words.lang_dict

        button_shape = (150, 60)
        num_cols = 5
        full_button_width = settings.DISPLAY_SIZE[0]/num_cols
        button_x_padding = (full_button_width - button_shape[0])

        for i, lang in enumerate(languages.keys()):
            button_x = button_x_padding/2 + (i%num_cols)*(button_shape[0]+button_x_padding)
            button_y = 300 + (button_shape[1]+8)*(i // num_cols)
            img_name = lang+".png"
            btn = button.Button(lang, lambda lang=lang: (lang, custom), button_shape, (button_x, button_y), back_img=os.path.join("images", img_name))
            self.objects.append(btn)
    
    def draw(self, display):
        display.blit(self.back_arrows_img, (0, 0))
        super().draw(display)
