import pygame, sys
from pygame.locals import QUIT
from utilities.config import FPS, SCREEN_SIZE

from character_files.character_creator import Character_creator
from level_files.level_creator import Level_creator
from level_files.level import Level


class Game:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption('Tiles!')
    
    self.screen = pygame.display.set_mode(SCREEN_SIZE).convert_alpha()
    self.clock = pygame.time.Clock()

    self.character_creator = Character_creator()
    self.player = self.character_creator.char_basic()

    self.level_creator = Level_creator()

    self.level_1 = self.level_creator.create_level(self.player, 1)
    self.level_2 = self.level_creator.create_level(self.player, 2)
    self.level_3 = self.level_creator.create_level(self.player, 3)

    self.current_level = self.level_1

    while True:
      for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

      level = self.current_level.update()

      match level:
        case 1:
          self.current_level = self.level_1
        case 2:
          self.current_level = self.level_2
        case 3:
          self.current_level = self.level_3
      
      pygame.display.update()
      self.clock.tick(FPS)