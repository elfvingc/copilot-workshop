import sys

import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 120
ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, 10, 30, 30)
player1 = pygame.Rect(20, SCREEN_HEIGHT // 2, PLAYER_WIDTH, PLAYER_HEIGHT)
player2 = pygame.Rect(
    SCREEN_WIDTH - 40,
    SCREEN_HEIGHT // 2,
    PLAYER_WIDTH,
    PLAYER_HEIGHT,
)
BALL_SPEED_X = 7
BALL_SPEED_Y = 7
PLAYER_SPEED = 0
font = pygame.font.Font(None, 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                PLAYER_SPEED = -7
            elif event.key == pygame.K_DOWN:
                PLAYER_SPEED = 7
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                PLAYER_SPEED = 0

    player1.y += PLAYER_SPEED
    if player1.y <= 0:
        player1.y = 0
    elif player1.y >= SCREEN_HEIGHT - PLAYER_HEIGHT:
        player1.y = SCREEN_HEIGHT - PLAYER_HEIGHT

    if player2.centery < ball.centery:
        player2.y += 7
        if player2.bottom > SCREEN_HEIGHT:
            player2.bottom = SCREEN_HEIGHT
    elif player2.centery > ball.centery:
        player2.y -= 7
        if player2.top < 0:
            player2.top = 0

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        BALL_SPEED_Y *= -1

    if ball.left <= 0:
        BALL_SPEED_X *= -1
        ball.x = SCREEN_WIDTH // 2
        ball.y = SCREEN_HEIGHT // 2
    elif ball.right >= SCREEN_WIDTH:
        BALL_SPEED_X *= -1
        ball.x = SCREEN_WIDTH // 2
        ball.y = SCREEN_HEIGHT // 2

    if ball.colliderect(player1):
        BALL_SPEED_X *= -1
        ball.right = player1.left
        if BALL_SPEED_X > 0:
            ball.left = player1.right
        else:
            ball.right = player1.left
    elif ball.colliderect(player2):
        BALL_SPEED_X *= -1
        ball.left = player2.right
        if BALL_SPEED_X > 0:
            ball.left = player2.right
        else:
            ball.right = player2.left

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
