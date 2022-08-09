import pygame
import time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PURPLE = 127, 0, 127
GRAY = 127, 127, 127
WHITE = 255, 255, 255


def draw_background(screen):
    background = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.draw.rect(screen, WHITE, background)


def draw_block(screen, color, position):

    block = pygame.Rect((position[1] * BLOCK_SIZE, position[0] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
"""
draw_background(screen)


draw_block(screen, RED, (1, 1))
draw_block(screen, RED, (3, 1))
draw_block(screen, RED, (5, 1))
draw_block(screen, RED, (7, 1))
draw_block(screen, GREEN, (12, 10))
draw_block(screen, GREEN, (12, 11))
draw_block(screen, GREEN, (12, 12))
draw_block(screen, GREEN, (12, 13))

pygame.display.update()
"""
block_position = [0, 0]

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RIGHT:
                block_position[1] += 1
            elif event.type == pygame.K_LEFT:
                block_position[1] -= 1
            elif event.type == pygame.K_UP:
                block_position[0] -= 1
            elif event.type == pygame.K_DOWN:
                block_position[0] += 1

    draw_background(screen)
    draw_block(screen, GREEN, block_position)
    pygame.display.update()




