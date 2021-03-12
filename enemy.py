import pygame
from random import randint
from math import sqrt

from pygame import draw

class Enemy():
    def __init__(self, quantity, surface):
        self.quantity = quantity
        self.surface = surface

        self.surf_width = self.surface.get_width()
        self.surf_height = self.surface.get_height()

        self.spawnEnemy()
        self.spawnFood()

        self.enemies_list = self.spawnEnemy()
        self.food_list = self.spawnFood()
    
    def spawnEnemy(self):
        self.enemy_pos = []
        
        for i in range(self.quantity):
            self.enemy_x = randint(0, self.surf_width)
            self.enemy_y = randint(0, self.surf_height)
            self.enemy_radius = randint(0, 100)
            if pygame.Rect(self.enemy_x, self.enemy_y, self.enemy_radius-10, self.enemy_radius-10) not in self.enemy_pos:
                self.enemy_pos.append([[self.enemy_x, self.enemy_y], self.enemy_radius])

        return self.enemy_pos
    
    def spawnFood(self):
        self.food_pos = []
        for i in range(100):
            self.food_x = randint(0, self.surf_width)
            self.food_y = randint(0, self.surf_height)
            self.food_radius = randint(1, 5)
            self.food_pos.append([(self.food_x, self.food_y), self.food_radius])

        return self.food_pos

    def draw(self):

        for enemy_pos, radius in self.enemies_list:
            pygame.draw.circle(self.surface, (80, 150, 50), enemy_pos, radius)

        for food_pos, radius in self.food_list:
            pygame.draw.circle(self.surface, (25, 20, 25), (food_pos), radius)

    def enemyMovement(self, enemy_vel, player_pos : list):
        self.player_pos = player_pos
        self.enemy_vel = enemy_vel

        for enemy_pos, enemy_radius in self.enemies_list:
            if enemy_pos[0] < self.player_pos[0]:
                enemy_pos[0] += self.enemy_vel
            if enemy_pos[0] > self.player_pos[0]:
                enemy_pos[0] -= self.enemy_vel
            if enemy_pos[1] < self.player_pos[1]:
                enemy_pos[1] += self.enemy_vel
            if enemy_pos[1] > self.player_pos[1]:
                enemy_pos[1] -= self.enemy_vel
            
            # also not working
            # for i in range(len(self.enemies_list)):
            #         if enemy.colliderect(self.enemies_list[i][0]):
            #             self.enemy_vel = 0
            #         else: self.enemy_vel = enemy_vel
            
            # not working
            # for food, food_radius in self.food_list:
            #     if enemy.colliderect(food):
            #         enemy_radius += food_radius // 2
            #         self.food_list.remove([food, food_radius])
    
    def ccCollision(self, c1x, c1y, c2x, c2y, c1r, c2r):
        self.distX = c1x - c2x # x distance between the two circles
        self.distY = c1y - c2y # y distance between the two circles
        self.distance = sqrt((self.distX**2) + (self.distY**2)) # pythagorean theorem to find the distance between the two circles

        # if the distance is less then the sum of the two circles radium, they are colliding
        if self.distance <= c1r + c2r:
            return True
        else: return False

    def eatEnemy(self, player):
        self.player = player

        for enemy_pos, enemy_radius in self.enemies_list:
            if player.radius > enemy_radius:
                    if self.ccCollision(enemy_pos[0], enemy_pos[1], player.x, player.y, enemy_radius - (enemy_radius * 0.75), player.radius):
                        player.radius += enemy_radius // 2
                        self.enemies_list.remove([enemy_pos, enemy_radius])

        for food_pos, food_radius in self.food_list:
            pygame.draw.circle(self.surface, (25, 20, 25), (food_pos), food_radius)
            
            if player.radius > food_radius:
                if self.ccCollision(food_pos[0], food_pos[1], player.x, player.y, food_radius, player.radius):
                    self.player.radius += food_radius // 2
                    self.food_list.remove([food_pos, food_radius])

    def update(self):
        self.draw()
        self.eatEnemy(self.player)
