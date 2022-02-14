import pygame
from pygame import QUIT, K_UP, K_DOWN


class Controller:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg

    def init(self):
        for events in self.pg.event.get():
            if events.type == QUIT:
                pygame.quit()
                exit()
