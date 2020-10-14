import pygame as py
import time
import random

import settings
import snake
import apple
import words
import gameover
import main_menu

py.init()

display = py.display.set_mode(settings.DISPLAY_SIZE)
clock = py.time.Clock()

# TODO :: Main menu
# TODO :: TTS
# TODO :: Variable speed
# TODO :: change colour of snake & show correct answer
# TODO :: Sound & Music


class Main:
    def __init__(self, language="English"):
        self.game_exit = False
        # 0: main menu, 1: game, 2: gameover
        self.game_state = 0
        self.prev_move = time.time()

        self.grid = [[False for j in range(settings.NUM_ROWS)] for i in range(settings.NUM_COLUMNS)]

        self.language = language
        self.word_generator = words.WordGenerator(self.language)
        self.word, self.answer = "temp", "temp"
        self.apple_num = 3
        self.apples = []
        self.reset_apples()
        self.directions = []
        self.snake_obj = snake.Snake(self.word, self.grid)

        self.game_over_screen = gameover.GameOver()
        self.main_menu_screen = main_menu.MainMenu()


    def reset_apples(self):
        self.apples = []
        coordinates = []
        word, answer = self.word_generator.get_word()
        self.word, self.answer = word, answer
        for i in range(self.apple_num):
            ap = apple.Apple(answer, self.grid)
            while ap.position in coordinates:
                ap = apple.Apple(answer, self.grid)
            coordinates.append(ap.position)
            self.apples.append(ap)
            word, answer = self.word_generator.get_word()


    def each_move(self):
        if self.directions:
            self.snake_obj.change_directions(self.directions[-1])
            self.directions = []

        ## moving ##
        game_over = self.snake_obj.move()
        if game_over:
            self.game_state = 2
            return

        ## apples ##
        for apple_obj in self.apples:
            ### Eating ###
            if self.grid[apple_obj.position[0]][apple_obj.position[1]]:
                correct = apple_obj.text == self.answer
                self.snake_obj.eat(self.word, correct)
                self.reset_apples()
                self.snake_obj.change_text(self.word)

                break
        self.prev_move = time.time()

    def main(self):
        while not self.game_exit:
            for event in py.event.get():
                if event.type == py.QUIT:
                    self.game_exit = True

                if event.type == py.KEYDOWN:
                    if event.key in [py.K_LEFT, py.K_a]:
                        self.directions.append((-1, 0))
                    if event.key in [py.K_RIGHT, py.K_d]:
                        self.directions.append((1, 0))
                    if event.key in [py.K_UP, py.K_w]:
                        self.directions.append((0, -1))
                    if event.key in [py.K_DOWN, py.K_s]:
                        self.directions.append((0, 1))

                if event.type == py.MOUSEBUTTONUP:
                    pos = py.mouse.get_pos()
                    if self.game_state == 2:
                        game_over = self.game_over_screen.click(pos)
                        if not game_over:
                            self.__init__(self.language)
                            self.game_state = 0
                    elif self.game_state == 0:
                        lang = self.main_menu_screen.click(pos)
                        if lang is not None:
                            self.__init__(lang)
                            self.game_state = 1

            if self.game_state == 0:
                self.main_menu_screen.draw(display)  
            elif self.game_state == 1:
                if time.time() - self.prev_move > 1/settings.MOVES_PER_SECOND:
                    self.each_move()

                self.snake_obj.animate()

                ### Drawing ###
                display.fill(py.Color('white'))
                for i in range(settings.NUM_ROWS):
                    py.draw.line(display, py.Color('gray'), (0, i*settings.BLOCK_SIZE), (settings.DISPLAY_SIZE[0], i*settings.BLOCK_SIZE))
                for i in range(settings.NUM_COLUMNS):
                    py.draw.line(display, py.Color('gray'), (i*settings.BLOCK_SIZE, settings.DISPLAY_SIZE[1]), (i*settings.BLOCK_SIZE, 0))

                
                for apple_obj in self.apples:
                    apple_obj.draw(display)

                self.snake_obj.draw(display)
            elif self.game_state == 2:
                self.game_over_screen.draw(display)

            py.display.update()
            clock.tick(settings.FPS)

        py.quit()
        quit()


if __name__ == "__main__":
    Main().main()