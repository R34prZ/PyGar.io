import pygame
class Player:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.cam_scroll = [0, 0]

    def drawPlayer(self, surface, color):
        self.surface = surface
        self.color = color

        self.player_length = self.radius + self.radius // 2

        self.player = pygame.draw.circle(self.surface, self.color, (self.x - self.cam_scroll[0], self.y - self.cam_scroll[1]), self.radius)

    def playerMovement(self, velocity : int, movement : dict):
        self.velocity = velocity
        self.movement = movement

        self.player_aceleration  = [0, 0]

        if self.movement['moving_up']:
            self.player_aceleration[1] = -self.velocity
        if self.movement['moving_down']:
            self.player_aceleration[1] = self.velocity
        if self.movement['moving_left']:
            self.player_aceleration[0] = -self.velocity
        if self.movement['moving_right']:
            self.player_aceleration[0] = self.velocity
        
        self.x += self.player_aceleration[0]
        self.y += self.player_aceleration[1]

    def camera(self):
        self.cam_scroll[0] += (self.x - self.cam_scroll[0] - round(self.surface.get_width() * 0.5 + self.radius * 0.5))// 20
        self.cam_scroll[1] += (self.y - self.cam_scroll[1] - round(self.surface.get_height() * 0.5 + self.radius * 0.5))// 20

    def update(self):
        self.drawPlayer(self.surface, self.color)
        self.playerMovement(self.velocity, self.movement)
        self.camera()