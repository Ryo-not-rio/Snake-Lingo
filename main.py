import pygame as py
import time
import random
import os
import threading

import settings
import snake
import apple
import words
import gameover
import main_menu
import loading
import stats

py.mixer.init(buffer=64)
py.init()

display = py.display.set_mode(settings.DISPLAY_SIZE)
clock = py.time.Clock()


correct_sound = py.mixer.Sound(os.path.join("sounds", "correct.wav"))
wrong_sound = py.mixer.Sound(os.path.join("sounds", "wrong.wav"))
turn_sound = py.mixer.Sound(os.path.join("sounds", "turn.wav"))

music = py.mixer.music.load(os.path.join("sounds", "music.mp3"))
py.mixer.music.set_volume(0.8)
py.mixer.music.play(-1)

back_img = py.image.load(os.path.join("images", "back.png"))
back_img = py.transform.scale(back_img, settings.DISPLAY_SIZE).convert()

class Main:
    def __init__(self, language=None, reversed_btn=None):
        settings.MOVES_PER_SECOND = 2

        reversed = False
        if reversed_btn is not None:
            reversed = reversed_btn.reversed

        self.game_exit = False
        # 0: main menu, 1: game, 2: gameover
        self.game_state = 0
        self.prev_move = time.time()

        self.grid = [[False for j in range(settings.NUM_ROWS)] for i in range(settings.NUM_COLUMNS)]

        self.stats_collector = stats.Stats()

        self.language = language
        if language is not None:
            self.word_generator = words.WordGenerator(self.language, self.stats_collector, reversed)
        self.word, self.answer = "Temp", "Temp"
        self.apple_num = 3
        self.apples = []
        self.temp_apple = None
        self.temp_start = None

        
        if language is not None:
            self.grid[5][5] = True
            self.reset_apples()
        self.snake_obj = snake.Snake(self.word, self.grid)
        self.directions = []
        

        self.game_over_screen = gameover.GameOver(self.stats_collector)
        self.main_menu_screen = main_menu.MainMenu()
        self.loading_screen = loading.Loading()


    def reset_apples(self):
        self.apples = []
        coordinates = []
        word, answer = self.word_generator.get_word(answer=True)
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
            py.mixer.Sound.play(turn_sound)
            self.snake_obj.change_directions(self.directions[-1])
            self.directions = []

        ## moving ##
        game_over = self.snake_obj.move()
        if game_over:
            py.mixer.Sound.play(wrong_sound)
            self.game_state = 2
            return

        ## apples ##
        for apple_obj in self.apples:
            ### Eating ###
            if self.grid[apple_obj.position[0]][apple_obj.position[1]]:
                correct = apple_obj.text == self.answer
                self.snake_obj.eat(self.word, correct)
                ### Correct ###
                if correct:
                    py.mixer.Sound.play(correct_sound)
                    self.word_generator.correct(self.word)
                    if settings.NUM_ROWS*settings.NUM_COLUMNS - self.snake_obj.length() == 0:
                        # Max Length
                        self.game_state = 2
                    if settings.NUM_ROWS*settings.NUM_COLUMNS - self.snake_obj.length() < self.apple_num:
                        self.apple_num = settings.NUM_ROWS*settings.NUM_COLUMNS - self.snake_obj.length()
                    if self.snake_obj.length() % 10 == 0:
                        settings.MOVES_PER_SECOND += 0.3
                else:
                    py.mixer.Sound.play(wrong_sound)
                    self.word_generator.wrong(self.word)
                    self.temp_apple = self.apples[0]
                    self.temp_apple.change_img()
                    self.temp_start = time.time()

                self.reset_apples()
                self.snake_obj.change_text(self.word)

                break
        self.prev_move = time.time()

    def draw(self):
        display.blit(back_img, (0, 0))
        if self.game_state == 0:
            self.main_menu_screen.draw(display)  
        elif self.game_state == 1:
            if time.time() - self.prev_move > 1/settings.MOVES_PER_SECOND:
                self.each_move()

            self.snake_obj.animate()

            for i in range(settings.NUM_ROWS):
                py.draw.line(display, py.Color('gray'), (0, i*settings.BLOCK_SIZE), (settings.DISPLAY_SIZE[0], i*settings.BLOCK_SIZE))
            for i in range(settings.NUM_COLUMNS):
                py.draw.line(display, py.Color('gray'), (i*settings.BLOCK_SIZE, settings.DISPLAY_SIZE[1]), (i*settings.BLOCK_SIZE, 0))

            
            for apple_obj in self.apples:
                apple_obj.draw(display)

            self.snake_obj.draw(display)

            if self.temp_apple is not None:
                self.temp_apple.draw(display)
                if time.time() - self.temp_start > 1.5:
                    self.temp_apple = None

        elif self.game_state == 2:
            self.game_over_screen.draw(display)


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
                        again = self.game_over_screen.click(pos)
                        if again is not None:
                            self.__init__(None)
                            self.game_state = 0
                    elif self.game_state == 0:
                        lang = self.main_menu_screen.click(pos)
                        if lang is not None:
                            ### Start Game ###
                            display.blit(back_img, (0, 0))
                            self.loading_screen.draw(display)
                            py.display.update()
                            self.__init__(lang[0], lang[1])
                            self.game_state = 1


            ### Drawing ###
            self.draw()
            
            py.display.update()
            clock.tick(settings.FPS)

        py.quit()
        quit()


if __name__ == "__main__":
    Main().main()