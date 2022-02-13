import pygame


class Background:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg

    def draw(self, screen):
        self.pg.draw.rect(screen, (255, 255, 255), (0, 0, 2.5, 400))
        self.pg.draw.rect(screen, (255, 255, 255), (300, 0, 2.5, 400))
        self.pg.draw.rect(screen, (255, 255, 255), (598, 0, 2.5, 400))

        self.pg.draw.rect(screen, (255, 255, 255), (0, 0, 600, 2.5))
        self.pg.draw.rect(screen, (255, 255, 255), (0, 398, 600, 2.5))
