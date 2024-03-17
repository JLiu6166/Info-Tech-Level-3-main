import pygame
from utilities.config import TILE_SIZE
from environment_files.tile import Tile
from obstacle_files.obstacle_creator import Obstacle_creator
from enemy_files.enemy_creator import Enemy_creator
from npc_files.npc_creator import NPC_creator
from camera import Camera_group
from UI_files.ui import UI

class Level:
  def __init__(self, player, level, map_info):
    self.screen = pygame.display.get_surface()
    self.background_group = Camera_group()
    self.visible_group = Camera_group()
    self.player_group = Camera_group()
    self.obstacle_group = Camera_group()
    self.enemy_group = Camera_group()
    self.loot_group = Camera_group()
    self.npc_group = Camera_group()

    # Initiate Tiles
    Tile.tile_populate_images()

    self.obstacle_creator = Obstacle_creator()
    self.enemy_creator = Enemy_creator()
    self.npc_creator = NPC_creator()

    # UI
    self.user_interface = UI(player)

    # Player
    self.player = player

    # Level Creation
    self.current_level = level
    self.map_info = map_info

    # Level Transition Control
    self.transition_position = None
    self.fresh_arrival = True
    self.next_lvl = None
    self.can_transition = False
    self.transition_buffer = pygame.time.get_ticks() + 2000

    # Initiate Maps and Objects
    self.create_map()
    self.spawn_obstacles()
    self.spawn_sprites()

  def create_map(self):
    for row_index, row in enumerate(self.map_info["map"]):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        match tile:
          case " ":
            Tile.tile("grass", (x,y), [self.background_group])
          case "S":
            Tile.tile("sand", (x,y), [self.background_group])
          case "1":
            self.transition_1_tile = Tile.tile("sand", (x,y), [self.background_group])
          case "2":
            self.transition_2_tile = Tile.tile("sand", (x,y), [self.background_group])
          case "3":
            self.transition_3_tile = Tile.tile("sand", (x,y), [self.background_group])

  def spawn_obstacles(self):
    for row_index, row in enumerate(self.map_info["obstacles"]):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        match tile:
          case "R":
            self.obstacle_creator.obstacle("rock", (x,y), [self.visible_group, self.obstacle_group])
          case "T":
            self.obstacle_creator.obstacle("bush", (x,y), [self.visible_group, self.obstacle_group])

  def spawn_sprites(self):
    for row_index, row in enumerate(self.map_info["sprites"]):
      for col_index, tile in enumerate(row):
        x = col_index * TILE_SIZE
        y = row_index * TILE_SIZE
        match tile:
          case "C":
            self.transition_position = (x, y)
            self.player_group.add(self.player)
            self.visible_group.add(self.player)
          case "E":
            self.enemy_creator.enemy("cow", (x,y), [self.enemy_group, self.visible_group], self.obstacle_group, self.player)
          case "K":
            self.enemy_creator.enemy("chicken", (x,y), [self.enemy_group, self.visible_group], self.obstacle_group, self.player)
          case "B":
            self.enemy_creator.enemy("bull", (x,y), [self.enemy_group, self.visible_group], self.obstacle_group, self.player)
          case "N":
            self.npc_creator.npc_basic((x, y),  [self.npc_group, self.visible_group])

  def check_level(self):
    if self.fresh_arrival:
      self.level = self.current_level
      self.player.obstacles = self.obstacle_group
      self.player.enemies = self.enemy_group
      self.player.loots = self.loot_group
      self.player.npcs = self.npc_group
      self.player.rect.topleft = self.transition_position
      self.fresh_arrival = False

    if self.can_transition:
      if pygame.time.get_ticks() >= self.transition_buffer:
        keys = pygame.key.get_pressed()
        for lvl in range(1,4):
          transition_tile_name = f"transition_{lvl}_tile"
          if hasattr(self, transition_tile_name):
            transition_tile = getattr(self, transition_tile_name)
            if self.player.hitbox.colliderect(transition_tile.rect):
              if keys[pygame.K_SPACE]:
                self.level = lvl
                self.transition_position = self.player.rect.topleft
                self.can_transition = False
                self.fresh_arrival = True

    else:
      self.transition_buffer = pygame.time.get_ticks() + 2000
      self.can_transition = True

  def update(self):
    self.check_level()
    self.screen.fill('black')
    self.player_group.update()
    self.enemy_group.update()
    self.loot_group.update()
    self.npc_group.update()
    self.background_group.draw(self.player)
    self.visible_group.draw(self.player)
    self.loot_group.draw(self.player)

    # UI
    self.user_interface.update()

    # Draw player hitbox, for visual reference only
    # self.visible_group.draw_sprite_hitbox(self.player)
    return self.level




