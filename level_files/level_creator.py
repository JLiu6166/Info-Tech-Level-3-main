import json
from level_files.level import Level

class Level_creator:
    def __init__(self):
        with open("level_files/maps.json", "r") as json_file:
            self.level_mapping = json.load(json_file)

        self.map_info = {}
        for level, path in self.level_mapping.items():
            with open(path, "r") as json_file:
                level_data = json.load(json_file)
                self.map_info.update({level : level_data})

    # Function to spawn a specific type of enemy
    def create_level(self, player, level):
        return Level(player, level, self.map_info[str(level)])