import pygame, sys
from pygame.locals import *

import world

version = "2.0"

pygame.init()
clock = pygame.time.Clock()

WIN_SIZE = width, height = 1080, 720
screen = pygame.display.set_mode(WIN_SIZE, 0, 32)

world = world.World(screen, 5)

while True:

    screen.fill((255, 255, 255))
    
    world.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption(f'Agar.py v{version} | FPS: {clock.get_fps() : .2f}')
    clock.tick(60)
    pygame.display.flip()