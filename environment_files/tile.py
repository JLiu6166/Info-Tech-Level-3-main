import pygame
from utilities.config import TILE_SIZE
from environment_files.tile_creator import tile_file_path
from utilities.image_handle import populate_image

class Tile(pygame.sprite.Sprite):
  def __init__(self, image, position, groups):
    super().__init__(groups)
    self.image = image
    self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
    self.rect = self.image.get_rect(topleft = position)
    
  @classmethod
  def tile_populate_images(cls):
    cls.tile_images = populate_image(tile_file_path)

  @classmethod
  def tile(cls, type, position, groups):
    return Tile(cls.tile_images[type], position, groups)