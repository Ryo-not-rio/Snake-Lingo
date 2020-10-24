import pygame as py

import settings

def normalize(data, lower, upper):
    minimum = min(data)
    maximum = max(data) + 0.0000000001
    a = (upper-lower)/(maximum-minimum)
    b = upper - a * maximum
    return list(map(lambda x: a * x + b, data))


def draw_graph(surface, x, y, colour=py.Color('white')):
    x = normalize(x, 0, surface.get_width())
    y = normalize(y, 1, surface.get_height())
    for i in range(len(x)-1):
        x_cor1 = int(x[i])
        y_cor1 = int(surface.get_height() - y[i])
        x_cor2 = int(x[i+1])
        y_cor2 = int(surface.get_height() - y[i+1])
        py.draw.line(surface, colour, (x_cor1, y_cor1), (x_cor2, y_cor2))


class Stats:
    def __init__(self):
        self.events = [[]]
        self.allowed_events = ["correct", "learnt", "snake_len"]
        self.keys = ["Correct Rate", "Learnt words", "Snake length"]
        self.non_show = ["wrong"]
        self.average_list = ["correct"]
        self.colours = [py.Color('blue'), py.Color('darkgreen'), py.Color('limegreen')]

    def get_count(self, event_string):
        c = 0
        for event in self.events:
            c += event.count(event_string)
        return c

    def get_Ys(self):
        Ys = {w:[0] for w in self.allowed_events}
        Ys['snake_len'] = [1]

        currents = {w:0 for w in self.allowed_events}
        currents['snake_len'] = 1
        
        total = 0
        for event in self.events:
            total += 1
            for w in self.non_show + self.allowed_events:
                if w in event:
                    if w == "correct":
                        currents['snake_len'] += 1
                    elif w == "wrong" and currents['snake_len'] > 1:
                        currents['snake_len'] -= 1

                    if w not in self.non_show:
                        currents[w] += 1

                if w not in self.non_show:
                    add_value = currents[w]/total if w in self.average_list else currents[w]
                    Ys[w].append(add_value)

        return Ys
    

    def get_surf(self, shape=(800, 800)):
        key_height = 30

        back_surf = py.Surface(shape, py.SRCALPHA)
        padding = 20
        text_width = shape[0]/len(self.allowed_events) - padding
        for i, t in enumerate(self.allowed_events):
            t_surf = settings.text_surface(self.keys[i], size=text_width, surf_shape=(int(text_width), key_height), colour=self.colours[i])
            back_surf.blit(t_surf, (int(i*(text_width+padding)), 0))

        surf = py.Surface((shape[0], shape[1]-key_height))
        surf.fill(py.Color('white'))

        x = range(len(self.events))
        Ys = self.get_Ys()
        #print(Ys['snake_len'])
        for i, y in enumerate(list(Ys.values())):
            if len(x) > 0 and len(y) > 0:    
                draw_graph(surf, x, y, self.colours[i])
            i += 1

        back_surf.blit(surf, (0, key_height))

        return back_surf
        

if __name__ == "__main__":
    py.init()
    display = py.display.set_mode((800, 800))
    x = range(0, 10)
    y = [n**2 for n in x]
    draw_graph(display, x, y)
    while True:
        py.display.update()