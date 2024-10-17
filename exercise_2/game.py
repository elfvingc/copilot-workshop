import pygame
from constants import *
from player import Player
from ball import Ball


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.player1 = Player(20, USER)
        self.player2 = Player(SCREEN_WIDTH - 40, COMPUTER)
        self.ball = Ball()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def update(self):
        self.player1.update(self.ball)
        self.player2.update(self.ball)
        self.ball.update(self.player1, self.player2)

    def draw(self):
        self.screen.fill(BLACK)
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        self.ball.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
