import pygame
class Player:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.cam_scroll = [0, 0]
        self.velocity = 5

    def drawPlayer(self, surface, color):
        self.surface = surface
        self.color = color

        self.player_length = self.radius + self.radius // 2

        self.player = pygame.draw.circle(self.surface, self.color, (self.x - self.cam_scroll[0], self.y - self.cam_scroll[1]), self.radius)

    def _playerMovement(self):
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_w]:
            self.y -= self.velocity
        if keystate[pygame.K_s]:
            self.y += self.velocity
        if keystate[pygame.K_a]:
            self.x -= self.velocity
        if keystate[pygame.K_d]:
            self.x += self.velocity

    def _camera(self):
        self.cam_scroll[0] += (self.x - self.cam_scroll[0] - round(self.surface.get_width() * 0.5 + self.radius * 0.5))// 20
        self.cam_scroll[1] += (self.y - self.cam_scroll[1] - round(self.surface.get_height() * 0.5 + self.radius * 0.5))// 20

    def update(self):
        self.drawPlayer(self.surface, self.color)
        self._playerMovement()
        self._camera()