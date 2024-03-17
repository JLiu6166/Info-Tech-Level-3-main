import pygame

class Inventory:
    def __init__(self, x, y, width, height, player, screen, font_size=24):
        self.inventory = player.inventory
        self.screen = screen
        self.x = x
        self.y = y
 
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.font = pygame.font.Font("assets/fonts/arcade.ttf", font_size)

    def sort_inventory(self):
        self.sorted_inventory = {}

        for item in self.inventory:
            if item in self.sorted_inventory:
                self.sorted_inventory[item] += 1
            else:
                self.sorted_inventory[item] = 1

    def compose(self):
        self.surface.fill((100, 100, 100, 200))
        self.rect = self.surface.get_rect()
        for i, (key, value) in enumerate(self.sorted_inventory.items()):
            if value == 1:
                text = key
            else:
                text = f"{key} ({value})"
            text = self.font.render(text, True, "black")
            text_rect = text.get_rect(left=self.rect.left + 15, top=self.rect.y + i * (self.font.get_linesize()) + 10)
            self.surface.blit(text, text_rect)
    
    def draw(self):
        self.sort_inventory()
        self.compose()
        self.screen.blit(self.surface, (self.x, self.y))

