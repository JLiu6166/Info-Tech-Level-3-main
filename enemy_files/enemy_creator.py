from enemy_files.enemy import Enemy
from utilities.image_handle import get_all_frames, flip_frames

class Enemy_creator():
  def __init__(self):
    # Dictionary to keep track of path to assets
    self.enemy_file_path = {"cow": {"idle_right": "assets/enemies/cow/idle/",
                                    "move_right": "assets/enemies/cow/move/",
                                    "death_right": "assets/enemies/cow/death/",},
                            "chicken": {"idle_right": "assets/enemies/chicken/idle/",
                                        "move_right": "assets/enemies/chicken/move/",
                                        "death_right": "assets/enemies/cow/death/",},
                            "bull": {"idle_right": "assets/enemies/bull/idle/",
                                     "move_right": "assets/enemies/bull/move/",
                                     "attack_right": "assets/enemies/bull/attack/",
                                     "death_right": "assets/enemies/bull/death/",},}
    
    self.enemy_tile_size = {"cow":64, "chicken":32, "bull":64}
    self.enemy_hostile = {"cow":False, "chicken":False, "bull":True}

    self.enemy_frames = {}
    self.populate_right_frames()
    self.populate_left_frames()

  def populate_right_frames(self):
    for key in self.enemy_file_path:
      list = get_all_frames(self.enemy_file_path[key], self.enemy_tile_size[key])
      self.enemy_frames.update({key: list})

  def populate_left_frames(self):
    for enemy in self.enemy_frames:
      if "idle_right" in self.enemy_frames[enemy]:
        list = flip_frames(self.enemy_frames[enemy]["idle_right"])
        self.enemy_frames[enemy].update({"idle_left": list})
      if "move_right" in self.enemy_frames[enemy]:
        list = flip_frames(self.enemy_frames[enemy]["move_right"])
        self.enemy_frames[enemy].update({"move_left": list})
      if "death_right" in self.enemy_frames[enemy]:
        list = flip_frames(self.enemy_frames[enemy]["death_right"])
        self.enemy_frames[enemy].update({"death_left": list})
      if "attack_right" in self.enemy_frames[enemy]:
        list = flip_frames(self.enemy_frames[enemy]["attack_right"])
        self.enemy_frames[enemy].update({"attack_left": list})

  # Function to spawn a specific type of enemy
  def enemy(self, type, spawn_point, group, obstacles, player):
    return Enemy(self.enemy_hostile[type], spawn_point, group, player, self.enemy_frames[type], obstacles, self.enemy_tile_size[type])