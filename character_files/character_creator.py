from character_files.character import Character
from utilities.image_handle import get_all_frames, flip_frames

class Character_creator():
    def __init__(self):
        self.characters = {"basic": {"idle_down": "assets/character/idle_down/",
                                    "idle_up": "assets/character/idle_up/", 
                                    "idle_right": "assets/character/idle_right/", 
                                    "walk_down": "assets/character/walk_down/",
                                    "walk_up": "assets/character/walk_up/",
                                    "walk_right": "assets/character/walk_right/",
                                    "atk_down": "assets/character/atk_down/",
                                    "atk_up": "assets/character/atk_up/", 
                                    "atk_right": "assets/character/atk_right/",},}

        self.animation_frames = get_all_frames(self.characters["basic"])
        self.animation_frames.update({"idle_left":flip_frames(self.animation_frames["idle_right"])})
        self.animation_frames.update({"walk_left":flip_frames(self.animation_frames["walk_right"])})
        self.animation_frames.update({"atk_left":flip_frames(self.animation_frames["atk_right"])})

    def char_basic(self):
        return Character(self.animation_frames)



