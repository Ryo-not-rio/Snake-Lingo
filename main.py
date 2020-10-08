import pygame as py
import time
import random

import settings
import snake
import apple
import words

py.init()

display = py.display.set_mode((settings.DISPLAY_SIZE, settings.DISPLAY_SIZE))
clock = py.time.Clock()

gameExit = False
prev_move = time.time()

language = "Spanish"
word, answer = words.get_word(language)
snake = snake.Snake(word)
apples = [apple.Apple(answer, snake)]

while not gameExit:
    for event in py.event.get():
        if event.type == py.QUIT:
            gameExit = True
        if event.type == py.KEYDOWN:
            if event.key in [py.K_LEFT, py.K_a]:
                snake.change_directions((-1, 0))
            if event.key in [py.K_RIGHT, py.K_d]:
                snake.change_directions((1, 0))
            if event.key in [py.K_UP, py.K_w]:
                snake.change_directions((0, -1))
            if event.key in [py.K_DOWN, py.K_s]:
                snake.change_directions((0, 1))

    ### Drawing ###
    if time.time() - prev_move > 1/settings.MOVES_PER_SECOND:
        display.fill(py.Color('white'))

        # Draw columns and rows
        for i in range(settings.NUM_ROWS_COLUMNS):
            py.draw.line(display, py.Color('gray'), (i*settings.BLOCK_SIZE, settings.DISPLAY_SIZE), (i*settings.BLOCK_SIZE, 0))
            py.draw.line(display, py.Color('gray'), (0, i*settings.BLOCK_SIZE), (settings.DISPLAY_SIZE, i*settings.BLOCK_SIZE))
        
        snake.move()
        for apple in apples:
            if snake.collide(apple.position):
                snake.eat(answer)
                word, answer = words.get_word(language)
                snake.change_text(word)
                apple.__init__(answer, snake)
                break
        
        apple.draw(display)
        snake.draw(display)
        prev_move = time.time()

    py.display.update()
    clock.tick(30)

quit()