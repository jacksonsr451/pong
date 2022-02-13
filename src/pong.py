import pygame
from pygame import QUIT, K_UP, K_DOWN

from src.background import Background
from src.ball import Ball
from src.racket_1 import Racket1
from src.racket_2 import Racket2

WIDTH = 600
RIGTH = 400


class Pong:
    def __init__(self):
        pygame.init()
        clock = pygame.time.Clock()
        clock.tick(60)

        self.racket1_up = False
        self.racket1_down = False

        self.speed = .1

        screen = pygame.display.set_mode((WIDTH, RIGTH))
        pygame.display.set_caption("Pong")

        self.racket1 = Racket1(pg=pygame)
        self.racket2 = Racket2(pg=pygame)
        self.ball = Ball(pg=pygame)
        self.background = Background(pg=pygame)

        while True:
            screen.fill((0, 0, 0))

            for events in pygame.event.get():
                if events.type == QUIT:
                    pygame.quit()
                    exit()
                elif events.type == pygame.KEYDOWN:
                    if events.key == K_UP:
                        self.racket1_up = True
                    elif events.key == K_DOWN:
                        self.racket1_down = True
                if events.type == pygame.KEYUP:
                    if events.key == K_UP:
                        self.racket1_up = False
                    elif events.key == K_DOWN:
                        self.racket1_down = False

            self.racket1.draw(screen=screen, speed=self.speed, up=self.racket1_up, down=self.racket1_down)
            self.racket2.draw(screen=screen)
            self.ball.draw(screen=screen)
            self.background.draw(screen=screen)

            pygame.display.update()
