import pygame

class World():
    def __init__(self, surface, size : int, player, x = 0, y = 0):
        """
            Set up world generation. Consider "size" as the number of times
            the screen size you want the game map to be.
        """
        self.surface = surface

        self.world_width = self.surface.get_width() * size
        self.world_height = self.surface.get_height() * size

        self.world_x = x
        self.world_y = y

        self.player = player

    def generate_world(self):
        self.world_rect = pygame.Rect(self.world_x - self.player.cam_scroll[0], self.world_y - self.player.cam_scroll[1], self.world_width, self.world_height)
        self.world = pygame.draw.rect(self.surface, (0, 0, 0), self.world_rect, 10)

    def update(self):
        self.generate_world()