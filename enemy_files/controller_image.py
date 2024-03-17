import pygame
from random import randint

class Image:
    def __init__(self, sprite, show_HP = False):
        # Sprite Attributes
        self.sprite = sprite
        self.frames = sprite.frames

        # Surface
        self.image_surface = pygame.Surface((sprite.size, sprite.size))
        self.centerx = self.image_surface.get_width()//2
        self.centery = self.image_surface.get_height()//2

        # HP
        self.HP_bar_width = 50
        self.max_HP = 40
        self.HP = 30
        self.show_HP = show_HP

        # Image Attributes
        self.frame_index = randint(0, 10)/10
        self.frame_speed = randint(2, 4)/100

    def animate(self):
        self.frame_index += self.frame_speed
        if self.frame_index >= len(self.frames[self.sprite.action]):
            self.frame_index = 0
        self.frame_image = self.frames[self.sprite.action][int(self.frame_index)].convert_alpha()

    def update_HP_bar(self, HP, max_HP):
        HP_bar_background = pygame.Surface((self.HP_bar_width, 5))
        HP_bar_background.fill((255,0,0))
        HP_bar_health = pygame.rect.Rect((0,0),((HP/self.max_HP)*self.HP_bar_width,5))
        pygame.draw.rect(HP_bar_background, (0,255,0), HP_bar_health)
        return HP_bar_background

    def compose(self):
        self.image_surface.fill("black")
        self.image_surface.blit(self.frame_image, (0, 0))

        if self.show_HP:
            HP_bar = self.update_HP_bar()
            self.image_surface.blit(HP_bar, ((self.centerx - self.HP_bar_width)//2, 5))
        
        self.image_surface.set_colorkey("black")

        self.sprite.image = self.image_surface
        #pygame.draw.rect(self.image_surface, (255,0,255), (0, 0, self.rect.width, self.rect.height), 3)
        #pygame.draw.rect(self.image_surface, (0,0,255), (0, 0, self.hitbox.width, self.hitbox.height), 2)
        
    def update(self):
        self.animate()
        self.update_HP_bar(self.HP, self.max_HP)
        self.compose()

    