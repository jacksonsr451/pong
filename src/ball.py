import pygame


class Ball:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg

    def draw(self, screen):
        self.pg.draw.circle(screen, (255, 255, 255), (300, 200), 5)
