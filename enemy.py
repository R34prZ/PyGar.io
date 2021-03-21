import pygame

class Enemy():
    def __init__(self, x, y, radius, surface, player):

        self.surface = surface

        self.x = x
        self.y = y
        self.radius = radius

        self.player = player
        self.enemy_vel = 2
    
    def __draw(self):
        pygame.draw.circle(self.surface, (80, 150, 50), (self.x - self.player.cam_scroll[0], self.y - self.player.cam_scroll[1]), self.radius)

    def _enemyMovement(self):

        if self.radius > self.player.radius:
            if self.x < self.player.x:
                self.x += self.enemy_vel
            if self.x > self.player.x:
                self.x -= self.enemy_vel
            if self.y < self.player.y:
                self.y += self.enemy_vel
            if self.y > self.player.y:
                self.y -= self.enemy_vel
        
        elif self.radius <= self.player.radius:
            if self.x < self.player.x:
                self.x -= self.enemy_vel
            if self.x > self.player.x:
                self.x += self.enemy_vel
            if self.y < self.player.y:
                self.y -= self.enemy_vel
            if self.y > self.player.y:
                self.y += self.enemy_vel
        
    def update(self):
        self.__draw()
        self._enemyMovement()
