import pygame
from utilities.config import SCREEN_SIZE

class Camera_group(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.screen = pygame.display.get_surface()
    self.map_width_mid = SCREEN_SIZE[0] // 2
    self.map_height_mid = SCREEN_SIZE[1] // 2

  def draw(self, player):
    offset_x = max(0, player.rect.x - self.map_width_mid)
    offset_y = max(0, player.rect.y - self.map_height_mid)
    for sprite in sorted(self.sprites(), key = self.return_y_pos):
      new_pos_x = sprite.rect.x - offset_x
      new_pos_y = sprite.rect.y - offset_y
      self.screen.blit(sprite.image, (new_pos_x, new_pos_y))

  def return_y_pos(self, sprite):
    return sprite.rect.bottom

  def draw_sprite_hitbox(self, player):
    offset_x = max(0, player.rect.x - self.map_width_mid)
    offset_y = max(0, player.rect.y - self.map_height_mid)
    for sprite in sorted(self.sprites(), key = self.return_y_pos):
      if hasattr(sprite, "hitbox"):
        new_pos_x = sprite.rect.x - offset_x + ((sprite.rect.width - sprite.hitbox.width) / 2)
        new_pos_y = sprite.rect.y - offset_y + ((sprite.rect.height - sprite.hitbox.height) / 2)
        pygame.draw.rect(self.screen, (0,0,255), (new_pos_x, new_pos_y, sprite.hitbox.width, sprite.hitbox.height), 3)
