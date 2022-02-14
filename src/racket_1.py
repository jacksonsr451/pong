import pygame
from pygame import K_UP, K_DOWN


class Racket1:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg
        self.posX = 10
        self.posY = 180
        self.width = 10
        self.height = 40
        self.racket = None

        self.keys = None

    def draw(self, screen, speed, keys):
        self.keys = keys
        self.racket = self.pg.Rect(self.get_position())
        self.pg.draw.rect(screen, (255, 255, 255), self.racket)
        self.__set_pos_y(screen=screen, speed=speed)

    def __set_pos_y(self, screen, speed):
        x, y = screen.get_size()
        if self.posY > 0:
            if self.keys[K_UP]:
                self.posY -= speed
        if self.posY < y - 40:
            if self.keys[K_DOWN]:
                self.posY += speed

    def get_position(self):
        position = (self.posX, self.posY, self.width, self.height)
        return position

    def get_racket(self):
        return self.racket
