import pygame as py

size = (800, 800)
display = py.display.set_mode(size)

gameExit = False

while not gameExit:
    for event in py.event.get():
        if event.type == py.QUIT:
            gameExit = True
    
    py.display.update()

quit()