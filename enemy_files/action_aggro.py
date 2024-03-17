import pygame

class Aggro:
    def __init__(self, sprite):
        self.sprite = sprite

        # Aggro Rect
        self.aggro = False
        self.aggro_rect = self.sprite.rect.inflate(100, 100)

        # Attack
        self.sprite.attacking = False
        self.attack_duration = 2000
        self.attack_finish = 0

        self.attack_allowed = True
        self.attack_cooldown = 1000
        self.next_attack = 0
        self.damage = 1

    def direction(self):
        self.x_dist = self.sprite.player.rect.centerx - self.sprite.rect.centerx
        self.y_dist = self.sprite.player.rect.centery - self.sprite.rect.centery

        self.sprite.direction_x = 1  if self.x_dist > 0 else -1
        self.sprite.direction_y = 1  if self.y_dist > 0 else -1

    def player_chase(self):
        if abs(self.x_dist) >= 10:
            self.sprite.rect.centerx += self.sprite.movespeed * self.sprite.direction_x
            self.collide_x()
            self.sprite.aggro_rect.centerx = self.sprite.rect.centerx
        if abs(self.y_dist) >= 10:
            self.sprite.rect.centery += self.sprite.movespeed * self.sprite.direction_y
            self.collide_y()    
            self.sprite.aggro_rect.centery = self.sprite.rect.centery  

    def attack(self):
        if (abs(self.x_dist) <= 10 or abs(self.y_dist) <= 10) and self.attack_allowed:
            self.sprite.attacking = True
            self.next_attack = pygame.time.get_ticks() + self.attack_cooldown
            self.attack_finish = pygame.time.get_ticks() + self.attack_duration
            self.attack_allowed = False
            if self.sprite.rect.colliderect(self.sprite.player.rect):
                self.sprite.player.HP -= self.damage

        if pygame.time.get_ticks() >= self.next_attack:
            self.attack_allowed = True
        if pygame.time.get_ticks() >= self.attack_finish:
            self.sprite.attacking = False


    def collide_x(self):
        for obstacle in self.sprite.obstacles:
            if obstacle.rect.colliderect(self.sprite.rect):
                if self.sprite.direction_x > 0:
                    self.sprite.rect.right = obstacle.rect.left
                elif self.sprite.direction_x < 0:
                    self.sprite.rect.left = obstacle.rect.right

    def collide_y(self): 
        for obstacle in self.sprite.obstacles:
            if obstacle.rect.colliderect(self.sprite.rect):
                if self.sprite.direction_y > 0:
                    self.sprite.rect.bottom = obstacle.rect.top
                elif self.sprite.direction_y < 0:
                    self.sprite.rect.top = obstacle.rect.bottom

    def update(self):
        self.direction()
        self.player_chase()
        self.attack()
