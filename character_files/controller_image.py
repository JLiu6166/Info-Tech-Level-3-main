import pygame
from utilities.config import TILE_SIZE

class Image:
    def __init__(self, player):
        self.player = player
        self.image_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))

    def animate(self):
        current_action = self.player.action + "_" + self.player.direction
        self.player.frame_index += self.player.frame_speed
        if self.player.frame_index >= len(self.player.frames[current_action]):
            self.player.frame_index = 0
        
        self.frame_image = self.player.frames[current_action][int(self.player.frame_index)]
        self.player.current_action = current_action

    def compose(self):
        self.image_surface.fill("black")
        self.image_surface.blit(self.frame_image, (0, 0))
        self.image_surface.set_colorkey("black")

        # pygame.draw.rect(image_surface, (255,0,0), (0,0, self.rect.width, self.rect.height), 3)
        # pygame.draw.rect(image_surface, (0,255,0), ((self.rect.width - self.hitbox.width) / 2, (self.rect.height - self.hitbox.height) / 2 + 10, self.hitbox.width, self.hitbox.height), 3)
        # pygame.draw.rect(image_surface, (0,0,255), ((self.rect.width - self.collisionbox.width) / 2, (self.rect.height - self.collisionbox.height) / 2 + 20, self.collisionbox.width, self.collisionbox.height), 3)

    def update(self):
        self.animate()
        self.compose()
        self.player.image = self.image_surface
