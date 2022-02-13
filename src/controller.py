import pygame
from pygame import QUIT, K_UP, K_DOWN


class Controller:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg
        self.racket1_up = False
        self.racket1_down = False

    def init(self):
        for events in self.pg.event.get():
            if events.type == QUIT:
                pygame.quit()
                exit()
            elif events.type == self.pg.KEYDOWN:
                if events.key == K_UP:
                    self.racket1_up = True
                elif events.key == K_DOWN:
                    self.racket1_down = True
            if events.type == self.pg.KEYUP:
                if events.key == K_UP:
                    self.racket1_up = False
                elif events.key == K_DOWN:
                    self.racket1_down = False

    def get_racket_up(self):
        return self.racket1_up

    def get_racket_down(self):
        return self.racket1_down
