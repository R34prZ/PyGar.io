import pygame
import enemy, player
from random import randint
from math import sqrt

class World():
    def __init__(self, surface, size : int, x = 0, y = 0):
        """
            Set up world generation. Consider "size" as the number of times
            the screen size you want the game map to be.
        """
        self.surface = surface

        self.player = player.Player(self.surface.get_width() // 2 - 15, self.surface.get_height() // 2 - 15, 20)
        self.player.drawPlayer(self.surface, (50, 100, 250))

        self.surf_width = self.surface.get_width()
        self.surf_height = self.surface.get_height()

        self.world_width = self.surf_width * size
        self.world_height = self.surf_height * size

        self.world_x = x
        self.world_y = y

        self.food_list = self.__spawnFood()
        self.enemies_list = self.__spawnEnemy()

    def generate_world(self):
        self.world_rect = pygame.Rect(self.world_x - self.player.cam_scroll[0], self.world_y - self.player.cam_scroll[1], self.world_width, self.world_height)
        self.world = pygame.draw.rect(self.surface, (0, 0, 0), self.world_rect, 10)
    
    def __spawnFood(self):
        self.food_pos = []
        for i in range(500):
            self.food_x = randint(0, self.world_width)
            self.food_y = randint(0, self.world_height)
            self.food_radius = randint(1, 5)
            self.food_pos.append([(self.food_x, self.food_y), self.food_radius])

        return self.food_pos
    
    def __spawnEnemy(self):
        self.enemies_list = []
        
        for i in range(20):
            self.enemy_x = randint(0, self.world_width)
            self.enemy_y = randint(0, self.world_height)
            self.enemy_radius = randint(0, 100)
            
            self.enemies_list.append(enemy.Enemy(self.enemy_x, self.enemy_y, self.enemy_radius, self.surface, self.player))

        return self.enemies_list

    def __draw(self):

        for food_pos, radius in self.food_list:
            pygame.draw.circle(self.surface, (25, 20, 25), (food_pos[0] - self.player.cam_scroll[0], food_pos[1] - self.player.cam_scroll[1]), radius)

        for enemy in self.enemies_list:
            enemy.update()

    def __eatEnemy(self):

        for enemy in self.enemies_list:
            if self.player.radius > enemy.radius:
                    if self.__ccCollision(enemy.x, enemy.y, self.player.x, self.player.y, enemy.radius - (enemy.radius * 0.75), self.player.radius):
                        self.player.radius += enemy.radius // 2
                        self.enemies_list.remove(enemy)
            
            for enemy2 in self.enemies_list:
                if enemy2.radius > enemy.radius:
                    if self.__ccCollision(enemy.x, enemy.y, enemy2.x, enemy2.y, enemy.radius - (enemy.radius * 0.75), enemy2.radius):
                        enemy2.radius += enemy.radius // 2
                        self.enemies_list.remove(enemy)

        for food_pos, food_radius in self.food_list:
            if self.player.radius > food_radius:
                if self.__ccCollision(food_pos[0], food_pos[1], self.player.x, self.player.y, food_radius, self.player.radius):
                    self.player.radius += food_radius // 2
                    self.food_list.remove([food_pos, food_radius])

            for enemy in self.enemies_list:
                if enemy.radius > food_radius:
                    if self.__ccCollision(food_pos[0], food_pos[1], enemy.x, enemy.y, food_radius, enemy.radius):
                        enemy.radius += food_radius // 2
                        try:
                            self.food_list.remove([food_pos, food_radius])
                        except:
                            pass

    def __ccCollision(self, c1x, c1y, c2x, c2y, c1r, c2r):

        """
            Function to calculate circle-circle collisions.
        """

        self.distX = c1x - c2x # x distance between the two circles
        self.distY = c1y - c2y # y distance between the two circles
        self.distance = sqrt((self.distX**2) + (self.distY**2)) # pythagorean theorem to find the distance between the two circles

        # if the distance is less then the sum of the two circles radium, they are colliding
        if self.distance <= c1r + c2r: return True
        else: return False

    def update(self):
        self.generate_world()
        self.__draw()
        self.__eatEnemy()
        self.player.update()

        if len(self.food_list) == 0:
            self.food_list = self.__spawnFood()
        if len(self.enemies_list) == 0:
            self.enemies_list = self.__spawnEnemy()