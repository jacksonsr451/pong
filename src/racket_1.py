import pygame


class Racket1:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg
        self.posX = 10
        self.posY = 180
        self.width = 10
        self.height = 40

    def draw(self, screen, speed, up: bool = False, down: bool = False):
        self.__set_pos_y(screen=screen, speed=speed, up=up, down=down)
        self.pg.draw.rect(screen, (255, 255, 255), (self.posX, self.posY, self.width, self.height))

    def __set_pos_y(self, screen, speed, up: bool = False, down: bool = False):
        x, y = screen.get_size()
        if self.posY > 0:
            if up:
                self.posY -= speed
        if self.posY < y - 40:
            if down:
                self.posY += speed
