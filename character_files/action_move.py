import pygame

class Character_Mover:
    def __init__(self, player):
        self.player = player

    def decide_direction(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.player.direction_vector['y'] = -1
            self.player.direction = "up"
        elif keys[pygame.K_DOWN]:
            self.player.direction_vector['y'] = 1
            self.player.direction = "down"
        else:
            self.player.direction_vector['y'] = 0

        if keys[pygame.K_RIGHT]:
            self.player.direction_vector['x'] = 1
            self.player.direction = "right"
        elif keys[pygame.K_LEFT]:
            self.player.direction_vector['x'] = -1
            self.player.direction = "left"
        else:
            self.player.direction_vector['x'] = 0
            
    def move(self):
        self.player.rect.centerx += self.player.direction_vector['x'] * self.player.speed
        self.player.hitbox.centerx = self.player.rect.centerx
        self.player.collisionbox.centerx = self.player.rect.centerx
        self.collide_x()
        self.player.rect.centery += self.player.direction_vector['y'] * self.player.speed
        self.player.hitbox.centery = self.player.rect.centery + 10
        self.player.collisionbox.centery = self.player.rect.centery + 20
        self.collide_y()

    def collide_x(self):
        for obstacle in self.player.obstacles:
            if obstacle.rect.colliderect(self.player.collisionbox):
                if self.player.direction_vector["x"] > 0:
                    self.player.collisionbox.right = obstacle.rect.left
                elif self.player.direction_vector["x"] < 0:
                    self.player.collisionbox.left = obstacle.rect.right
        self.player.rect.centerx = self.player.collisionbox.centerx

    def collide_y(self): 
        for obstacle in self.player.obstacles:
            if obstacle.rect.colliderect(self.player.collisionbox):
                if self.player.direction_vector["y"] > 0:
                    self.player.collisionbox.bottom = obstacle.rect.top
                elif self.player.direction_vector["y"] < 0:
                    self.player.collisionbox.top = obstacle.rect.bottom
        self.player.rect.centery = self.player.collisionbox.centery - 20

    def update(self):
        self.decide_direction()
        self.move()
