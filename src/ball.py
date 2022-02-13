from random import randint

import pygame


class Ball:
    def __init__(self, pg: pygame, speed: float):
        self.pg: pygame = pg
        self.position_x = 300
        self.position_y = 200
        self.move_x = speed
        self.move_y = speed * .3
        self.ball = None
        self.points = {
            "player": 0,
            "computer": 0
        }

    def draw(self, screen, racket_1, racket_2):
        self.ball = self.pg.Rect(self.__get_direction())
        self.pg.draw.ellipse(screen, (255, 255, 255), self.ball)
        self.__check_collisions(racket_1=racket_1, racket_2=racket_2)
        self.__move()

    def __check_collisions(self, racket_1, racket_2):
        if self.position_x > 598 or self.position_x < 2:
            self.__set_points()
            self.position_x = 300
            self.position_y = randint(100, 300)
        elif self.position_y > 394 or self.position_y < 4:
            self.move_y *= -1
        elif self.ball.colliderect(racket_1) or self.ball.colliderect(racket_2):
            self.move_x *= -1

    def __set_points(self):
        if self.position_x > 598:
            self.points['player'] += 1
        else:
            self.points['computer'] += 1

    def __move(self):
        self.position_x += self.move_x
        self.position_y += self.move_y

    def __get_direction(self):
        direction = (self.position_x, self.position_y, 5, 5)
        return direction

    def get_position(self):
        position = (self.position_x, self.position_y)
        return position

    def get_points(self):
        return self.points
