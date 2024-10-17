import pygame

from ball import Ball
from constants import *


class Player:
    def __init__(self, x: int, control_type: str) -> None:

        self.rect = pygame.Rect(x, SCREEN_CENTER_H, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = WHITE
        self.control_type = control_type
        self.speed = PLAYER_SPEED

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, ball: Ball) -> None:
        if self.control_type == USER:
            self._handle_user_input()
        elif self.control_type == COMPUTER:
            self._handle_computer_input(ball)

    def _handle_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_up()
            if self.rect.top < 0:
                self.rect.top = 0
        if keys[pygame.K_DOWN]:
            self.move_down()
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    def _handle_computer_input(self, ball: Ball):
        if self.rect.centery < ball.rect.centery:
            self.move_down()
            if self.rect.bottom > SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
        elif self.rect.centery > ball.rect.centery:
            self.move_up()
            if self.rect.top < 0:
                self.rect.top = 0
