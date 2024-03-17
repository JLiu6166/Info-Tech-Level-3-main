import pygame
import random
from item_files.item_creator import Item_creator


class Death:
    def __init__(self, sprite):
        # Sprite Attributes
        self.sprite = sprite
        self.action = f"death_{"right" if sprite.direction else "left"}"

        # Surface
        self.image_surface = pygame.Surface((sprite.size, sprite.size))
        self.centerx = self.image_surface.get_width()//2
        self.centery = self.image_surface.get_height()//2

        # Image Attributes
        self.frame_index = 0
        self.frame_speed = 0.2

        # Despawn
        self.sprite.death_time = pygame.time.get_ticks()
        self.sprite.despawn_time = self.sprite.death_time + self.sprite.despawn_timer

        # Loot
        self.item_creator = Item_creator()
        self.decide_loot()


    def animate(self):
        self.frame_index += self.frame_speed
        if self.frame_index >= len(self.sprite.frames[self.action]):
            self.frame_index = len(self.sprite.frames[self.action]) - 1
        self.frame_image = self.sprite.frames[self.action][int(self.frame_index)].convert_alpha()

    def compose(self):
        self.image_surface.fill("black")
        self.image_surface.blit(self.frame_image, (0, 0))
        self.image_surface.set_colorkey("black")
        self.sprite.image = self.image_surface

    def decide_loot(self):
        loot_items = list(self.sprite.loot_table.keys())
        drop_chances = list(self.sprite.loot_table.values())
        self.item = random.choices(loot_items, drop_chances, k=1)[0]

    def drop_loot(self):
        if self.item is not None:
            loot = self.item_creator.item(self.item, self.sprite.rect.center)
            self.sprite.player.loots.add(loot)

    def remove(self):
        if pygame.time.get_ticks() >= self.sprite.despawn_time:
            self.sprite.kill()
            self.drop_loot()
        
    def update(self):
        self.animate()
        self.compose()
        self.remove()

    