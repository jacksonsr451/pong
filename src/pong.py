import pygame

from src.background import Background
from src.ball import Ball
from src.controller import Controller
from src.racket_1 import Racket1
from src.racket_2 import Racket2

WIDTH = 600
RIGHT = 400


class Pong:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(60)

        self.controller = Controller(pg=pygame)

        self.speed = .1

        screen = pygame.display.set_mode((WIDTH, RIGHT))
        pygame.display.set_caption("Recreate a Pong Game")

        self.racket1 = Racket1(pg=pygame)
        self.racket2 = Racket2(pg=pygame)
        self.ball = Ball(pg=pygame, speed=self.speed)
        self.background = Background(pg=pygame)

        while True:
            screen.fill((0, 0, 0))

            self.controller.init()

            self.racket1.draw(screen=screen, speed=self.speed, up=self.controller.get_racket_up(),
                              down=self.controller.get_racket_down())
            self.racket2.draw(screen=screen)
            self.ball.draw(screen=screen, racket_1=self.racket1.get_racket(), racket_2=self.racket2.get_racket())
            self.background.draw(screen=screen)

            pygame.display.update()
