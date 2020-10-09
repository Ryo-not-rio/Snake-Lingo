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
directions = []

while not gameExit:
    for event in py.event.get():
        if event.type == py.QUIT:
            gameExit = True
        if event.type == py.KEYDOWN:
            if event.key in [py.K_LEFT, py.K_a]:
                directions.append((-1, 0))
            if event.key in [py.K_RIGHT, py.K_d]:
                directions.append((1, 0))
            if event.key in [py.K_UP, py.K_w]:
                directions.append((0, -1))
            if event.key in [py.K_DOWN, py.K_s]:
                directions.append((0, 1))
        
    if time.time() - prev_move > 1/settings.MOVES_PER_SECOND:
        if directions:
            snake.change_directions(directions[-1])
        directions = []
        snake.move()
        for apple in apples:
            if snake.collide(apple.position):
                snake.eat(word)
                word, answer = words.get_word(language)
                snake.change_text(word)
                apple.__init__(answer, snake)
                break
        prev_move = time.time()

    snake.animate()

    ### Drawing ###
    display.fill(py.Color('white'))
    for i in range(settings.NUM_ROWS_COLUMNS):
        py.draw.line(display, py.Color('gray'), (i*settings.BLOCK_SIZE, settings.DISPLAY_SIZE), (i*settings.BLOCK_SIZE, 0))
        py.draw.line(display, py.Color('gray'), (0, i*settings.BLOCK_SIZE), (settings.DISPLAY_SIZE, i*settings.BLOCK_SIZE))

    
    for apple in apples:
        apple.draw(display)

    snake.draw(display)

    py.display.update()
    clock.tick(settings.FPS)

quit()