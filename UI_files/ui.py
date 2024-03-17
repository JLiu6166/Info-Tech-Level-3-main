import pygame
from utilities.config import HP_BAR_SIZE, MP_BAR_SIZE
from UI_files.textbox import Text_box
from UI_files.inventory import Inventory

class UI:
    def __init__(self, player):
        # self.player
        self.player = player

        # Screen
        self.screen = pygame.display.get_surface()
        self.screen_centerx = self.screen.get_width() // 2

        # HP/MP Bars
        self.HP_bar_background = pygame.rect.Rect((10,10), HP_BAR_SIZE)
        self.MP_bar_background = pygame.rect.Rect((10,30), MP_BAR_SIZE)

        # Attack and Skills
        self.attack_background = pygame.rect.Rect((180,10), (36, 36))
        self.magic_background = pygame.rect.Rect((220,10), (36, 36))
        self.heal_background = pygame.rect.Rect((260,10), (36, 36))

        # Text Box
        self.text_box = Text_box(0, 0, 700, 150)
        self.text_box_x = self.screen_centerx - (self.text_box.rect.width // 2)
        self.text_box_y = self.screen.get_height() - 170

        # Inventory
        self.inventory = Inventory(640, 10, 150, 200, self.player, self.screen)

    def textbox_nextline(self):
        if self.player.next_line:
            self.text_box.next_line()
            self.player.next_line = False

    def display_HP(self):
        # Update HP
        self.HP_bar = pygame.rect.Rect((10,10),((self.player.HP/self.player.max_HP)*HP_BAR_SIZE[0],HP_BAR_SIZE[1]))
        # Draw HP
        pygame.draw.rect(self.screen, (0, 0, 0), self.HP_bar_background)
        pygame.draw.rect(self.screen, (255, 0, 0), self.HP_bar)

    def display_MP(self):
        # Update MP
        self.MP_bar = pygame.rect.Rect((10,30),((self.player.MP/self.player.max_MP)*MP_BAR_SIZE[0],MP_BAR_SIZE[1]))
        # Draw MP
        pygame.draw.rect(self.screen, (0, 0, 0), self.MP_bar_background)
        pygame.draw.rect(self.screen, (0, 0, 255), self.MP_bar)

    def display_attack_satus(self):
        # Attack / Magic / Heal
        pygame.draw.rect(self.screen, (0, 0, 0), self.attack_background)
        pygame.draw.rect(self.screen, (0, 0, 0), self.magic_background)
        pygame.draw.rect(self.screen, (0, 0, 0), self.heal_background)
        
    def display_inventory(self):
        self.inventory.draw()

    def display_textbox(self):
        if self.player.draw_textbox:
            self.text_box.set_text(self.player.current_lines)
            self.text_box.draw(self.screen, self.text_box_x, self.text_box_y)

    def display(self):
        self.display_HP()
        self.display_MP()
        self.display_attack_satus()
        self.display_inventory()
        self.display_textbox()

    def update(self):
        self.display()
        self.textbox_nextline()
