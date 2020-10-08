import pygame as py
import settings
import snake
import time

py.init()

display = py.display.set_mode((settings.DISPLAY_SIZE, settings.DISPLAY_SIZE))
clock = py.time.Clock()

gameExit = False
prev_move = time.time()
snake = snake.Snake()

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
        display.fill(py.Color('black'))

        # Draw columns and rows
        for i in range(settings.NUM_ROWS_COLUMNS):
            py.draw.line(display, py.Color('white'), (i*settings.BLOCK_SIZE, settings.DISPLAY_SIZE), (i*settings.BLOCK_SIZE, 0))
            py.draw.line(display, py.Color('white'), (0, i*settings.BLOCK_SIZE), (settings.DISPLAY_SIZE, i*settings.BLOCK_SIZE))

        
        if snake.bodies[0].vel != (0, 0):
            snake.eat()
        snake.move()
        
        snake.draw(display)
        prev_move = time.time()

    py.display.update()
    clock.tick(30)

quit()