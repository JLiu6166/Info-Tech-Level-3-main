import pygame
from enemy_files.action_patrol_AI import AI

class Patrol:
    def __init__(self, sprite):
        self.sprite = sprite
        self.player = sprite.player
        self.obstacles = sprite.obstacles

        # AI
        self.AI = AI(sprite)
        self.AI.update()

    def check_move(self):
        if self.sprite.moving:
            self.move()
        else:
            if pygame.time.get_ticks() >= self.sprite.next_move:
                self.AI.update()
                self.sprite.moving = True

    def move(self):
        self.sprite.rect.x += self.sprite.movespeed
        self.sprite.aggro_rect.centerx = self.sprite.rect.centerx

        if self.sprite.direction_x == 1 and self.sprite.rect.x >= self.sprite.target_x:
            self.sprite.moving = False
        elif self.sprite.direction_x == -1 and self.sprite.rect.x <= self.sprite.target_x:
            self.sprite.moving = False

        self.collide()
   
    def collide(self):
        for obstacle in self.obstacles:
            if obstacle.rect.colliderect(self.sprite.rect):
                if self.sprite.direction_x == 1:
                    self.sprite.rect.right = obstacle.rect.left
                elif self.sprite.direction_x == -1:
                    self.sprite.rect.left = obstacle.rect.right
                self.sprite.moving = False
        self.sprite.aggro_rect.centerx = self.sprite.rect.centerx

    def update(self):
        self.check_move()