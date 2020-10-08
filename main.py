import pygame as py
import settings
import snake

py.init()

display = py.display.set_mode((settings.DISPLAY_SIZE, settings.DISPLAY_SIZE))
clock = py.time.Clock()

gameExit = False
snake = snake.Snake()

while not gameExit:
    for event in py.event.get():
        if event.type == py.QUIT:
            gameExit = True

    # Draw columns and rows
    for i in range(settings.NUM_ROWS_COLUMNS):
        py.draw.line(display, py.Color('white'), (i*settings.BLOCK_SIZE, settings.DISPLAY_SIZE), (i*settings.BLOCK_SIZE, 0))
        py.draw.line(display, py.Color('white'), (0, i*settings.BLOCK_SIZE), (settings.DISPLAY_SIZE, i*settings.BLOCK_SIZE))


    snake.draw(display)
    py.display.update()
    clock.tick(30)

quit()