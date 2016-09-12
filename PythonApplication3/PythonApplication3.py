import pygame
import sys
from pygame.locals import *

pygame.init()

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

screen=pygame.display.set_mode((500,500))
screen.fill((255,255,255))
pygame.display.set_caption('Testing')
font = pygame.font.SysFont(None, 36)

main_clock = pygame.time.Clock()

sonic=pygame.Rect(700, 600, 60, 10)
player_speed = 10
