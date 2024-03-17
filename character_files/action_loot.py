import pygame

class Loot:
    def __init__(self, player):
        self.player = player

    def pick_up_loot(self):
        for item in self.player.loots:
            if self.player.rect.colliderect(item.rect):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.player.inventory.append(item.ID)
                    item.kill()

    def update(self):
        self.pick_up_loot()