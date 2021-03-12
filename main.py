import pygame, sys, random
from pygame.locals import *

import player, enemy

pygame.init()
clock = pygame.time.Clock()

WIN_SIZE = width, height = 1080, 720
screen = pygame.display.set_mode(WIN_SIZE)

movements = {
    'moving_up' : False,
    'moving_down'  : False,
    'moving_left' : False,
    'moving_right' : False
}

player = player.Player(width//2 - 15, height//2 - 15, 20)
player.drawPlayer(screen, (50, 100, 250))
player.playerMovement(5, movements)

enemy = enemy.Enemy(1, screen)
enemy.eatEnemy(player)

while True:

    screen.fill((255, 255, 255))
    
    player.update()
    enemy.update()

    if len(enemy.enemies_list) <= 0:
        enemy.enemies_list = enemy.spawnEnemy()
    if len(enemy.food_list) <= 0:
        enemy.food_list = enemy.spawnFood()
    
    enemy.enemyMovement(2, [player.x, player.y])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                movements['moving_up'] = True
            elif event.key == K_a:
                movements['moving_left'] = True
            elif event.key == K_s:
                movements['moving_down'] = True
            elif event.key == K_d:
                movements['moving_right'] = True
            # elif event.key == K_q:
            #     enemies_list = spawnEnemy(5)
        elif event.type == KEYUP:
            if event.key == K_w:
                movements['moving_up'] = False
            elif event.key == K_a:
                movements['moving_left'] = False
            elif event.key == K_s:
                movements['moving_down'] = False
            elif event.key == K_d:
                 movements['moving_right'] = False

    clock.tick(60)
    pygame.display.flip()