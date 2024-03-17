from enemy_files.action_patrol import Patrol
from enemy_files.action_aggro import Aggro

class Action:
    def __init__(self, sprite):
        self.sprite = sprite

        # Sprite State
        self.status = "patrol"

        # Patrol Controller
        self.patrol_controller = Patrol(sprite)

        # Aggro Controller
        self.aggro_controller = Aggro(sprite)

    def check_status(self):
        if self.sprite.aggro_rect.colliderect(self.sprite.player.rect) and self.sprite.hostile:
            self.status = "aggro"
            if not self.sprite.attacking:
                self.sprite.action = f"move_{'right' if self.sprite.direction_x == 1 else 'left'}"
            else:         
                self.sprite.action = f"attack_{'right' if self.sprite.direction_x == 1 else 'left'}"
        else:
            self.status = "patrol"
            if self.sprite.moving:
                self.sprite.action = f"move_{'right' if self.sprite.direction_x == 1 else 'left'}"                
            else:
                self.sprite.action = f"idle_{'right' if self.sprite.direction_x == 1 else 'left'}"

    def update(self):
        self.check_status()
        if self.status == "patrol":
            self.patrol_controller.update()
        elif self.status == "aggro":
            self.aggro_controller.update()