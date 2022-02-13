import pygame


class Racket2:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg
        self.posX = 580
        self.posY = 180
        self.width = 10
        self.height = 40
        self.racket = None

    def draw(self, screen, posY: int = None):
        self.posY = posY if posY is not None else self.posY
        self.racket = self.pg.Rect(self.get_position())
        self.pg.draw.rect(screen, (255, 255, 255), self.racket)

    def get_position(self):
        position = (self.posX, self.posY, self.width, self.height)
        return position

    def get_racket(self):
        return self.racket
