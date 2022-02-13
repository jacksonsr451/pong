import pygame


class Racket2:
    def __init__(self, pg: pygame, speed):
        self.pg: pygame = pg
        self.posX = 580
        self.posY = 180
        self.width = 10
        self.height = 40
        self.racket = None
        self.ball_x = 0
        self.ball_y = 0
        self.move = speed

    def draw(self, screen, position):
        self.ball_x, self.ball_y = position
        self.__set_pos_y(screen=screen)
        self.racket = self.pg.Rect(self.get_position())
        self.pg.draw.rect(screen, (255, 255, 255), self.racket)

    def __set_pos_y(self, screen):
        x, y = screen.get_size()
        if self.ball_x > 299:
            if (self.posY > 0) and (self.posY > self.ball_y):
                self.posY -= self.move
            elif (self.move < (y - 40)) and (self.posY < self.ball_y):
                self.posY += self.move
        else:
            if self.posY > 180:
                self.posY -= self.move
            elif self.posY < 220:
                self.posY += self.move

    def get_position(self):
        position = (self.posX, self.posY, self.width, self.height)
        return position

    def get_racket(self):
        return self.racket
