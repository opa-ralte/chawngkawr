import sys
import pygame
from pygame.locals import *

def update(dt):
    
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def draw(screen):
    screen.fill((0, 0, 0))

    pygame.display.flip()

def runGame():
    pygame.init()

    fps = 60.0
    fpsClock = pygame.time.Clock()

    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    dt = 1/fps
    while True:
        update(dt)
        draw(screen)

        dt = fpsClock.tick(fps)

runGame()