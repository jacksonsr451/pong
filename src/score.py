import pygame


class Score:
    def __init__(self, pg: pygame):
        self.pg: pygame = pg
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.my_score = ""
        self.text_1 = None
        self.text_rect_1 = None
        self.computer_score = ""
        self.text_2 = None
        self.text_rect_2 = None

    def render(self, screen, score):
        self.my_score = str(score['player'])
        self.__set_score_player(screen=screen)

        self.computer_score = str(score['computer'])
        self.__set_score_computer(screen=screen)

    def __set_score_player(self, screen):
        self.text_1 = self.font.render(self.my_score, True, (255, 255, 255))
        self.text_rect_1 = self.text_1.get_rect()
        self.text_rect_1.center = (60, 30)
        screen.blit(self.text_1, self.text_rect_1)

    def __set_score_computer(self, screen):
        self.text_2 = self.font.render(self.computer_score, True, (255, 255, 255))
        self.text_rect_2 = self.text_1.get_rect()
        self.text_rect_2.center = (540, 30)
        screen.blit(self.text_2, self.text_rect_2)
