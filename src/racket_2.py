import pygame


class Racket2:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg
        self.posX = 580
        self.posY = 180
        self.width = 10
        self.height = 40

    def draw(self, screen, posY: int = None):
        self.posY = posY if posY is not None else self.posY
        self.pg.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.width, self.height))
