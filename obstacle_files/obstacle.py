import pygame
from utilities.config import TILE_SIZE

class Obstacle(pygame.sprite.Sprite):
  def __init__(self, image, position, groups):
    super().__init__(groups)
    self.image = image
    self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
    self.rect = self.image.get_rect(topleft = position)

    # Enemy Hitbox
    #self.collisionbox = self.rect.inflate(-5, -5)

    self.create_image()

  def create_image(self):
    image_surface = pygame.Surface((self.rect.width,self.rect.height))
    image_surface.blit(self.image, (0,0))
    image_surface.set_colorkey((0,0,0))

    #pygame.draw.rect(image_surface, (255,0,0), (0, 0, self.rect.width, self.rect.height), 3)
    self.image = image_surface
