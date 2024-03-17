import pygame
from npc_files.npc_image import Image

class NPC(pygame.sprite.Sprite):
  def __init__(self, position, groups, frames, id = "npc1", dialogue = None):
    super().__init__(groups)

    # ID
    self.npc_id = id

    # Frames
    self.frames = frames

    # Frame Control
    self.frame_index = 0
    self.frame_speed = 0.1

    # NPC Actions
    self.action = "idle_down"
    self.spawn_point = position

    # Image and Rect
    self.image_controller = Image(self)
    self.image_controller.update()
    self.rect = self.image.get_rect(topleft = position)

    # Hitbox
    self.hitbox = self.rect.inflate(10,10)

    # Dialogue Lines
    self.dialogue_lines = dialogue
    self.current_line = 0

  def update(self):
    self.image_controller.update()
    