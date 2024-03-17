import pygame
from character_files.controller_image import Image
from character_files.controller_action import Action



class Character(pygame.sprite.Sprite):
  def __init__(self, frames, position = (0,0)):
    super().__init__()

    # Character Stats
    self.max_HP = 50
    self.HP = 50
    self.max_MP = 50
    self.MP = 25
    self.damage = 99999

    # Frame Control
    self.frames = frames
    self.frame_index = 0
    self.frame_speed = 0.1

    # Obstacles / Enemies / NPCs (set at each level)
    self.obstacles = None
    self.enemies = None
    self.npcs = None
    self.loots = None

    # Character Movements
    self.direction_vector = {'x': 0, 'y': 0}
    self.direction = "down"
    self.speed = 5

    # Character Actions
    self.action = "idle"
    self.attacking = False
    self.current_action = f"{self.action}_{self.direction}"

    # Image and Rect
    self.image = frames[self.current_action][self.frame_index]
    self.rect = self.image.get_rect(topleft = position)
    self.hitbox = self.rect.inflate(-38, -35)
    self.collisionbox = self.hitbox.inflate(0, -10)

    # Controllers
    self.image_controller = Image(self)
    self.action_controller = Action(self)

    # NPC Dialogue Text Box
    self.current_npc = None
    self.current_lines = None
    self.npc_interacting = False
    self.draw_textbox = False
    self.next_line = False

    # Inventory
    self.inventory = []

  def update(self):
    self.action_controller.update()
    self.image_controller.update()





