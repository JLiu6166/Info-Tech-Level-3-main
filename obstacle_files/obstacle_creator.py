import pygame
from obstacle_files.obstacle import Obstacle
from utilities.image_handle import populate_image

class Obstacle_creator():
  def __init__(self):
    # Dictionary to keep track of path to assets
    self.obstacle_file_path = {"bush": "assets/obstacle/bush.png",
                               "rock": "assets/obstacle/rock.png",}
    self.obstacle_images = populate_image(self.obstacle_file_path)

  # Function to spawn a specific type of enemy
  def obstacle(self, type, position, groups):
    return Obstacle(self.obstacle_images[type], position, groups)