import pygame
from character_files.action_move import Character_Mover
from character_files.action_attack import Attack
from character_files.action_npc_interact import Interact
from character_files.action_loot import Loot

class Action:
    def __init__(self, player):
        self.player = player

        # Attack
        self.player.attacking = False
        self.player.attack_allowed = True

        # Heal
        self.player.healing = False
        self.player.heal_allowed = True

        # Movement Control
        self.character_mover = Character_Mover(player)

        # Attack Control
        self.character_attacker = Attack(player)

        # NPC Interaction
        self.interaction_controller = Interact(player)

        # Lootables
        self.loot_controller = Loot(player)

    def decide_action(self):
        # General Actions
        if self.player.direction_vector['x'] != 0 or self.player.direction_vector['y'] != 0:
            action = "walk"
        else:
            action = "idle"

        # Special Actions
        if self.player.attacking:
            action = "atk"
        if self.player.healing:
            action = "heal"

        self.player.action = action

    def update(self):
        self.decide_action()
        self.character_mover.update()
        self.character_attacker.check_attack()
        self.interaction_controller.check_interaction()
        self.loot_controller.update()