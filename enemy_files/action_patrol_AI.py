import pygame
from random import randint, choice

class AI:
    def __init__(self, sprite):
        self.sprite = sprite
        
        self.movespeed_min = 2
        self.movespeed_max = 4
        self.move_distance_min = 40
        self.move_distance_max = 110

    def decide_direction(self):
        if self.sprite.rect.x <= self.sprite.spawn_point_x - self.sprite.leash_distance:
            direction = 1
        elif self.sprite.rect.x >= self.sprite.spawn_point_x + self.sprite.leash_distance:
            direction = -1
        else:
            direction = choice([1, -1])
        self.sprite.direction_x = direction
    
    def decide_movespeed(self):
        self.sprite.movespeed = randint(self.movespeed_min, self.movespeed_max) * self.sprite.direction

    def decide_target(self):
        self.sprite.target_x = self.sprite.rect.x + (randint(self.move_distance_min, self.move_distance_max) * self.sprite.direction)

    def decide_next_move(self):
        self.sprite.next_move = pygame.time.get_ticks() + randint(7, 18)*1000
    
    def update(self):
        self.decide_direction()
        self.decide_movespeed()
        self.decide_target()
        self.decide_next_move()