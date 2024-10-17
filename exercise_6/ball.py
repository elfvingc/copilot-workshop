import pygame
from constants import *


class Ball:
    def __init__(self):
        start_pos_x, start_pos_y = self.get_start_x_y()
        self.rect = pygame.Rect(start_pos_x, start_pos_y, BALL_WIDTH, BALL_HEIGHT)
        self.color = WHITE
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def get_start_x_y(self):
        x = SCREEN_CENTER_W - (BALL_WIDTH // 2)
        y = SCREEN_CENTER_H - (BALL_HEIGHT // 2)
        return x, y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce_x(self):
        self.speed_x *= -1

    def bounce_y(self):
        self.speed_y *= -1

    def reset(self):
        self.rect.x, self.rect.y = self.get_start_x_y()

    def update(self, player_1, player_2):
        self.move()

        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.bounce_y()

        if self.rect.left <= 0:
            self.bounce_x()
        elif self.rect.right >= self.screen_width:
            self.bounce_x()

        if (
            self.rect.x == player_1.rect.x
            and self.rect.y == player_1.rect.y
            or self.rect.x == player_2.rect.x
            and self.rect.y == player_2.rect.y
        ):
            self.bounce_x()

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)
