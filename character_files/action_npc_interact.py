import pygame

class Interact:
    def __init__(self, player):
        self.player = player

    def check_interaction(self):
        for npc in self.player.npcs:
            if self.player.rect.colliderect(npc.hitbox):

                # Determine NPC and Dialogue
                self.player.current_npc = npc.npc_id
                self.player.current_lines = npc.dialogue_lines

                # Determine User Inputs
                keys = pygame.key.get_pressed()
                if not self.player.npc_interacting:
                    if keys[pygame.K_SPACE]:
                        self.player.npc_interacting = True
                        self.player.draw_textbox = True
                        self.player.keypressed = True
                else:
                    if not self.player.keypressed:
                        if keys[pygame.K_SPACE]:
                            self.player.next_line = True
                            self.player.keypressed = True
                        if keys[pygame.K_ESCAPE]:
                            self.player.npc_interacting = False
                            self.player.draw_textbox = False
                if not keys[pygame.K_SPACE]:
                    self.player.keypressed = False
            
    def update(self):
        self.check_interaction()