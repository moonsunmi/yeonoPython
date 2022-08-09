import pygame
import time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 80

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PURPLE = 127, 0, 127
GRAY = 127, 127, 127
WHITE = 255, 255, 255


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

rect = pygame.Rect((0, 0), (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.draw.rect(screen, WHITE, rect)

rect = pygame.Rect((0, 0), (40, 40))
pygame.draw.rect(screen, GREEN, rect)

rect = pygame.Rect((360, 60), (60, 20))
pygame.draw.rect(screen, RED, rect)

pygame.display.update()

time.sleep(3)