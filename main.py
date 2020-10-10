import pygame as py
import time
import random

import settings
import snake
import apple
import words
import gameover

py.init()

display = py.display.set_mode((settings.DISPLAY_SIZE, settings.DISPLAY_SIZE))
clock = py.time.Clock()

game_exit = False
game_over = False
prev_move = time.time()

grid = [[False for j in range(settings.NUM_ROWS_COLUMNS)] for i in range(settings.NUM_ROWS_COLUMNS)]

language = "Spanish"
word_generator = words.WordGenerator(language)
word, answer = word_generator.get_word()
snake_obj = snake.Snake(word, grid)
apples = [apple.Apple(answer, grid)]
directions = []

game_over_screen = gameover.GameOver()

def initialize():
    global game_exit
    global game_over
    global prev_move
    global grid
    global language
    global word
    global answer
    global snake_obj
    global apples
    global directions
    global game_over_screen

    game_exit = False
    game_over = False
    prev_move = time.time()

    grid = [[False for j in range(settings.NUM_ROWS_COLUMNS)] for i in range(settings.NUM_ROWS_COLUMNS)]

    language = "Spanish"
    word_generator = words.WordGenerator(language)
    word, answer = word_generator.get_word()
    snake_obj = snake.Snake(word, grid)
    apples = [apple.Apple(answer, grid)]
    directions = []

    game_over_screen = gameover.GameOver()

def each_move():
    global directions
    global snake_obj
    global game_over
    global word
    global answer
    global apples
    global prev_move

    if directions:
        snake_obj.change_directions(directions[-1])
        directions = []

    ## moving ##
    game_over = snake_obj.move()
    if game_over:
        return

    ## apples ##
    for apple_obj in apples:
        if grid[apple_obj.position[0]][apple_obj.position[1]]:
            snake_obj.eat(word)
            word, answer = word_generator.get_word()
            snake_obj.change_text(word)
            apple_obj.__init__(answer, grid)
            break
    prev_move = time.time()

while not game_exit:
    for event in py.event.get():
        if event.type == py.QUIT:
            game_exit = True

        if event.type == py.KEYDOWN:
            if event.key in [py.K_LEFT, py.K_a]:
                directions.append((-1, 0))
            if event.key in [py.K_RIGHT, py.K_d]:
                directions.append((1, 0))
            if event.key in [py.K_UP, py.K_w]:
                directions.append((0, -1))
            if event.key in [py.K_DOWN, py.K_s]:
                directions.append((0, 1))

        if event.type == py.MOUSEBUTTONUP:
            if game_over:
                pos = py.mouse.get_pos()
                game_over = game_over_screen.click(pos)
                if not game_over:
                    initialize()

        
    if not game_over:
        if time.time() - prev_move > 1/settings.MOVES_PER_SECOND:
            each_move()

        snake_obj.animate()

        ### Drawing ###
        display.fill(py.Color('white'))
        for i in range(settings.NUM_ROWS_COLUMNS):
            py.draw.line(display, py.Color('gray'), (i*settings.BLOCK_SIZE, settings.DISPLAY_SIZE), (i*settings.BLOCK_SIZE, 0))
            py.draw.line(display, py.Color('gray'), (0, i*settings.BLOCK_SIZE), (settings.DISPLAY_SIZE, i*settings.BLOCK_SIZE))

        
        for apple_obj in apples:
            apple_obj.draw(display)

        snake_obj.draw(display)
    else:
        game_over_screen.draw(display)

    py.display.update()
    clock.tick(settings.FPS)

py.quit()
quit()