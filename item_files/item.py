import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, ID, image, position):
        super().__init__()
        self.ID = ID
        self.image = image
        self.rect = self.image.get_rect(topleft = position)