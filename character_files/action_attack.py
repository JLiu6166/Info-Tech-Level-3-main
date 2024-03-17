import pygame

class Attack:
    def __init__(self, player):
        self.player = player

        self.attack_cooldown = 1
        self.cooldown_rate = 0.1

    def check_attack(self):
        keys = pygame.key.get_pressed()
        if not self.player.attacking:
            if keys[pygame.K_a] and self.player.attack_allowed:
                self.player.attacking = True
                self.player.attack_allowed = False
                self.player.frame_index = 0
                self.attack_cooldown = 1

            if self.attack_cooldown > 0:
                self.attack_cooldown -= self.cooldown_rate
            else:
                self.player.attack_allowed = True
        else:
            self.player.atk_hitbox = self.player.rect.inflate(5,5)
            self.check_damage()

            if self.player.frame_index == 0:
                self.player.attacking = False

    def check_damage(self):
        for enemy in self.player.enemies:
            if enemy.rect.colliderect(self.player.atk_hitbox):
                enemy.initiate_death()

                

    