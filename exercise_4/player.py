import pygame

from ball import Ball
from constants import *


class Player:
    def __init__(self, x: int, control_type: str) -> None:
        """
        Initialize a Player object.

        Args:
            x (int): The x-coordinate of the player.
            control_type (str): The type of control to use for the player.

        Returns:
            None
        """
        self.rect = pygame.Rect(x, SCREEN_CENTER_H, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.color = WHITE
        self.control_type = control_type
        self.speed = PLAYER_SPEED

    def move_up(self):
        """
        Move the player up by its speed.

        Returns:
            None
        """
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def update(self, ball: Ball) -> None:
        """
        Update the player's position based on control type.

        Args:
            ball (Ball): The current state of the ball.

        Returns:
            None
        """
        if self.control_type == USER:
            self._handle_user_input()
        elif self.control_type == COMPUTER:
            self._handle_computer_input(ball)

    def _handle_user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move_up()
        if keys[pygame.K_DOWN]:
            self.move_down()

    def _handle_computer_input(self, ball: Ball):
        """
        Control the computer player's position based on the ball's position.

        If the computer player's center is above the ball's center, move the
        player down.  If the computer player's center is below the ball's
        center, move the player up.

        Args:
            ball (Ball): The current state of the ball.
        """
        if self.rect.centery < ball.rect.centery:
            i = 0
            self.move_down()
        elif self.rect.centery > ball.rect.centery:
            self.move_up()
