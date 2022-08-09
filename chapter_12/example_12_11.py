import pygame
import time
from datetime import datetime
from datetime import timedelta

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PURPLE = 127, 0, 127
GRAY = 127, 127, 127
WHITE = 255, 255, 255

DIRECTION_ON_KEY = {
    pygame.K_UP: 'north',
    pygame.K_DOWN: 'south',
    pygame.K_LEFT: 'west',
    pygame.K_RIGHT: 'east'
}


def draw_background(screen):
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position):
    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

block_direction = 'east'
block_position = [0, 0]
last_moved_time = datetime.now()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in DIRECTION_ON_KEY:
                block_direction = DIRECTION_ON_KEY[event.key]

            if event.key == pygame.K_UP:  # 입력된 키가 위쪽 화살표 키인 경우
                block_position[0] -= 1  # 블록의 y 좌표에서 1을 뺀다.
            elif event.key == pygame.K_DOWN:  # 입력된 키가 아래쪽 화살표 키인 경우
                block_position[0] += 1  # 블록의 y 좌표에서 1을 더한다.
            elif event.key == pygame.K_LEFT:  # 입력된 키가 왼쪽 화살표 키인 경우
                block_position[1] -= 1  # 블록의 x 좌표에서 1을 뺀다.
            elif event.key == pygame.K_RIGHT:  # 입력된 키가 왼쪽 화살표 키인 경우
                block_position[1] += 1  # 블록의 x 좌표에서 1을 더한다.

    if timedelta(seconds=1) <= datetime.now() - last_moved_time:
        if block_direction == 'north':
            block_position[0] -= 1
        elif block_direction == 'south':
            block_position[0] += 1
        elif block_direction == 'west':
            block_position[1] -= 1
        elif block_direction == 'east':
            block_position[1] += 1

        last_moved_time = datetime.now()

    draw_background(screen)
    draw_block(screen, GREEN, block_position)
    pygame.display.update()




