from npc_files.npc import NPC
from utilities.image_handle import get_all_frames, flip_frames
import json

class NPC_creator():
    def __init__(self):
        self.npc = {"basic": {"idle_down": "assets/character/idle_down/",
                              "idle_up": "assets/character/idle_up/", 
                              "idle_right": "assets/character/idle_right/",},}
        self.animation_frames = get_all_frames(self.npc["basic"])
        self.animation_frames.update({"idle_left":flip_frames(self.animation_frames["idle_right"])})

        with open("npc_files/dialogue.json", "r") as json_file:
            self.npc_dialogue = json.load(json_file)

    def npc_basic(self, position, groups):
        npc_id = "npc1"
        return NPC(position, groups, self.animation_frames, npc_id, self.npc_dialogue[npc_id])