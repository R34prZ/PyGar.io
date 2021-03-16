import pygame, sys
from pygame.locals import *

import player, enemy, world

version = "1.3"

pygame.init()
clock = pygame.time.Clock()

WIN_SIZE = width, height = 1080, 720
screen = pygame.display.set_mode(WIN_SIZE, 0, 32)

player = player.Player(width//2 - 15, height//2 - 15, 20)
player.drawPlayer(screen, (50, 100, 250))

world = world.World(screen, 5, player)

enemy = enemy.Enemy(5, screen, world)
enemy.eatEnemy(player)

while True:

    screen.fill((255, 255, 255))
    
    player.update()
    enemy.update()
    world.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.set_caption(f'Agar.py v{version} | FPS: {clock.get_fps() : .2f}')
    clock.tick(60)
    pygame.display.flip()