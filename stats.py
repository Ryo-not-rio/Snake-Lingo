import pygame as py

def normalize(data, lower, upper):
    minimum = min(data)
    maximum = max(data) + 0.0000000001
    a = (upper-lower)/(maximum-minimum)
    b = upper - a * maximum
    return list(map(lambda x: a * x + b, data))


def draw_graph(surface, x, y, colour=py.Color('white')):
    x = normalize(x, 0, surface.get_width())
    y = normalize(y, 0, surface.get_height())
    for i in range(len(x)-1):
        x_cor1 = int(x[i])
        y_cor1 = int(surface.get_height() - y[i])
        x_cor2 = int(x[i+1])
        y_cor2 = int(surface.get_height() - y[i+1])
        py.draw.line(surface, colour, (x_cor1, y_cor1), (x_cor2, y_cor2))


class Stats:
    def __init__(self):
        self.events = []

    def get_y(self, target_word):
        y = []

        current = 0
        total = 0
        for e in self.events:
            total += 1
            if target_word in e:
                current += 1
            y.append(current/total)

        return y

    def get_surf(self, shape=(800, 800)):
        surf = py.Surface(shape)
        surf.fill(py.Color('white'))

        x = range(len(self.events))
        y = self.get_y("correct")

        if len(x) == 0 or len(y) == 0:
            return surf
        
        draw_graph(surf, x, y, py.Color('blue'))
        return surf
        

if __name__ == "__main__":
    py.init()
    display = py.display.set_mode((800, 800))
    x = range(0, 10)
    y = [n**2 for n in x]
    draw_graph(display, x, y)
    while True:
        py.display.update()