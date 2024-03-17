import pygame
from utilities.draw_utils import center_on_surf

class Image:
    def __init__(self, npc, size = 64):
        self.npc = npc
        self.image_surface = pygame.Surface((size, size))

    def animate(self):
        self.npc.frame_index += self.npc.frame_speed
        if self.npc.frame_index >= len(self.npc.frames[self.npc.action]):
            self.npc.frame_index = 0
        self.frame_image = self.npc.frames[self.npc.action][int(self.npc.frame_index)]

    def compose(self):
        self.image_surface.fill("black")
        self.image_surface.blit(self.frame_image, (0, 0))
        self.image_surface.set_colorkey((0, 0, 0))

    def update(self):
        self.animate()
        self.compose()
        self.npc.image = self.image_surface
