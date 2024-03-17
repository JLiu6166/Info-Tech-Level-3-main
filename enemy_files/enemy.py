import pygame
from enemy_files.controller_image import Image
from enemy_files.controller_action import Action
from enemy_files.controller_death import Death
import random


class Enemy(pygame.sprite.Sprite):
  def __init__(self, hostile, position, groups, player, frames, obstacles, size = 64):
    super().__init__(groups)

    # Interactables
    self.player = player
    self.obstacles = obstacles

    # Stats
    self.max_HP = 40
    self.HP = 30

    # Image and Rect
    self.frames = frames
    self.size = size
    self.image = frames["idle_right"][0]
    self.rect = self.image.get_rect(topleft = position)
    self.image_controller = Image(self)

    # Aggro
    self.hostile = hostile
    self.aggro = False
    self.aggro_range = 100
    self.aggro_rect = self.rect.inflate(self.aggro_range, self.aggro_range)

    # Sprite Control
    self.spawn_point_x = position[0]
    self.spawn_point_y = position[1]
    self.moving = False
    self.direction = 1
    self.movespeed = 0
    self.target_x = 0
    self.target_y = 0
    self.leash_distance = 200
    self.action_controller = Action(self)

    # State
    self.alive = True
    self.death_time = None
    self.despawn_timer = 100

    # Action
    self.moving = False

    # Loot table
    self.loot_table = {
      'steak': 0.5,
      'cheese': 0.2,
      None : 0.3}

    # Loot creator
    self.can_drop_loot = True

  # On death
  def initiate_death(self):
    self.alive = False
    self.death_controller = Death(self)

  def update(self):
    if self.alive:
      self.action_controller.update()
      self.image_controller.update()
    else:
      self.death_controller.update()