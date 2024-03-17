import pygame

class Heal:
    def __init__(self, status):
        self.status = status
        self.attack_cooldown = 1
        self.cooldown_rate = 0.1

    def check_heal(self):
        keys = pygame.key.get_pressed()
        if not self.status["healing"]:
            if keys[pygame.K_w] and self.status["heal_allowed"]:
                self.status["healing"] = True
                self.status["frame_index"] = 0
                self.attack_cooldown = 20

                self.status["heal_allowed"] = False
                self.status["attack_allowed"] = False

            if self.attack_cooldown > 0:
                self.attack_cooldown -= self.cooldown_rate
            else:
                self.status["heal_allowed"] = True
        else:
            if self.status["frame_index"] == 0:
                self.status["healing"] = False